# SECTION 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import os
import matplotlib.transforms as transforms

# SECTION 2: Global Styling Setup (rcParams)
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 4,
    'axes.titlesize': 3,
    'axes.labelsize': 3,
    'xtick.labelsize': 2.3,
    'ytick.labelsize': 2.3, # Adjusted from your provided code for y-tick labels like ' Banded'
    'figure.facecolor': 'none',
    'axes.facecolor': 'white',
    'savefig.transparent': False
})

# SECTION 3: Define Consistent Colors and Styles for Plots
STRUCTURAL_LINE_COLOR = 'dimgray'
STRUCTURAL_LINE_WIDTH = 0.5
FIGURE_OUTSIDE_COLOR = '#EAF6FF'

# SECTION 4: Function to Draw "Fertilizers and Nitrogen (N2O)" Plot (Left)
def draw_new_plot_right(ax): # This function draws the N2O plot
    ax.set_facecolor('white')
    new_data_structured_plot2 = [
        {'sub_category': 'Irrigation ', 'display_label': '  Irrigated ',   'N': 455, 'L1': 0.07258868582,  'L2': 0.2567284469, 'type': 'factor'},
        {'sub_category': 'Irrigation ', 'display_label': ' Rainfed ','N': 390, 'L1': -0.04517994696,  'L2': 0.2500873777, 'type': 'factor'},
        {'sub_category': 'Tillage ', 'display_label': '   No-till ', 'N': 94,  'L1': -0.5102707987,  'L2': -0.1309050162, 'type': 'factor'},
        {'sub_category': 'Tillage ', 'display_label': '  Tilled ', 'N': 132,  'L1': -0.5665261941,  'L2': -0.2621682374, 'type': 'factor'},
        {'sub_category': 'Land Use ', 'display_label': '  Lowland ',    'N': 214, 'L1': -0.5422677975, 'L2': -0.3738603451, 'type': 'factor'},
        {'sub_category': 'Land Use ', 'display_label': '  Grassland ','N': 63,  'L1': -0.6322132661, 'L2': -0.3527624608, 'type': 'factor'},
        {'sub_category': 'Crop type ', 'display_label': '  Cereals ',   'N': 287, 'L1': -0.6062237387, 'L2': -0.2734526486, 'type': 'factor'},
        {'sub_category': 'Crop type ', 'display_label': '  Mixed ', 'N': 59, 'L1': -1.068364718, 'L2': -0.5855453734, 'type': 'factor'},
        {'sub_category': 'Climate zones ', 'display_label': '  Climate types ', 'N': 672, 'L1': 0.05658725911, 'L2': 0.3412975117, 'type': 'factor'},
        {'sub_category': 'Climate zones ', 'display_label': '  Seasons ', 'N': 101, 'L1': -0.8732754141, 'L2': -0.5217038467,  'type': 'factor'},
        {'sub_category': 'Climatic parameters ', 'display_label': '  0-1500 mm ', 'N': 599,  'L1': 0.2843992855,  'L2': 0.4954671586, 'type': 'factor'},
        {'sub_category': 'Inhibitor ', 'display_label': '  Type', 'N': 596,  'L1': 0.2737371301,  'L2': 0.4972695813, 'type': 'factor'},
        {'sub_category': 'Inhibitor ', 'display_label': '  Type', 'N': 596,  'L1': 0.2737371301,  'L2': 0.4972695813, 'type': 'factor'},
        {'sub_category': 'Crop type ', 'display_label': '  Mixed ', 'N': 59, 'L1': -1.068364718, 'L2': -0.5855453734, 'type': 'factor'},
        {'sub_category': 'Climate zones ', 'display_label': '  Climate types ', 'N': 672, 'L1': 0.05658725911, 'L2': 0.3412975117, 'type': 'factor'},
        {'sub_category': 'Inhibitor Type ', 'display_label': '  DI ', 'N': 101, 'grand mean': -0.444722534, 'SE*1.96': 0.190931935,  'type': 'factor'},
        {'sub_category': 'Inhibitor Type ', 'display_label': '  UI ', 'N': 599,  'grand mean': -0.194914849,  'SE*1.96': 0.4954671586, 'type': 'factor'},
        {'sub_category': 'Inhibitor Type ', 'display_label': '  NI', 'N': 596,  'grand mean': -0.475671889,  'SE*1.96': 0.4972695813, 'type': 'factor'},


        
    ]
    df = pd.DataFrame(new_data_structured_plot2)

    PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR = 'lightslategray'; PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH = 1.2; PLOT_SPECIFIC_STUDY_MARKER_SIZE = 3
    PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH = 0.6; PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR = 'white'; PLOT_SPECIFIC_ERRORBAR_ALPHA = 1.0
    PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR = 'lightblue'; PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH = 0.5; PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE = '--'
    PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE = 3.2 ### MODIFIED for visibility
    PLOT_SPECIFIC_SUBCAT_TEXT_COLOR = 'black';
    PLOT_SPECIFIC_GRID_COLOR = 'lightgray'; PLOT_SPECIFIC_GRID_LINEWIDTH = 0.4; PLOT_SPECIFIC_GRID_LINESTYLE = '-'
    PLOT_SPECIFIC_ZERO_LINE_COLOR = 'lightcoral'; PLOT_SPECIFIC_ZERO_LINE_WIDTH = 0.8; PLOT_SPECIFIC_ZERO_LINE_STYLE = '--'
    PLOT_SPECIFIC_CATEGORY_BAR_COLOR = 'dimgray' ### MODIFIED
    PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH = 0.4  ### MODIFIED

    ax.set_title('Agriculture practices', fontweight='bold', loc='center', fontsize=plt.rcParams['axes.titlesize']) # Title from your code
    y_pos = np.arange(len(df))

    PLOT_SPECIFIC_DESIRED_XTICKS = np.array([-1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6]) # From your code
    tick_step = PLOT_SPECIFIC_DESIRED_XTICKS[1] - PLOT_SPECIFIC_DESIRED_XTICKS[0] if len(PLOT_SPECIFIC_DESIRED_XTICKS) > 1 else 0.2
    main_plot_data_xmin = PLOT_SPECIFIC_DESIRED_XTICKS.min() - tick_step / 2
    main_plot_data_xmax = PLOT_SPECIFIC_DESIRED_XTICKS.max() + tick_step / 2
    
    plot_width_for_n_box = main_plot_data_xmax - main_plot_data_xmin
    box_width = plot_width_for_n_box * 0.16 # From your code
    box_start_x = main_plot_data_xmax + plot_width_for_n_box * 0.02
    numbers_text_x_center = box_start_x + (box_width / 2)
    figure_content_xmax = box_start_x + box_width

    ax.set_xlim(main_plot_data_xmin, figure_content_xmax)
    ax.set_xticks(PLOT_SPECIFIC_DESIRED_XTICKS)
    ax.set_xticklabels([f"{t:.1f}" for t in PLOT_SPECIFIC_DESIRED_XTICKS], fontsize=plt.rcParams['xtick.labelsize'])

    def format_subcategory_display_name_plot_N2O(original_sub_cat_name):
        key = original_sub_cat_name.strip()
        if "Irrigation" == key: return "Irrigation"
        if "Tillage" == key: return "Tillage"
        if "Land Use" == key: return "Land\nUse" ### MODIFIED for multi-line
        if "Crop type" == key: return "Crop\ntype" ### MODIFIED for multi-line
        if "Climate zones" == key: return "Climate\nzones" ### MODIFIED for multi-line
        if "Climatic parameters" == key: return "Climatic\nparameters" ### MODIFIED for multi-line
        # Fallback for any other keys from your specific N2O data if they were missed in mapping
        if "Fertilizer appplication" == key: return "Fertilizer\napplication"
        if "Nitrogen rate" == key: return "Nitrogen\nrate"
        if "Nitrogen sources" == key: return "Nitrogen\nsources"
        if "Nitrogen content" == key: return "Nitrogen\ncontent"
        if "Nitrogen amount" == key: return "Nitrogen\namount"
        return key

    subcat_display_info = []
    ordered_subcategories = df['sub_category'].unique()
    for sub_cat_name_orig in ordered_subcategories:
        group_rows_indices = df[df['sub_category'] == sub_cat_name_orig].index
        if not group_rows_indices.empty:
            y_coords_for_group = y_pos[group_rows_indices]
            center_y = (np.min(y_coords_for_group) + np.max(y_coords_for_group)) / 2.0
            display_text = format_subcategory_display_name_plot_N2O(sub_cat_name_orig)
            subcat_display_info.append({'text_to_plot': display_text, 'center_y': center_y,
                                        'min_y_group': np.min(y_coords_for_group), 'max_y_group': np.max(y_coords_for_group)})

    current_sub_category_for_grouping = None
    if len(df) > 0:
        for i, row_data in df.iterrows():
            if row_data['sub_category'] != current_sub_category_for_grouping:
                if current_sub_category_for_grouping is not None and i > 0:
                    ax.hlines(y_pos[i] - 0.5, main_plot_data_xmin, main_plot_data_xmax, color=PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR, linewidth=PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH, linestyle=PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE, zorder=0.6)
                current_sub_category_for_grouping = row_data['sub_category']
            ax.hlines(y_pos[i], main_plot_data_xmin, main_plot_data_xmax, color=PLOT_SPECIFIC_GRID_COLOR, linewidth=PLOT_SPECIFIC_GRID_LINEWIDTH, linestyle=PLOT_SPECIFIC_GRID_LINESTYLE, zorder=0.5)
    
    PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR = -0.29 ### MODIFIED: Anchor for CENTER of text block
    PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC = -0.25 ### MODIFIED: Bar to the LEFT of text block

    blended_transform = transforms.blended_transform_factory(ax.transAxes, ax.transData)

    for vert_label_info in subcat_display_info:
        ax.text(PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR, vert_label_info['center_y'], vert_label_info['text_to_plot'],
                transform=blended_transform, rotation=90, 
                ha='center', va='center',  ### MODIFIED: ha='center' for better multi-line alignment
                fontsize=PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE, color=PLOT_SPECIFIC_SUBCAT_TEXT_COLOR, clip_on=False, zorder=2.5)
        bar_y_start = vert_label_info['min_y_group'] - 0.3 # Adjusted extension
        bar_y_end = vert_label_info['max_y_group'] + 0.3   # Adjusted extension
        ax.plot([PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC, PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC], [bar_y_start, bar_y_end],
                color=PLOT_SPECIFIC_CATEGORY_BAR_COLOR, linewidth=PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH,
                transform=blended_transform, clip_on=False, zorder=1.0)

    for i, row_data in df.iterrows():
        ax.hlines(y=y_pos[i], xmin=row_data['L1'], xmax=row_data['L2'], color=PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR, linewidth=PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH, alpha=PLOT_SPECIFIC_ERRORBAR_ALPHA, zorder=3)
        center_x = (row_data['L1'] + row_data['L2']) / 2
        ax.plot(center_x, y_pos[i], 'D', markerfacecolor=PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR, markeredgecolor=PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR, markersize=PLOT_SPECIFIC_STUDY_MARKER_SIZE, markeredgewidth=PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH, alpha=PLOT_SPECIFIC_ERRORBAR_ALPHA, zorder=5)

    ax.axvline(0, color=PLOT_SPECIFIC_ZERO_LINE_COLOR, linewidth=PLOT_SPECIFIC_ZERO_LINE_WIDTH, linestyle=PLOT_SPECIFIC_ZERO_LINE_STYLE, ymax=1.0, zorder=2)
    
    current_ylim_for_box_and_final_plot = (-0.5, len(df) - 0.5) if len(df) > 0 else (-0.5, 0.5)
    ax.add_patch(Rectangle((box_start_x, current_ylim_for_box_and_final_plot[0]), box_width, current_ylim_for_box_and_final_plot[1] - current_ylim_for_box_and_final_plot[0], facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH, clip_on=False, zorder=1))
    for i, row_data in df.iterrows():
        if pd.notna(row_data['N']):
            ax.text(numbers_text_x_center, y_pos[i], f"{int(row_data['N'])}", 
                    ha='center', va='center', 
                    fontsize=plt.rcParams['ytick.labelsize'], 
                    color='black', 
                    fontweight='bold', # N-box numbers bold
                    zorder=2)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['display_label'], fontsize=plt.rcParams['ytick.labelsize'])
    for label in ax.get_yticklabels(): # Y-axis tick labels bold
        label.set_fontweight('bold')
    
    PLOT_SPECIFIC_YTICK_LABEL_PADDING = 0.5 # From your code
    ax.tick_params(axis='y', which='major', pad=PLOT_SPECIFIC_YTICK_LABEL_PADDING, direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH)
    ax.tick_params(axis='x', which='major', direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH, pad=1.0)
    
    ax.set_xlabel(r'RR (N$_2$O)', fontweight='bold', fontsize=plt.rcParams['axes.labelsize'])
    ax.set_ylim(current_ylim_for_box_and_final_plot)

    ax.spines['left'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['left'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['bottom'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_bounds(main_plot_data_xmin, figure_content_xmax)
    ax.spines['top'].set_visible(True); ax.spines['top'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['top'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['top'].set_bounds(main_plot_data_xmin, figure_content_xmax)
    ax.spines['right'].set_visible(True); ax.spines['right'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['right'].set_linewidth(STRUCTURAL_LINE_WIDTH)


# SECTION 5: Function to Draw "Fertilizers and Nitrogen (Yield)" Plot (Right)
def draw_new_plot_left(ax): # This function draws the Yield plot
    ax.set_facecolor('white')
    new_data_structured_plot1 = [
        {'sub_category': 'Irrigation', 'display_label': '  Irrigated ', 'N': 208, 'L1': 0.01344055752, 'L2': 0.08459489226, 'type': 'factor'},
        {'sub_category': 'Irrigation', 'display_label': '  Rainfed', 'N': 199, 'L1': -0.05605577626, 'L2': 0.06873342949, 'type': 'factor'},
        {'sub_category': 'Tillage', 'display_label': ' No-till ', 'N': 136, 'L1': -0.05982965813, 'L2': 0.07848814822, 'type': 'factor'},
        {'sub_category': 'Tillage', 'display_label': '  Tilled ', 'N': 93, 'L1': 0.08355716737, 'L2': 0.06853185341, 'type': 'factor'}, # L2 was different in data, using this one
        {'sub_category': 'Land Use', 'display_label': '  Lowland ', 'N': 68, 'L1': 0.1411064945, 'L2': 0.1096571241, 'type': 'factor'}, # L2 was different in data
        {'sub_category': 'Land Use', 'display_label': '  Upland', 'N': 65, 'L1': 0.01912035738, 'L2': 0.0506729008, 'type': 'factor'}, # L1 was different
        {'sub_category': 'Crop type', 'display_label': '  Cereals ', 'N': 361, 'L1': -0.04971354024, 'L2': 0.08630621089, 'type': 'factor'},
        {'sub_category': 'Crop type', 'display_label': '  Mixed ', 'N': 229, 'L1': -0.01607073554, 'L2': 0.1589930553, 'type': 'factor'},
        {'sub_category': 'Climate zones', 'display_label': '  Seasons ', 'N': 67, 'L1': -0.02003324606, 'L2': 0.2003324606, 'type': 'factor'}, # L1 was different
        {'sub_category': 'Climate zones', 'display_label': '  Climatic type ', 'N': 113, 'L1': -0.0248159777, 'L2': 0.0741612144, 'type': 'factor'}
    ]
    df = pd.DataFrame(new_data_structured_plot1)

    PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR = 'lightslategray'; PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH = 1.2; PLOT_SPECIFIC_STUDY_MARKER_SIZE = 3
    PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH = 0.6; PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR = 'white'; PLOT_SPECIFIC_ERRORBAR_ALPHA = 1.0
    PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR = 'lightblue'; PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH = 0.5; PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE = '--'
    PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE = 3.2 ### MODIFICATION ### Increased font size
    PLOT_SPECIFIC_SUBCAT_TEXT_COLOR = 'black';
    PLOT_SPECIFIC_GRID_COLOR = 'lightgray'; PLOT_SPECIFIC_GRID_LINEWIDTH = 0.4; PLOT_SPECIFIC_GRID_LINESTYLE = '-'
    PLOT_SPECIFIC_ZERO_LINE_COLOR = 'lightcoral'; PLOT_SPECIFIC_ZERO_LINE_WIDTH = 0.8; PLOT_SPECIFIC_ZERO_LINE_STYLE = '--'
    PLOT_SPECIFIC_CATEGORY_BAR_COLOR = 'dimgray' ### MODIFICATION ### Softer color
    PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH = 0.4  ### MODIFICATION ### Slightly thicker

    ax.set_title('Agriculture practices', fontweight='bold', loc='center', fontsize=plt.rcParams['axes.titlesize']) # Title from your code
    y_pos = np.arange(len(df))

    PLOT_SPECIFIC_DESIRED_XTICKS = np.array([-0.2, 0.0, 0.2,]) # From your code
    tick_step = PLOT_SPECIFIC_DESIRED_XTICKS[1] - PLOT_SPECIFIC_DESIRED_XTICKS[0] if len(PLOT_SPECIFIC_DESIRED_XTICKS) > 1 else 0.2
    main_plot_data_xmin = PLOT_SPECIFIC_DESIRED_XTICKS.min() - tick_step / 2
    main_plot_data_xmax = PLOT_SPECIFIC_DESIRED_XTICKS.max() + tick_step / 2
    
    plot_width_for_n_box = main_plot_data_xmax - main_plot_data_xmin
    box_width = plot_width_for_n_box * 0.16 # From your code
    box_start_x = main_plot_data_xmax + plot_width_for_n_box * 0.02
    numbers_text_x_center = box_start_x + (box_width / 2)
    figure_content_xmax = box_start_x + box_width

    ax.set_xlim(main_plot_data_xmin, figure_content_xmax)
    ax.set_xticks(PLOT_SPECIFIC_DESIRED_XTICKS)
    ax.set_xticklabels([f"{t:.1f}" for t in PLOT_SPECIFIC_DESIRED_XTICKS], fontsize=plt.rcParams['xtick.labelsize'])

    def format_subcategory_display_name_plot_Yield(original_sub_cat_name):
        key = original_sub_cat_name.strip() # Ensure keys are stripped for comparison
        if "Irrigation" == key: return "Irrigation" # Undisturbed
        if "Tillage" == key: return "Tillage"       # Undisturbed
        
        if "Land Use" == key: return "Land\nUse"     ### MODIFIED for multi-line
        if "Crop type" == key: return "Crop\ntype"   ### MODIFIED for multi-line
        if "Climate zones" == key: return "Climate\nzones" ### MODIFIED for multi-line
        # Add other mappings if needed from your Yield plot data/reference image
        if "Fertilizer application" == key: return "Fertilizer\napplication"
        if "Nitrogen rate" == key: return "Nitrogen\nrate"
        if "Nitrogen sources" == key: return "Nitrogen\nsources"
        if "Plant N Use" == key: return "Plant N\nUse"
        if "Plant productivity" == key: return "Plant\nproductivity"
        return key

    subcat_display_info = []
    ordered_subcategories = df['sub_category'].unique()
    for sub_cat_name_orig in ordered_subcategories:
        group_rows_indices = df[df['sub_category'] == sub_cat_name_orig].index
        if not group_rows_indices.empty:
            y_coords_for_group = y_pos[group_rows_indices]
            center_y = (np.min(y_coords_for_group) + np.max(y_coords_for_group)) / 2.0
            display_text = format_subcategory_display_name_plot_Yield(sub_cat_name_orig)
            subcat_display_info.append({'text_to_plot': display_text, 'center_y': center_y,
                                        'min_y_group': np.min(y_coords_for_group), 'max_y_group': np.max(y_coords_for_group)})

    current_sub_category_for_grouping = None
    if len(df) > 0:
        for i, row_data in df.iterrows():
            if row_data['sub_category'] != current_sub_category_for_grouping:
                if current_sub_category_for_grouping is not None and i > 0:
                    ax.hlines(y_pos[i] - 0.5, main_plot_data_xmin, main_plot_data_xmax, color=PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR, linewidth=PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH, linestyle=PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE, zorder=0.6)
                current_sub_category_for_grouping = row_data['sub_category']
            ax.hlines(y_pos[i], main_plot_data_xmin, main_plot_data_xmax, color=PLOT_SPECIFIC_GRID_COLOR, linewidth=PLOT_SPECIFIC_GRID_LINEWIDTH, linestyle=PLOT_SPECIFIC_GRID_LINESTYLE, zorder=0.5)

    PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR = -0.29 ### MODIFICATION: Anchor for CENTER of text block
    PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC = -0.25  ### MODIFICATION: Bar to the LEFT of text block

    blended_transform = transforms.blended_transform_factory(ax.transAxes, ax.transData)

    for vert_label_info in subcat_display_info:
        ax.text(PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR, vert_label_info['center_y'], vert_label_info['text_to_plot'],
                transform=blended_transform, rotation=90, 
                ha='center', va='center', ### MODIFICATION: ha='center'
                fontsize=PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE, color=PLOT_SPECIFIC_SUBCAT_TEXT_COLOR, clip_on=False, zorder=2.5)
        bar_y_start = vert_label_info['min_y_group'] - 0.3 # Adjusted extension
        bar_y_end = vert_label_info['max_y_group'] + 0.3   # Adjusted extension
        ax.plot([PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC, PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC], [bar_y_start, bar_y_end],
                color=PLOT_SPECIFIC_CATEGORY_BAR_COLOR, linewidth=PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH,
                transform=blended_transform, clip_on=False, zorder=1.0)

    for i, row_data in df.iterrows():
        ax.hlines(y=y_pos[i], xmin=row_data['L1'], xmax=row_data['L2'], color=PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR, linewidth=PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH, alpha=PLOT_SPECIFIC_ERRORBAR_ALPHA, zorder=3)
        center_x = (row_data['L1'] + row_data['L2']) / 2
        ax.plot(center_x, y_pos[i], 'D', markerfacecolor=PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR, markeredgecolor=PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR, markersize=PLOT_SPECIFIC_STUDY_MARKER_SIZE, markeredgewidth=PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH, alpha=PLOT_SPECIFIC_ERRORBAR_ALPHA, zorder=5)

    ax.axvline(0, color=PLOT_SPECIFIC_ZERO_LINE_COLOR, linewidth=PLOT_SPECIFIC_ZERO_LINE_WIDTH, linestyle=PLOT_SPECIFIC_ZERO_LINE_STYLE, ymax=1.0, zorder=2)
    
    current_ylim_for_box_and_final_plot = (-0.5, len(df) - 0.5) if len(df) > 0 else (-0.5, 0.5)
    ax.add_patch(Rectangle((box_start_x, current_ylim_for_box_and_final_plot[0]), box_width, current_ylim_for_box_and_final_plot[1] - current_ylim_for_box_and_final_plot[0], facecolor='white', edgecolor=STRUCTURAL_LINE_COLOR, linewidth=STRUCTURAL_LINE_WIDTH, clip_on=False, zorder=1))
    for i, row_data in df.iterrows():
        if pd.notna(row_data['N']):
            ax.text(numbers_text_x_center, y_pos[i], f"{int(row_data['N'])}", 
                    ha='center', va='center', 
                    fontsize=plt.rcParams['ytick.labelsize'], 
                    color='black', 
                    fontweight='bold', # N-box numbers bold
                    zorder=2)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['display_label'], fontsize=plt.rcParams['ytick.labelsize'])
    for label in ax.get_yticklabels(): # Y-axis tick labels bold
        label.set_fontweight('bold')
        
    PLOT_SPECIFIC_YTICK_LABEL_PADDING = 0.5 # From your code
    ax.tick_params(axis='y', which='major', pad=PLOT_SPECIFIC_YTICK_LABEL_PADDING, direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH)
    ax.tick_params(axis='x', which='major', direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH, pad=1.0)
    
    ax.set_xlabel(r'RR (Yield)', fontweight='bold', fontsize=plt.rcParams['axes.labelsize']) ### Ensured bold X-axis label
    ax.set_ylim(current_ylim_for_box_and_final_plot)

    ax.spines['left'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['left'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['bottom'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['bottom'].set_bounds(main_plot_data_xmin, figure_content_xmax)
    ax.spines['top'].set_visible(True); ax.spines['top'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['top'].set_linewidth(STRUCTURAL_LINE_WIDTH)
    ax.spines['top'].set_bounds(main_plot_data_xmin, figure_content_xmax)
    ax.spines['right'].set_visible(True); ax.spines['right'].set_color(STRUCTURAL_LINE_COLOR); ax.spines['right'].set_linewidth(STRUCTURAL_LINE_WIDTH)


# SECTION 6: Main Script to Create and Save Side-by-Side Plots
width_cm = 10
width_inches = width_cm / 2.54
original_height_inches = 2.7

# SUB-SECTION 6.1: Create Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width_inches, original_height_inches), dpi=600)

# Setting the FIGURE's (outside area) background color
fig.patch.set_facecolor(FIGURE_OUTSIDE_COLOR)
fig.patch.set_alpha(1.0)

# SUB-SECTION 6.2: Draw the Plots (N2O on left, Yield on right)
draw_new_plot_right(ax1)
draw_new_plot_left(ax2)

# SUB-SECTION 6.3: Adjust Layout
fig.subplots_adjust(
    left=0.28,   ### MODIFIED for new label anchors
    right=0.95,  ### MODIFIED for balance
    bottom=0.15,
    top=0.92,
    wspace=0.50  ### MODIFIED for space between plots for right plot's labels
)

# SUB-SECTION 6.4: Save and Show Plot
# custom_directory 


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
    custom_directory = "."
    print(f"Figures will be saved to the current directory: {os.path.abspath(custom_directory)}")
    print(f"--------------------------------------------------------------------")

full_path_png = os.path.join(custom_directory, base_filename_for_save + ".png")
full_path_tiff = os.path.join(custom_directory, base_filename_for_save + ".tiff")
figure_actual_facecolor_for_saving = fig.get_facecolor()

try:
    plt.savefig(full_path_png, dpi=600, bbox_inches='tight', facecolor=figure_actual_facecolor_for_saving, transparent=False)
    print(f"Figure saved as PNG: {full_path_png}")
except Exception as e:
    print(f"Error saving PNG to {full_path_png}: {e}")
try:
    plt.savefig(full_path_tiff, dpi=600, bbox_inches='tight', facecolor=figure_actual_facecolor_for_saving, transparent=False)
    print(f"Figure saved as TIFF: {full_path_tiff}")
except Exception as e:
    print(f"Error saving TIFF to {full_path_tiff}: {e}")

plt.show()
