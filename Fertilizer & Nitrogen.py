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
    'ytick.labelsize': 2.5,
    'figure.facecolor': 'none',
    'axes.facecolor': 'white',
    'savefig.transparent': False
})

# SECTION 3: Define Consistent Colors and Styles for Plots
STRUCTURAL_LINE_COLOR = 'dimgray'
STRUCTURAL_LINE_WIDTH = 0.5
FIGURE_OUTSIDE_COLOR = '#EAF6FF' # Light blue for area around plots

# SECTION 4: Function to Draw "Fertilizers and Nitrogen (N2O)" Plot (Left)
def draw_new_plot_right(ax): # This function draws the N2O plot
 
    ax.set_facecolor('white') # Now draw the plot's actual white background ON TOP
    # ... rest of your existing function code continues here ...

    ax.set_facecolor('white') # Original first line of function
    new_data_structured_plot2 = [ # Original data definition
# ... rest of the draw_new_plot_right function ...
        
        {'sub_category': 'Fertilizer appplication ', 'display_label': '  Banded ', 'N': 104, 'L1': -0.5804269471, 'L2': -0.3169457012, 'type': 'factor'},
        {'sub_category': 'Fertilizer appplication ', 'display_label': '  Broadcasted ', 'N': 92, 'L1': -0.4367765699, 'L2': -0.09899569337,  'type': 'factor'},
        {'sub_category': 'Fertilizer appplication ', 'display_label': '  Mixed ', 'N': 59, 'L1': -0.6871755627, 'L2': -0.4164115893,  'type': 'factor'},

        {'sub_category': 'Nitrogen rate ', 'display_label': '  <150 (kg/ha) ',   'N': 141, 'L1': -1.012067627,  'L2': -0.5479462823, 'type': 'factor'},
        {'sub_category': 'Nitrogen rate ', 'display_label': ' 150-300 (kg/ha)  ','N': 225, 'L1': -0.7679696165,  'L2': -0.3590656211, 'type': 'factor'},
        {'sub_category': 'Nitrogen rate ', 'display_label': ' >300 (kg/ha)  ','N': 288, 'L1': -0.8654736857,  'L2': -0.6267189318, 'type': 'factor'},

        {'sub_category': 'Nitrogen sources ', 'display_label': '   Inorganic  ', 'N': 902,  'L1': -0.568657625,  'L2': -0.3370258923, 'type': 'factor'},
        {'sub_category': 'Nitrogen sources ', 'display_label': '  Organic  ', 'N': 829,  'L1': -0.6128879438,  'L2': -0.3766170626, 'type': 'factor'},
    
        
        {'sub_category': 'Nitrogen content ', 'display_label': '  <5 (g/kg)  ',   'N': 36, 'L1': -1.55914528, 'L2': -0.692562991, 'type': 'factor'},
        {'sub_category': 'Nitrogen content ', 'display_label': '  >5 (g/kg)  ', 'N': 97, 'L1': -0.9081474673, 'L2': -0.6276155227, 'type': 'factor'},

        {'sub_category': 'Nitrogen amount ', 'display_label': '  <160  ',    'N': 20, 'L1': -0.9497151274, 'L2': -0.3832229594, 'type': 'factor'},
        {'sub_category': 'Nitrogen amount ', 'display_label': ' 160-320 ','N': 15,  'L1': -0.7233567135, 'L2': -0.3691098219, 'type': 'factor'},
        {'sub_category': 'Nitrogen amount ', 'display_label': '  ≥320 ','N': 27,  'L1': -0.5388976425, 'L2': -0.2664556678, 'type': 'factor'},
  
         
    ]
    df = pd.DataFrame(new_data_structured_plot2)

    # Plot specific styling constants
    PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR = 'lightslategray'; PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH = 1.2; PLOT_SPECIFIC_STUDY_MARKER_SIZE = 3
    PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH = 0.6; PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR = 'white'; PLOT_SPECIFIC_ERRORBAR_ALPHA = 1.0
    PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR = 'lightblue'; PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH = 0.5; PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE = '--'
    PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE = 3
    PLOT_SPECIFIC_SUBCAT_TEXT_COLOR = 'black';
    PLOT_SPECIFIC_GRID_COLOR = 'lightgray'; PLOT_SPECIFIC_GRID_LINEWIDTH = 0.4; PLOT_SPECIFIC_GRID_LINESTYLE = '-'
    PLOT_SPECIFIC_ZERO_LINE_COLOR = 'lightcoral'; PLOT_SPECIFIC_ZERO_LINE_WIDTH = 0.8; PLOT_SPECIFIC_ZERO_LINE_STYLE = '--'
    PLOT_SPECIFIC_CATEGORY_BAR_COLOR = 'black'; PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH = 0.3

    ax.set_title('Fertilizers and Nitrogen ', fontweight='bold', loc='center', fontsize=plt.rcParams['axes.titlesize'])
    y_pos = np.arange(len(df))

    PLOT_SPECIFIC_DESIRED_XTICKS = np.array([-1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2])
    tick_step = PLOT_SPECIFIC_DESIRED_XTICKS[1] - PLOT_SPECIFIC_DESIRED_XTICKS[0] if len(PLOT_SPECIFIC_DESIRED_XTICKS) > 1 else 0.2
    main_plot_data_xmin = PLOT_SPECIFIC_DESIRED_XTICKS.min() - tick_step / 2
    main_plot_data_xmax = PLOT_SPECIFIC_DESIRED_XTICKS.max() + tick_step / 2
    
    plot_width_for_n_box = main_plot_data_xmax - main_plot_data_xmin
    box_width = plot_width_for_n_box * 0.13
    box_start_x = main_plot_data_xmax + plot_width_for_n_box * 0.02
    numbers_text_x_center = box_start_x + (box_width / 2)
    figure_content_xmax = box_start_x + box_width

    ax.set_xlim(main_plot_data_xmin, figure_content_xmax)
    ax.set_xticks(PLOT_SPECIFIC_DESIRED_XTICKS)
    ax.set_xticklabels([f"{t:.1f}" for t in PLOT_SPECIFIC_DESIRED_XTICKS], fontsize=plt.rcParams['xtick.labelsize'])

