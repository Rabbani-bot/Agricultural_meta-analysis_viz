# SECTION 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import os # Ensure this is imported for path operations

# SECTION 2: Global Styling Setup (rcParams)
# These are general settings for how your plots will look
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 4,
    'axes.titlesize': 5,
    'axes.labelsize': 4,
    'xtick.labelsize': 4,
    'ytick.labelsize': 4,
    'figure.facecolor': 'none', # We will explicitly set the figure's patch color later
    'axes.facecolor': 'white',  # Default background for the plot areas themselves to white
    'savefig.transparent': False # Ensure saved figures are not transparent by default
})

# SECTION 3: Define Consistent Colors and Styles for Plots
# These are specific style choices for elements within your plots
STUDY_ERRORBAR_COLOR = 'lightslategray'
STUDY_ERRORBAR_LINEWIDTH = 1.2
STUDY_MARKER_SIZE = 3
STUDY_MARKER_EDGEWIDTH = 0.6
STUDY_MARKER_FACECOLOR = 'white'

GRANDMEAN_COLOR = '#475877'
GRANDMEAN_LINEWIDTH = 1.3
GRANDMEAN_MARKER_SIZE = 4
GRANDMEAN_MARKER_EDGEWIDTH = 0.7
GRANDMEAN_MARKER_FACECOLOR = 'white'

ERRORBAR_ALPHA = 1.0
STRUCTURAL_LINE_COLOR = 'dimgray'
STRUCTURAL_LINE_WIDTH = 0.5
GRID_COLOR = 'lightgray'
GRID_LINEWIDTH = 0.4
GRID_LINESTYLE = '--'
ZERO_LINE_COLOR = 'lightcoral'
ZERO_LINE_WIDTH = 0.6
ZERO_LINE_STYLE = '--'

FIGURE_OUTSIDE_COLOR = '#EAF6FF' # Light blue for the FIGURE's background

