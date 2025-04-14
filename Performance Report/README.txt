Performance Dashboard – Power BI
________________


  At-a-Glance
This is a business intelligence project focused on tracking gross profit trends across products, geographies, and time periods for a plant-based company. The dashboard supports financial and strategic decision-making by highlighting year-to-date (YTD) performance, comparing it with the previous year (PYTD), and analyzing gross profit contribution by country, product type, and account segmentation.
Built entirely in Power BI, the report offers interactive charts and dynamic KPIs, giving stakeholders a clear, real-time view of profitability and growth drivers.
________________


Solution
1. Data Modeling & Preparation
* Structured data using separate YTD, PYTD, and Base Measures (Gross Profit, Quantity, Sales) tables.

* Integrated dimensional fields such as Date, Country, and Product_Type for slicing and dicing.

* Created custom switching logic (SWITCH measures) to allow dynamic toggling between metrics.

________________


2. Metric Logic & DAX Measures
   * Developed DAX measures for:

      * YTD and PYTD values for Gross Profit, Quantity, and Sales.

      * GP% (Gross Profit Margin %).

      * YTD vs PYTD delta calculation with conditional formatting (color-coded increase/decrease).

         * Time intelligence functions used for month-over-month and year-over-year comparisons.

________________


3. KPI Cards & Summary Metrics
            * KPIs include:

               * YTD Gross Profit: 1.40M

               * PYTD Gross Profit: 1.47M

               * YTD vs PYTD: –77.62K (highlighted red to indicate decline)

               * GP%: 39.15%

________________


4. Visual Design & Layout
                  * Created a single-page, visually compact report with the following components:

• Treemap: Bottom 10 Countries by YTD vs PYTD
                     * Identifies underperforming regions (e.g., Canada, Germany, Japan).

• Waterfall Chart: Monthly YTD vs PYTD
                        * Highlights month-wise gains and losses in gross profit.

                        * February shows a major increase; March & April display sharp declines.

• Combo Chart: Product Type Performance
                           * Clustered columns for YTD by product type (Indoor, Landscape, Outdoor).

                           * Line overlay tracks PYTD, showing comparison trends.

• Scatter Plot: GP% vs Gross Profit
                              * Segments accounts by profitability and value.

                              * Used to identify high-profit, low-volume or high-volume, low-margin accounts.

________________


5. Interactivity & Usability
                                 * Users can toggle between Gross Profit, Quantity, and Sales at the report level.

                                 * The dashboard updates dynamically based on the selected metric.

                                 * Slicers, filters, and consistent formatting enhance user experience and navigation.

________________


Recommendations
💡 Country Performance Focus
 Canada and Germany have significant negative variances. Deeper investigation into pricing, costs, or operational issues in these regions is recommended.
💡 Product Category Trends
 “Outdoor” and “Landscape” products appear to be more volatile in performance. Review marketing or seasonal demand factors affecting these categories.
💡 Account Segmentation Insights
 Use the GP% vs Gross Profit scatter plot to identify strategic accounts for retention or upsell opportunities.
💡 Monthly Planning
 Performance peaks and dips by month indicate a need for improved monthly planning, particularly heading into Q2.
________________


What I Learned
                                    * Built a financial dashboard from scratch with real-time insights and dynamic metric toggling.

                                    * Mastered time intelligence and variance analysis with DAX.

                                    * Applied data storytelling principles to guide stakeholder decisions through clear, interactive visuals.

                                    * Gained hands-on experience in building a multi-layered Power BI model optimized for executive-level reporting.