# ... (inside draw_new_plot_right(ax))
    def format_subcategory_display_name_plot_N2O(original_sub_cat_name):
        # Trim whitespace from the key first for reliable matching
        key = original_sub_cat_name.strip()
        if "Climate zone" == key: return "Climate\nzone"
        if "Crop type" == key: return "Crop\ntype"
        if "Land Use" == key: return "Land\nUse"
        if "Irrigation" == key: return "Irrigation" # Can stay single line or "Irri-\ngation"
        if "Tillage" == key: return "Tillage"       # Can stay single line
        if "Climatic factors" == key: return "Climatic\nfactors"
        if "Fertilizer appplication" == key: return "Fertilizer\napplication" # Corrected original key
        if "Nitrogen rate" == key: return "Nitrogen\nrate"
        if "Nitrogen sources" == key: return "Nitrogen\nsources"
        if "Nitrogen content" == key: return "Nitrogen\ncontent"
        if "Nitrogen amount" == key: return "Nitrogen\namount"
        return key # Return the stripped key if no specific format is found

    subcat_display_info = []
    ordered_subcategories = df['sub_category'].unique()
    for sub_cat_name_orig in ordered_subcategories:
        group_rows_indices = df[df['sub_category'] == sub_cat_name_orig].index
        if not group_rows_indices.empty:
            y_coords_for_group = y_pos[group_rows_indices]
            center_y = (np.min(y_coords_for_group) + np.max(y_coords_for_group)) / 2.0
            display_text = format_subcategory_display_name_plot_N2O(sub_cat_name_orig) # Using renamed function
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
    
    PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR = -0.40
    PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC = -0.35

    blended_transform = transforms.blended_transform_factory(ax.transAxes, ax.transData)

    for vert_label_info in subcat_display_info:
        ax.text(PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR, vert_label_info['center_y'], vert_label_info['text_to_plot'],
                transform=blended_transform, rotation=90, ha='center', va='center',
                fontsize=PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE, color=PLOT_SPECIFIC_SUBCAT_TEXT_COLOR, clip_on=False, zorder=2.5)
        bar_y_start = vert_label_info['min_y_group'] - 0.35
        bar_y_end = vert_label_info['max_y_group'] + 0.35
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
                    fontweight='bold', # BOLD N-BOX NUMBERS ###
                    zorder=2)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['display_label'], fontsize=plt.rcParams['ytick.labelsize'])
     ### BOLD Y-AXIS TICK LABELS ###
    for label in ax.get_yticklabels():
        label.set_fontweight('bold')
    
    PLOT_SPECIFIC_YTICK_LABEL_PADDING = 0.5
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

    ax.set_facecolor('white') # Original first line of function
    new_data_structured_plot1 = [ # Original data definition
# ... rest of the draw_new_plot_left function ...
        {'sub_category': 'Fertilizer application', 'display_label': '  Banded ', 'N': 73, 'L1': -0.09718693736, 'L2': 0.07732096084, 'type': 'factor'},
        {'sub_category': 'Fertilizer application', 'display_label': '  Broadcasted', 'N': 59, 'L1': -0.1165786161, 'L2': 0.07433323159, 'type': 'factor'},
        {'sub_category': 'Fertilizer application', 'display_label': '  Mixed', 'N': 36, 'L1': -0.05706561183, 'L2': 0.1514443346, 'type': 'factor'},
        
        {'sub_category': 'Nitrogen rate', 'display_label': '  <150 (kg/ha) ', 'N': 233, 'L1': -0.02197634361, 'L2': 0.08868929665, 'type': 'factor'},
        {'sub_category': 'Nitrogen rate', 'display_label': '  150-300 (kg/ha) ', 'N': 203, 'L1': -0.02222334265, 'L2': 0.144114968, 'type': 'factor'},
        {'sub_category': 'Nitrogen rate', 'display_label': '  >300 (kg/ha) ', 'N': 137, 'L1': 0.005605124497, 'L2': 0.1557207564, 'type': 'factor'},

        
        {'sub_category': 'Nitrogen sources', 'display_label': '  Inorganic ', 'N': 202, 'L1': -0.01431454826, 'L2': 0.1169320448, 'type': 'factor'},
        {'sub_category': 'Nitrogen sources', 'display_label': '  Mixed ', 'N': 91, 'L1': -0.01336070902, 'L2': 0.1400699129, 'type': 'factor'},
        
        {'sub_category': 'Plant N Use', 'display_label': '  Grain N-content', 'N': 110, 'L1': -0.0427423232, 'L2': 0.1553517976, 'type': 'factor'},
        {'sub_category': 'Plant N Use', 'display_label': '  Plant N uptake', 'N': 321, 'L1': -0.07574069329, 'L2': 0.09198252316, 'type': 'factor'},

        
        {'sub_category': 'Plant productivity', 'display_label': ' Yield ', 'N': 588, 'L1': -0.06271154356, 'L2': 0.0677969872, 'type': 'factor'},
        {'sub_category': 'Plant productivity', 'display_label': '  Biomass ', 'N': 376, 'L1': -0.1893757429, 'L2': 0.09215045249, 'type': 'factor'},
    ]
    df = pd.DataFrame(new_data_structured_plot1)

    # Plot specific styling constants
    PLOT_SPECIFIC_STUDY_ERRORBAR_COLOR = 'lightslategray'; PLOT_SPECIFIC_STUDY_ERRORBAR_LINEWIDTH = 1.2; PLOT_SPECIFIC_STUDY_MARKER_SIZE = 3
    PLOT_SPECIFIC_STUDY_MARKER_EDGEWIDTH = 0.6; PLOT_SPECIFIC_STUDY_MARKER_FACECOLOR = 'white'; PLOT_SPECIFIC_ERRORBAR_ALPHA = 1.0
    PLOT_SPECIFIC_SUBCAT_DIVIDER_COLOR = 'lightblue'; PLOT_SPECIFIC_SUBCAT_DIVIDER_LINEWIDTH = 0.5; PLOT_SPECIFIC_SUBCAT_DIVIDER_STYLE = '--'
    PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE = 3
    PLOT_SPECIFIC_SUBCAT_TEXT_COLOR = 'black';
    PLOT_SPECIFIC_GRID_COLOR = 'lightgray'; PLOT_SPECIFIC_GRID_LINEWIDTH = 0.4; PLOT_SPECIFIC_GRID_LINESTYLE = '-'
    PLOT_SPECIFIC_ZERO_LINE_COLOR = 'lightcoral'; PLOT_SPECIFIC_ZERO_LINE_WIDTH = 0.8; PLOT_SPECIFIC_ZERO_LINE_STYLE = '--'
    PLOT_SPECIFIC_CATEGORY_BAR_COLOR = 'black'; PLOT_SPECIFIC_CATEGORY_BAR_LINEWIDTH = 0.3

    ax.set_title('Fertilizers and Nitrogen ', fontweight='bold', loc='center', fontsize=plt.rcParams['axes.titlesize'])
    y_pos = np.arange(len(df))

    PLOT_SPECIFIC_DESIRED_XTICKS = np.array([-0.2, 0.0, 0.2,])
    tick_step = PLOT_SPECIFIC_DESIRED_XTICKS[1] - PLOT_SPECIFIC_DESIRED_XTICKS[0] if len(PLOT_SPECIFIC_DESIRED_XTICKS) > 1 else 0.2
    main_plot_data_xmin = PLOT_SPECIFIC_DESIRED_XTICKS.min() - tick_step / 2
    main_plot_data_xmax = PLOT_SPECIFIC_DESIRED_XTICKS.max() + tick_step / 2
    
    plot_width_for_n_box = main_plot_data_xmax - main_plot_data_xmin
    box_width = plot_width_for_n_box * 0.13
    box_start_x = main_plot_data_xmax + plot_width_for_n_box * 0.02
    numbers_text_x_center = box_start_x + (box_width / 2)
    figure_content_xmax = box_start_x + box_width

    ax.set_xlim(main_plot_data_xmin, figure_content_xmax)
    ax.set_xticks(PLOT_SPECIFIC_DESIRED_XTICKS)
    ax.set_xticklabels([f"{t:.1f}" for t in PLOT_SPECIFIC_DESIRED_XTICKS], fontsize=plt.rcParams['xtick.labelsize'])