# SECTION 4: Function to Draw Plot 1 (Left Plot - N2O)
def draw_plot1(ax):
    ax.set_facecolor('white')
    data1 = {
        "Study": ["Cai et al (2017) ", "Ma et al (2023)", "Fan et al (2022)", "Liao et al (2021)", "Tufail et al (2023)", "Thapa et al (2016)", "Di Wu et al (2021)", "Ribeiro et al (2023)", "Soares et al (2023)", "Wang et al (2024)", "Grand mean"],
        "L1": [-0.002033886, -0.085681899, 0.006026948, 0.022212993, -0.120704656, -0.113818774, -0.6698780909, -0.9395422339, -0.9592365826, -0.6647951034, -0.6802914917],
        "L2": [-0.2075265192, -0.1464455668, -0.4965336415, -0.4008631672, -0.554127865, -0.3431529298, -0.2991557559, -0.4292441277, -0.7082604559, -0.4461406026, -0.4344652722],
        "Mean": [-0.3021983951, -0.3270452054, -0.5352054846, -0.6792955445, -0.6415707825, -0.5643638738,-0.4845169234, -0.6843931808, -0.8337485192, -0.555467853, -0.5573783819],
        "Numbers": [138, 217, 656, 38, 180, 123, 60, 74, 269, 144, 1899],
        "SE": [0.04830197747, 0.0921426777, 0.01973053218, 0.1420573353, 0.04461373342, 0.1128627266, 0.09457202422, 0.1301780883, 0.06402452211, 0.05577920939, 0.0627107703]
    }
    df_original1 = pd.DataFrame(data1)
    grand_mean_row1 = df_original1[df_original1['Study'] == 'Grand mean']
    studies_df1 = df_original1[df_original1['Study'] != 'Grand mean'].copy()
    studies_df1['error_bar_length'] = studies_df1['L2'] - studies_df1['L1']
    studies_df_sorted1 = studies_df1.sort_values(by='error_bar_length', ascending=True)
    df1 = pd.concat([studies_df_sorted1, grand_mean_row1]).reset_index(drop=True)
    n_sum_calculated1 = df_original1[df_original1['Study'] != 'Grand mean']['Numbers'].sum()

    ax.set_title('Overall', fontweight='bold', loc='center')
    y_pos1 = np.arange(len(df1))
    gm_idx1 = df1.index[df1['Study'] == "Grand mean"][0]
    divider_y1 = gm_idx1 - 0.5

    DESIRED_XTICKS1 = np.array([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2])
    main_plot_data_xmin1 = DESIRED_XTICKS1.min() - 0.05
    main_plot_data_xmax1 = DESIRED_XTICKS1.max() + 0.05
    box_width1 = 0.27
    box_start_x1 = main_plot_data_xmax1
    numbers_text_x_center1 = box_start_x1 + (box_width1 / 2)
    figure_content_xmax1 = box_start_x1 + box_width1

    ax.set_xlim(main_plot_data_xmin1, figure_content_xmax1)
    ax.set_xticks(DESIRED_XTICKS1)
    ax.set_xticklabels([f"{t:.1f}" for t in DESIRED_XTICKS1])

    for y_coord in y_pos1:
        ax.hlines(y_coord, xmin=main_plot_data_xmin1, xmax=main_plot_data_xmax1, color=GRID_COLOR,
                  linewidth=GRID_LINEWIDTH, linestyle=GRID_LINESTYLE, zorder=0.5)

    for i, row in df1.iterrows():
        is_grand_mean = (row['Study'] == "Grand mean")
        current_ebar_color = GRANDMEAN_COLOR if is_grand_mean else STUDY_ERRORBAR_COLOR
        current_ebar_lw = GRANDMEAN_LINEWIDTH if is_grand_mean else STUDY_ERRORBAR_LINEWIDTH
        current_marker_shape = 'D'
        current_marker_size = GRANDMEAN_MARKER_SIZE if is_grand_mean else STUDY_MARKER_SIZE
        current_marker_ew = GRANDMEAN_MARKER_EDGEWIDTH if is_grand_mean else STUDY_MARKER_EDGEWIDTH
        current_marker_facecolor = GRANDMEAN_MARKER_FACECOLOR
        current_marker_edgecolor = current_ebar_color

        ax.hlines(y=y_pos1[i], xmin=row['L1'], xmax=row['L2'],
                  color=current_ebar_color, linewidth=current_ebar_lw,
                  linestyle='-', alpha=ERRORBAR_ALPHA, zorder=3)
        center_x = row['Mean']
        ax.plot(center_x, y_pos1[i], current_marker_shape,
                markerfacecolor=current_marker_facecolor,
                markeredgecolor=current_marker_edgecolor,
                markersize=current_marker_size,
                markeredgewidth=current_marker_ew,
                alpha=ERRORBAR_ALPHA, zorder=5)

    ax.axvline(0, color=ZERO_LINE_COLOR, linewidth=ZERO_LINE_WIDTH, linestyle=ZERO_LINE_STYLE,
              ymax=(gm_idx1) / len(df1) if len(df1) > 0 else 0, zorder=2)
    ax.hlines(y=divider_y1, xmin=main_plot_data_xmin1, xmax=figure_content_xmax1,
              color=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
              linestyle='-', zorder=1.1)

    plot_ymin_explicit1 = -0.5
    plot_ymax_explicit1 = len(df1) - 1 + 0.5
    ax.add_patch(Rectangle((box_start_x1, plot_ymin_explicit1), box_width1, plot_ymax_explicit1 - plot_ymin_explicit1,
                           facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
                           clip_on=False, zorder=1))
    gm_row_y_center1 = y_pos1[gm_idx1]
    ax.add_patch(Rectangle((box_start_x1, gm_row_y_center1 - 0.5), box_width1, 1.0,
                           facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
                           clip_on=False, zorder=1.2))

    for i, row in df1.iterrows():
        txt_to_display = f"{int(n_sum_calculated1)}" if row['Study'] == "Grand mean" else (f"{int(row['Numbers'])}" if pd.notna(row['Numbers']) else "")
        if txt_to_display:
            ax.text(numbers_text_x_center1, y_pos1[i], txt_to_display,
                    ha='center', va='center', fontsize=plt.rcParams['xtick.labelsize'],
                    color='black', fontweight='normal', zorder=2)

    ax.set_yticks(y_pos1)
    ax.set_yticklabels(df1['Study'], linespacing=1.0)
    if gm_idx1 != -1 and gm_idx1 < len(ax.get_yticklabels()):
        ax.get_yticklabels()[gm_idx1].set_fontweight('bold')

    ax.set_ylabel('(References)', rotation=90, va='center', labelpad=4)
    ax.set_xlabel(r'RR (N$_2$O)', fontweight='bold') # (%) was removed as per your general instruction
    ax.set_ylim(plot_ymin_explicit1, plot_ymax_explicit1)

    ax.tick_params(axis='both', which='major', direction='out', length=1.5, width=0.2, pad=1.0)
    ax.spines['left'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['left'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['bottom'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_bounds(main_plot_data_xmin1, figure_content_xmax1)
    ax.spines['top'].set_visible(True)
    ax.spines['top'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['top'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['top'].set_bounds(main_plot_data_xmin1, figure_content_xmax1)
    ax.spines['right'].set_visible(True)
    ax.spines['right'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['right'].set_linewidth(STRUCTURAL_LINE_WIDTH)


# SECTION 5: Function to Draw Plot 2 (Right Plot - Yield)
def draw_plot2(ax):
    ax.set_facecolor('white')
    data2 = {
        "Study": ["Ma et al (2023)", "Cai et al (2017)", "Fan et al (2022)", "Liao et al (2021)", "Tufail et al (2023)", "Thapa et al (2016)", "Abalos et al (2014)", "Ribeiro et al (2023)", "Wang et al (2024)", "Grand mean"],
        "L1": [-0.085681899, -0.002033886001, 0.006026947998, 0.02221299303, -0.120704656, -0.1138187743, 0.02351739823, -0.03722381183, 0.03039437643, -0.02032692129],
        "L2": [0.1889940519, 0.1541452923, 0.0566177146, 0.1560828779, 0.01442945, 0.1629045606, 0.1158370324, 0.101194414, 0.09394816161, 0.104084878],
        "Mean": [0.05165607648, 0.07605570316, 0.0313223313, 0.08914793545, -0.053137603, 0.02454289314, 0.06967721532, 0.03198530107, 0.06217126902, 0.04187897838],
        "Numbers": [68, 92, 328, 39, 125, 81, 275, 109, 223, 1340],
        "SE": [0.07007039563, 0.03984162712, 0.01290580781, 0.03415048082, 0.03447298622, 0.07059268746, 0.02355092708, 0.03531077189, 0.0162127003, 0.03173770391]
    }
    df_original2 = pd.DataFrame(data2)
    grand_mean_row2 = df_original2[df_original2['Study'] == 'Grand mean']
    studies_df2 = df_original2[df_original2['Study'] != 'Grand mean'].copy()
    studies_df2['error_bar_length'] = studies_df2['L2'] - studies_df2['L1']
    studies_df_sorted2 = studies_df2.sort_values(by='error_bar_length', ascending=True)
    df2 = pd.concat([studies_df_sorted2, grand_mean_row2]).reset_index(drop=True)
    n_sum_calculated2 = df_original2[df_original2['Study'] != 'Grand mean']['Numbers'].sum()

    ax.set_title('Overall', fontweight='bold', loc='center')
    y_pos2 = np.arange(len(df2))
    gm_idx2 = df2.index[df2['Study'] == "Grand mean"][0]
    divider_y2 = gm_idx2 - 0.5

    DESIRED_XTICKS2 = np.array([-0.1, 0.0, 0.1, 0.2])
    main_plot_data_xmin2 = DESIRED_XTICKS2.min() - 0.05
    main_plot_data_xmax2 = DESIRED_XTICKS2.max() + 0.05
    box_width2 = 0.08
    box_start_x2 = main_plot_data_xmax2
    numbers_text_x_center2 = box_start_x2 + (box_width2 / 2)
    figure_content_xmax2 = box_start_x2 + box_width2

    ax.set_xlim(main_plot_data_xmin2, figure_content_xmax2)
    ax.set_xticks(DESIRED_XTICKS2)
    ax.set_xticklabels([f"{t:.1f}" for t in DESIRED_XTICKS2])

    for y_coord in y_pos2:
        ax.hlines(y_coord, xmin=main_plot_data_xmin2, xmax=main_plot_data_xmax2, color=GRID_COLOR,
                  linewidth=GRID_LINEWIDTH, linestyle=GRID_LINESTYLE, zorder=0.5)

    for i, row in df2.iterrows():
        is_grand_mean = (row['Study'] == "Grand mean")
        current_ebar_color = GRANDMEAN_COLOR if is_grand_mean else STUDY_ERRORBAR_COLOR
        current_ebar_lw = GRANDMEAN_LINEWIDTH if is_grand_mean else STUDY_ERRORBAR_LINEWIDTH
        current_marker_shape = 'D'
        current_marker_size = GRANDMEAN_MARKER_SIZE if is_grand_mean else STUDY_MARKER_SIZE
        current_marker_ew = GRANDMEAN_MARKER_EDGEWIDTH if is_grand_mean else STUDY_MARKER_EDGEWIDTH
        current_marker_facecolor = GRANDMEAN_MARKER_FACECOLOR
        current_marker_edgecolor = current_ebar_color

        ax.hlines(y=y_pos2[i], xmin=row['L1'], xmax=row['L2'],
                  color=current_ebar_color, linewidth=current_ebar_lw,
                  linestyle='-', alpha=ERRORBAR_ALPHA, zorder=3)
        center_x = row['Mean']
        ax.plot(center_x, y_pos2[i], current_marker_shape,
                markerfacecolor=current_marker_facecolor,
                markeredgecolor=current_marker_edgecolor,
                markersize=current_marker_size,
                markeredgewidth=current_marker_ew,
                alpha=ERRORBAR_ALPHA, zorder=5)

    ax.axvline(0, color=ZERO_LINE_COLOR, linewidth=ZERO_LINE_WIDTH, linestyle=ZERO_LINE_STYLE,
              ymax=(gm_idx2) / len(df2) if len(df2) > 0 else 0, zorder=2)
    ax.hlines(y=divider_y2, xmin=main_plot_data_xmin2, xmax=figure_content_xmax2,
              color=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
              linestyle='-', zorder=1.1)

    plot_ymin_explicit2 = -0.5
    plot_ymax_explicit2 = len(df2) - 1 + 0.5
    ax.add_patch(Rectangle((box_start_x2, plot_ymin_explicit2), box_width2, plot_ymax_explicit2 - plot_ymin_explicit2,
                           facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
                           clip_on=False, zorder=1))
    gm_row_y_center2 = y_pos2[gm_idx2]
    ax.add_patch(Rectangle((box_start_x2, gm_row_y_center2 - 0.5), box_width2, 1.0,
                           facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH,
                           clip_on=False, zorder=1.2))

    for i, row in df2.iterrows():
        txt_to_display = f"{int(n_sum_calculated2)}" if row['Study'] == "Grand mean" else (f"{int(row['Numbers'])}" if pd.notna(row['Numbers']) else "")
        if txt_to_display:
            ax.text(numbers_text_x_center2, y_pos2[i], txt_to_display,
                    ha='center', va='center', fontsize=plt.rcParams['xtick.labelsize'],
                    color='black', fontweight='normal', zorder=2)

    ax.set_yticks(y_pos2)
    ax.set_yticklabels(df2['Study'], linespacing=1.0)
    if gm_idx2 != -1 and gm_idx2 < len(ax.get_yticklabels()):
        ax.get_yticklabels()[gm_idx2].set_fontweight('bold')

    # (References) y-label removed for the right plot
    ax.set_xlabel(r'RR (Yield)', fontweight='bold') # (%) was removed as per your general instruction
    ax.set_ylim(plot_ymin_explicit2, plot_ymax_explicit2)

    ax.tick_params(axis='both', which='major', direction='out', length=1.5, width=0.2, pad=1.0)
    ax.spines['left'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['left'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['bottom'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_bounds(main_plot_data_xmin2, figure_content_xmax2)
    ax.spines['top'].set_visible(True)
    ax.spines['top'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['top'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['top'].set_bounds(main_plot_data_xmin2, figure_content_xmax2)
    ax.spines['right'].set_visible(True)
    ax.spines['right'].set_color(STRUCTURAL_LINE_COLOR)
    ax.spines['right'].set_linewidth(STRUCTURAL_LINE_WIDTH)


# SECTION 6: Main Script to Create and Save Side-by-Side Plots
width_cm = 8
width_inches = width_cm / 2.54
original_height_inches = 1.7 # Keeping this from your original individual plot structure

# SUB-SECTION 6.1: Create Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width_inches, original_height_inches), dpi=600)

# Setting the FIGURE's (outside area) background color and ensuring it's opaque
fig.patch.set_facecolor(FIGURE_OUTSIDE_COLOR)
fig.patch.set_alpha(1.0)

# SUB-SECTION 6.2: Draw the Plots (Original order: N2O on left, Yield on right)
draw_plot1(ax1) # This function draws the N2O plot on ax1 (left)
draw_plot2(ax2) # This function draws the Yield plot on ax2 (right)

# SUB-SECTION 6.3: Adjust Layout
plt.tight_layout(pad=0.5, w_pad=1.0) # Using settings from your last confirmed working code

# SUB-SECTION 6.4: Save and Show Plot (MODIFIED FOR YOUR SPECIFIC PATH)

# 1. Define the directory part of your custom path
#    custom_directory 


# 2. Define your base filename. Since the plots are "Overall", let's make a generic name.
base_filename_for_save = "Overall finals"

# 3. Create the custom directory if it doesn't exist
try:
    if not os.path.exists(custom_directory):
        os.makedirs(custom_directory)
        print(f"Successfully created directory: {custom_directory}")
    else:
        print(f"Directory already exists: {custom_directory}")
except Exception as e:
    print(f"--------------------------------------------------------------------")
    print(f"ERROR: Could not create or access directory: {custom_directory}")
    print(f"Error details: {e}")
    print(f"Please ensure the path is correct (e.g., 'Researcher' spelling) and you have write permissions.")
    custom_directory = "." # Fallback: save in the current directory
    print(f"Figures will be saved to the current directory: {os.path.abspath(custom_directory)}")
    print(f"--------------------------------------------------------------------")

# 4. Construct the full file paths for PNG and TIFF using os.path.join
full_path_png = os.path.join(custom_directory, base_filename_for_save + ".png")
full_path_tiff = os.path.join(custom_directory, base_filename_for_save + ".tiff")

# 5. Get the figure's actual facecolor to pass to savefig for consistency
figure_actual_facecolor_for_saving = fig.get_facecolor()

# 6. Save as PNG to the constructed full path
try:
    plt.savefig(full_path_png,
                dpi=600,
                bbox_inches='tight',
                facecolor=figure_actual_facecolor_for_saving,
                transparent=False)
    print(f"Figure saved as PNG: {full_path_png}")
except Exception as e:
    print(f"Error saving PNG to {full_path_png}: {e}")

# 7. Save as TIFF to the constructed full path
try:
    plt.savefig(full_path_tiff,
                dpi=600,
                bbox_inches='tight',
                facecolor=figure_actual_facecolor_for_saving,
                transparent=False)
    print(f"Figure saved as TIFF: {full_path_tiff}")
except Exception as e:
    print(f"Error saving TIFF to {full_path_tiff}: {e}")

plt.show()
