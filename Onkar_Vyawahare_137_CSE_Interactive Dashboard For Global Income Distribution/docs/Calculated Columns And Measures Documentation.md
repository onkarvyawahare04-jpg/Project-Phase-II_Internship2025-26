* #### **Country\_Name**



* ###### **Calculated Columns**



&nbsp;   **1.Country\_Continent**

&nbsp;     

&nbsp;     In dataset, each country belongs to one continent, which helps group and compare economic indicators like GDP and unemployment at a regional level.

&nbsp;   

* ###### **Calculated Measures**

&nbsp;   

&nbsp;   **1.Total\_Countries**



&nbsp;     The Total\_Countries measure calculates the total number of unique countries in your dataset. 

&nbsp;    

&nbsp;   **2.Country\_Strength\_Score**



&nbsp;     The Country\_Strength\_Score measure represents a combined performance score of a country based on multiple economic indicators such as GDP, unemployment rate, income gap.





* #### **Year**



* ###### **Calculated Columns**



&nbsp;   **1.Year\_Group**



&nbsp;     The Year\_Group column is used to categorize years into specific ranges or groups





* #### **GDP\_Per\_Capita ($)**



* ###### **Calculated Columns**



&nbsp;  **1.GDP\_Per\_Capita\_Category**



&nbsp;   The GDP\_Per\_Capita\_Category column groups countries into income levels based on their GDP per capita value.



* ###### **Calculated Measures**



&nbsp;  **1.GDP\_YoY\_Change %**



&nbsp;    The GDP\_YoY\_Change % measure shows the Year-over-Year percentage change in GDP.



&nbsp;  **2.Region\_Total\_GD**P



&nbsp;    The Region\_Total\_GDP measure calculates the total GDP for all countries within the same continent (region).



&nbsp;  **3.Region\_GDP\_%\_Contribution**



&nbsp;    The Region\_GDP\_%\_Contribution measure shows the percentage share of a region’s GDP compared to the total global GDP in the dataset.

&nbsp;    



* #### **Gini\_Index (0-100)**



* ###### **Calculated Columns**



&nbsp;  **1.Gini\_Inequality\_Level**



&nbsp;    The Gini\_Inequality\_Level column categorizes countries based on their Gini Index value, which measures income inequality within a country.



* ###### **Calculated Measures**



&nbsp;  **1.Gini\_Inequality\_Severity\_Score**



&nbsp;    The Gini\_Inequality\_Severity\_Score measure represents a calculated score based on the Gini Index to indicate the intensity of income inequality in a country.



&nbsp;  **2.Gini\_YoY\_Change**



&nbsp;    The Gini\_YoY\_Change measure calculates the Year-over-Year change in the Gini Index for a country.





* #### **Income\_Share (%)**



* ###### **Calculated Columns**

&nbsp;

&nbsp;  **1.Income\_Share\_Gap**



&nbsp;    The Income\_Share\_Gap column represents the difference between the income share of the highest 20% and the lowest 20% of the population.



&nbsp;  **2.Middle\_Class\_Income\_Share**



&nbsp;    The Middle\_Class\_Income\_Share column represents the combined income share of the middle 60% of the population (second, third, and fourth 20% income groups).



* ###### **Calculated Measures**



&nbsp;  **1.Income\_Polarization\_Index**



&nbsp;    The Income\_Polarization\_Index measure calculates the difference between the income share of the highest 20% and the lowest 20% of the population.





* #### **Unemployement\_Rate (%)**



* ###### **Calculated Columns**



&nbsp;  **1. Unemployment\_Level**



&nbsp;     The Unemployment\_Level column categorizes countries based on their unemployment rate into groups such as



* ###### **Calculated Measures**



&nbsp;  **1.Unemployment\_YoY\_Change**



&nbsp;    The Unemployment\_YoY\_Change measure calculates the Year-over-Year change in the unemployment rate for a country.



&nbsp;  **2.Unemployment\_Rank**



&nbsp;    The Unemployment\_Rank measure ranks countries based on their average unemployment rate using the RANKX() function.



&nbsp;  **3.Unemployement\_Region\_Average**

&nbsp; 

&nbsp;    The Unemployement\_Region\_Average measure calculates the average unemployment rate of all countries within the same continent (region).



&nbsp;    



&nbsp;    

&nbsp;    

&nbsp;  

&nbsp;    

&nbsp;    