# ... (inside draw_new_plot_left(ax))
    def format_subcategory_display_name_plot_Yield(original_sub_cat_name):
        if "Fertilizer application" == original_sub_cat_name: return "Fertilizer\napplication"
        if "Nitrogen rate" == original_sub_cat_name: return "Nitrogen\nrate"
        if "Nitrogen sources" == original_sub_cat_name: return "Nitrogen\nsources"
        if "Plant N Use" == original_sub_cat_name: return "Plant N\nUse" # Or "Plant\nN Use"
        if "Plant productivity" == original_sub_cat_name: return "Plant\nproductivity"
        return original_sub_cat_name

    subcat_display_info = []
    ordered_subcategories = df['sub_category'].unique()
    for sub_cat_name_orig in ordered_subcategories:
        group_rows_indices = df[df['sub_category'] == sub_cat_name_orig].index
        if not group_rows_indices.empty:
            y_coords_for_group = y_pos[group_rows_indices]
            center_y = (np.min(y_coords_for_group) + np.max(y_coords_for_group)) / 2.0
            display_text = format_subcategory_display_name_plot_Yield(sub_cat_name_orig) # Using renamed function
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

    PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR = -0.38
    PLOT_SPECIFIC_BAR_X_COORD_AXES_FRAC = -0.33

    blended_transform = transforms.blended_transform_factory(ax.transAxes, ax.transData)

    for vert_label_info in subcat_display_info:
        ax.text(PLOT_SPECIFIC_SUBCAT_LABELS_X_ANCHOR, vert_label_info['center_y'], vert_label_info['text_to_plot'],
                transform=blended_transform, rotation=90, ha='center', va='center',
                fontsize=PLOT_SPECIFIC_SUBCAT_TEXT_FONTSIZE, color=PLOT_SPECIFIC_SUBCAT_TEXT_COLOR, clip_on=False, zorder=2.5)
        bar_y_start = vert_label_info['min_y_group'] - 0.35
        bar_y_end = vert_label_info['max_y_group'] + 0.35
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
                    fontweight='bold', ### BOLD N-BOX NUMBERS ###
                    zorder=2)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['display_label'], fontsize=plt.rcParams['ytick.labelsize'])
    ### BOLD Y-AXIS TICK LABELS ###
    for label in ax.get_yticklabels():
        label.set_fontweight('bold')
    
    PLOT_SPECIFIC_YTICK_LABEL_PADDING = 0.5
    ax.tick_params(axis='y', which='major', pad=PLOT_SPECIFIC_YTICK_LABEL_PADDING, direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH)
    ax.tick_params(axis='x', which='major', direction='out', length=1.5, width=STRUCTURAL_LINE_WIDTH, pad=1.0)
    
    ax.set_xlabel(r'RR (Yield)', fontweight='bold', fontsize=plt.rcParams['axes.labelsize'])
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

