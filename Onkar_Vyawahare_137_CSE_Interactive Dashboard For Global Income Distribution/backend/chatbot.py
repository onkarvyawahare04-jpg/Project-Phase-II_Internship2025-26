import pandas as pd
import os
import re

class GIDAChatbot:
    def __init__(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        excel_path = os.path.join(base_dir, '..', 'dataset', 'Global Income Distribution Dataset.xlsx')
        
        try:
            self.df = pd.read_excel(excel_path)
            self.df.columns = [c.strip() for c in self.df.columns]
        except Exception as e:
            print(f"Chatbot Data Load Error: {e}")
            self.df = pd.DataFrame()

        self.indicators = {
            "gini index": "The Gini Index is a vital measure of income inequality. It ranges from 0 (perfect equality) to 100 (maximal inequality). In our dashboard, higher scores indicate a more significant wealth gap within a nation.",
            "gdp per capita": "GDP Per Capita measures the economic output of a nation per person. It is a primary indicator of average living standards and economic strength.",
            "unemployment rate": "This metric tracks the percentage of the labor force that is currently without work but actively seeking employment, reflecting the health of the job market.",
            "income share": "Income distribution is categorized by quintiles (20% groups). Analyzing the share of the lowest vs. highest quintiles helps identify structural wealth disparities.",
            "middle class": "The Middle Class Income Share represents the economic stability of the 'middle' segments of society. A robust middle class is often linked to sustainable economic growth.",
            "regional comparison": "Our analytics allow you to compare continents (e.g., Africa vs. Europe) to understand how geographic factors influence income distribution and GDP.",
            "trend analysis": "The trend section tracks how metrics like GDP and Gini have evolved from 2000 to 2024, revealing the long-term trajectory of global development."
        }

    def get_response(self, query):
        query = query.lower().strip()

        # 1. Professional Redirect for Unrelated Topics
        if any(word in query for word in ["weather", "joke", "movie", "game", "recipe", "sport"]):
            return "I am the GIDA Economic Analytics Assistant. I specialize in global economic data and inequality insights. Please feel free to ask about GDP, Gini Index, or dashboard navigation."

        # 2. Indicators & Definitions
        for indicator, definition in self.indicators.items():
            if indicator in query:
                return f"<b>{indicator.title()}</b>: {definition}"

        # 3. Dashboard Guidance
        if "how to" in query or "help" in query or "navigation" in query or "filter" in query:
            return ("To use the dashboard effectively: <br>1. Use the <b>Slicers</b> at the top to filter by Year, Continent, or Country.<br>"
                    "2. Monitor the <b>KPI Cards</b> for immediate economic snapshots.<br>"
                    "3. Explore the <b>Interactive Map</b> for geographic trends.<br>"
                    "4. Use the <b>Action Hub</b> to switch between Comparative Analysis, FAQ, and the Analytics Guide.")

        # 4. Comparisons & Data Retrieval
        years = re.findall(r'\b(20\d{2})\b', query)
        found_countries = []
        if not self.df.empty:
            all_countries = self.df['Country_Name'].unique()
            # Sort countries by length descending to catch "South Africa" before "Africa" if it were a country
            for c in sorted(all_countries, key=len, reverse=True):
                if c.lower() in query:
                    if c not in found_countries:
                        found_countries.append(c)

        # A. Multi-Country Comparison (Same Year or Different Years)
        if len(found_countries) >= 2:
            y1 = int(years[0]) if len(years) >= 1 else 2024
            y2 = int(years[1]) if len(years) >= 2 else y1
            
            c1, c2 = found_countries[0], found_countries[1]
            row1 = self.df[(self.df['Country_Name'] == c1) & (self.df['year'] == y1)]
            row2 = self.df[(self.df['Country_Name'] == c2) & (self.df['year'] == y2)]
            
            if not row1.empty and not row2.empty:
                d1, d2 = row1.iloc[0], row2.iloc[0]
                return (f"<b>Comparative Analysis:</b><br><br>"
                        f"<b>{c1} ({y1})</b> vs <b>{c2} ({y2})</b><br>"
                        f"• GDP Per Capita: <b>${d1['GDP_Per_Capita ($)']:,.0f}</b> vs <b>${d2['GDP_Per_Capita ($)']:,.0f}</b><br>"
                        f"• Gini Index: <b>{d1['Gini_Index (0-100)']}</b> vs <b>{d2['Gini_Index (0-100)']}</b><br>"
                        f"• Unemployment: <b>{d1['Unemployement_Rate (%)']}%</b> vs <b>{d2['Unemployement_Rate (%)']}%</b><br><br>"
                        f"<i>Observation: {c1 if d1['GDP_Per_Capita ($)'] > d2['GDP_Per_Capita ($)'] else c2} has a higher GDP, "
                        f"while {c1 if d1['Gini_Index (0-100)'] > d2['Gini_Index (0-100)'] else c2} shows higher income inequality.</i>")

        # B. Single Country, Multi-Year Comparison (Progress Analysis)
        if len(found_countries) == 1 and len(years) >= 2:
            c = found_countries[0]
            y1, y2 = int(years[0]), int(years[1])
            row1 = self.df[(self.df['Country_Name'] == c) & (self.df['year'] == y1)]
            row2 = self.df[(self.df['Country_Name'] == c) & (self.df['year'] == y2)]
            
            if not row1.empty and not row2.empty:
                d1, d2 = row1.iloc[0], row2.iloc[0]
                gdp_diff = ((d2['GDP_Per_Capita ($)'] - d1['GDP_Per_Capita ($)']) / d1['GDP_Per_Capita ($)'] * 100)
                gini_diff = d2['Gini_Index (0-100)'] - d1['Gini_Index (0-100)']
                return (f"<b>Progress Analysis for {c}:</b><br><br>"
                        f"From <b>{y1}</b> to <b>{y2}</b>:<br>"
                        f"• GDP Change: <b>{gdp_diff:+.1f}%</b> (${d1['GDP_Per_Capita ($)']:,.0f} → ${d2['GDP_Per_Capita ($)']:,.0f})<br>"
                        f"• Gini Shift: <b>{gini_diff:+.1f} pts</b> ({d1['Gini_Index (0-100)']} → {d2['Gini_Index (0-100)']})<br>"
                        f"• Unemployment: <b>{d1['Unemployement_Rate (%)']}%</b> → <b>{d2['Unemployement_Rate (%)']}%</b>")

        # C. Single Country, Single Year (Deep Dive)
        if len(found_countries) == 1 and len(years) == 1:
            country, year = found_countries[0], int(years[0])
            row = self.df[(self.df['Country_Name'] == country) & (self.df['year'] == year)]
            if not row.empty:
                data = row.iloc[0]
                return (f"<b>Analytical Deep-Dive: {country} ({year})</b><br>"
                        f"• Economic Strength (GDP): <b>${data['GDP_Per_Capita ($)']:,.2f}</b><br>"
                        f"• Inequality Level (Gini): <b>{data['Gini_Index (0-100)']}</b> ({data['Gini_Inequality_Level']})<br>"
                        f"• Labor Market (Unemployment): <b>{data['Unemployement_Rate (%)']}%</b> ({data['Unemployment_Level']})")

        # 5. Targeted Extremes (Highest/Lowest Logic)
        is_highest = "highest" in query or "most" in query or "top" in query or "richest" in query
        is_lowest = "lowest" in query or "least" in query or "bottom" in query or "poorest" in query
        
        if is_highest or is_lowest:
            # Map user terms to columns
            col = None
            label = ""
            if "gdp" in query: 
                col = 'GDP_Per_Capita ($)'
                label = "GDP Per Capita"
            elif "gini" in query or "inequality" in query: 
                col = 'Gini_Index (0-100)'
                label = "Gini Index"
            elif "unemployment" in query: 
                col = 'Unemployement_Rate (%)%'
                label = "Unemployment Rate"
                # Fix for column name in dataset
                if 'Unemployement_Rate (%)' in self.df.columns:
                    col = 'Unemployement_Rate (%)'
            elif "income share" in query or "wealth" in query:
                col = 'Income Share_Highest 20%' if is_highest else 'Income Share_Lowest 20%'
                label = "Income Share"

            if col:
                # Scenario A: Metric + Year (Global extreme for that year)
                if years and not found_countries:
                    y = int(years[0])
                    year_df = self.df[self.df['year'] == y]
                    if not year_df.empty:
                        idx = year_df[col].idxmax() if is_highest else year_df[col].idxmin()
                        row = year_df.loc[idx]
                        val = row[col]
                        formatted_val = f"${val:,.2f}" if "GDP" in label else f"{val}%" if "Unemployment" in label else f"{val}"
                        return (f"In <b>{y}</b>, the <b>{label}</b> was <b>{ 'highest' if is_highest else 'lowest' }</b> in "
                                f"<b>{row['Country_Name']}</b> with a value of <b>{formatted_val}</b>.")

                # Scenario B: Metric + Country (Historical extreme for that country)
                if found_countries:
                    c = found_countries[0]
                    country_df = self.df[self.df['Country_Name'] == c]
                    if not country_df.empty:
                        idx = country_df[col].idxmax() if is_highest else country_df[col].idxmin()
                        row = country_df.loc[idx]
                        val = row[col]
                        formatted_val = f"${val:,.2f}" if "GDP" in label else f"{val}%" if "Unemployment" in label else f"{val}"
                        return (f"The <b>{ 'highest' if is_highest else 'lowest' }</b> {label} for <b>{c}</b> was recorded in "
                                f"<b>{row['year']}</b> with a value of <b>{formatted_val}</b>.")

        # 6. General Rankings & Insights (Legacy Fallbacks)
        if "highest gini" in query or "most unequal" in query or "ranking" in query:
            idx = self.df['Gini_Index (0-100)'].idxmax()
            row = self.df.loc[idx]
            return (f"The <b>{row['Country_Name']}</b> recorded the highest Gini Index of <b>{row['Gini_Index (0-100)']}</b> in {row['year']}, "
                    "signaling extreme income disparity.")

        if "highest gdp" in query or "richest" in query:
            idx = self.df['GDP_Per_Capita ($)'].idxmax()
            row = self.df.loc[idx]
            return f"The highest GDP Per Capita in our dataset is <b>${row['GDP_Per_Capita ($)']:,.2f}</b>, recorded by <b>{row['Country_Name']}</b> in {row['year']}."

        if "summary" in query or "overview" in query or "trend" in query:
            return (f"Currently, I am tracking <b>{len(self.df['Country_Name'].unique())} countries</b>. "
                    "Global trends show that while GDP has grown on average, income inequality (Gini) remains a structural challenge in several regions. "
                    "You can view these longitudinal shifts in the 'Trend Analysis' section of the dashboard.")

        # 7. Fallback (Professional Persona)
        return ("Greetings. I am your AI Economic Analytics Assistant. I can provide professional insights on:<br>"
                "• <b>Economic Indicators</b> (GDP, Gini, Unemployment)<br>"
                "• <b>Country & Regional Comparisons</b><br>"
                "• <b>Targeted Extremes</b> (e.g., 'Highest GDP in 2010' or 'Lowest Gini of USA')<br>"
                "• <b>Dashboard Guidance</b><br><br>"
                "How may I assist your analysis today?")

# Singleton instance
chatbot = GIDAChatbot()