# SUB-SECTION 6.2: Draw the Plots (Order Swapped: N2O on left, Yield on right)
draw_new_plot_right(ax1) # This function draws the N2O plot, now on ax1 (left)
draw_new_plot_left(ax2)  # This function draws the Yield plot, now on ax2 (right)

# SUB-SECTION 6.3: Adjust Layout
# <<< POINT 3 MODIFICATION WILL HAPPEN HERE (Titles closer to plots) >>>
# We will adjust 'top' and potentially 'hspace' if there were multiple rows.
# For titles, adjusting 'top' moves the top edge of subplots down from figure top.
# And we can adjust title position itself using ax.set_title(..., y=...)
fig.subplots_adjust(
    left=0.28,
    right=0.97,
    bottom=0.15, # Increased bottom margin slightly for x-labels
    top=0.92,    # Reduced top margin to bring titles potentially closer
    wspace=0.60
)

# SUB-SECTION 6.4: Save and Show Plot

# 1. Define the directory part of your custom path
# Based on your provided path: 
# custom_directory 

# 2. Define your base filename (the part without the folder path or .png/.tiff)
base_filename_for_save = "Fertilizers and N related"

# 3. Create the custom directory if it doesn't exist
#    This is crucial for savefig to work with a nested path.
try:
    if not os.path.exists(custom_directory):
        os.makedirs(custom_directory) # This creates all necessary parent folders
        print(f"Successfully created directory: {custom_directory}")
    else:
        print(f"Directory already exists: {custom_directory}")
except Exception as e:
    print(f"--------------------------------------------------------------------")
    print(f"ERROR: Could not create or access directory: {custom_directory}")
    print(f"Error details: {e}")
    print(f"Please ensure the path is correct (check for typos like 'Reseacher') and you have write permissions.")
    print(f"Attempting to save files to the current script directory instead.")
    print(f"--------------------------------------------------------------------")
    custom_directory = "." # Fallback: current directory

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
