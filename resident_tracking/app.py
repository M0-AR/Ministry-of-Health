import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

# Configure Streamlit for deployment
st.set_page_config(
    page_title="نظام متابعة الأطباء المقيمين",
    page_icon="👨‍⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for RTL support and styling
st.markdown("""
<style>
    body {
        direction: rtl;
    }
    .stButton button {
        width: 100%;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        text-align: right;
    }
    .stTextInput input {
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# Sample data
@st.cache_data
def load_sample_data():
    data = {
        'ID': [str(i) for i in range(1, 16)],
        'Name': [
            'أحمد محمد', 'سارة خالد', 'محمد علي', 'نور حسين', 'ليلى عمر',
            'عمر خالد', 'رنا سامي', 'سامي حسن', 'دانا وليد', 'كريم محمود',
            'لينا سعيد', 'طارق نبيل', 'ريم عادل', 'باسل فادي', 'هدى منير'
        ],
        'Specialty': [
            'جراحة عامة', 'أمراض داخلية', 'أطفال', 'نسائية وتوليد', 'عينية',
            'جراحة عظمية', 'أذن أنف حنجرة', 'جراحة عامة', 'أمراض داخلية', 'قلبية',
            'عصبية', 'جراحة عامة', 'نسائية وتوليد', 'جراحة عظمية', 'أطفال'
        ],
        'Hospital': [
            'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى الأطفال', 'مشفى التوليد الجامعي', 'مشفى العيون',
            'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى الأسد الجامعي', 'مشفى المجتهد', 'مشفى القلب الجراحي',
            'مشفى المواساة الجامعي', 'مشفى الأسد الجامعي', 'مشفى التوليد الجامعي', 'مشفى المجتهد', 'مشفى الأطفال'
        ],
        'Start_Date': [
            datetime(2023, 1, 1), datetime(2023, 2, 15), datetime(2023, 3, 10), datetime(2023, 4, 1), datetime(2023, 5, 1),
            datetime(2023, 6, 1), datetime(2023, 7, 15), datetime(2023, 8, 1), datetime(2023, 9, 1), datetime(2023, 10, 1),
            datetime(2023, 11, 1), datetime(2023, 12, 1), datetime(2024, 1, 1), datetime(2024, 2, 1), datetime(2024, 3, 1)
        ],
        'End_Date': [
            datetime(2025, 1, 1), datetime(2025, 2, 15), datetime(2025, 3, 10), datetime(2025, 4, 1), datetime(2025, 5, 1),
            datetime(2025, 6, 1), datetime(2025, 7, 15), datetime(2025, 8, 1), datetime(2025, 9, 1), datetime(2025, 10, 1),
            datetime(2025, 11, 1), datetime(2025, 12, 1), datetime(2026, 1, 1), datetime(2026, 2, 1), datetime(2026, 3, 1)
        ],
        'Status': ['نشط'] * 15
    }
    df = pd.DataFrame(data)

    # Extended transfer history with more realistic scenarios
    transfers_data = {
        'Doctor_ID': [
            '1', '3', '5', '7', '2', '9', '4', '8', '10', '12',  # First set
            '1', '3', '6', '8', '2', '11', '4', '7', '9', '5',   # Second set
            '13', '14', '15', '2', '6', '8', '10', '12', '7', '4' # Third set
        ],
        'From_Hospital': [
            'مشفى المجتهد', 'مشفى الأطفال', 'مشفى العيون', 'مشفى المواساة الجامعي', 'مشفى المواساة الجامعي',
            'مشفى المجتهد', 'مشفى التوليد الجامعي', 'مشفى الأسد الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي',
            'مشفى الأسد الجامعي', 'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى الأطفال',
            'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي', 'مشفى التوليد الجامعي', 'مشفى المجتهد',
            'مشفى التوليد الجامعي', 'مشفى المجتهد', 'مشفى الأطفال', 'مشفى العيون', 'مشفى المواساة الجامعي',
            'مشفى الأسد الجامعي', 'مشفى القلب الجراحي', 'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى التوليد الجامعي'
        ],
        'To_Hospital': [
            'مشفى الأسد الجامعي', 'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي', 'مشفى الأطفال',
            'مشفى التوليد الجامعي', 'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى الأسد الجامعي', 'مشفى المجتهد',
            'مشفى المجتهد', 'مشفى الأطفال', 'مشفى الأسد الجامعي', 'مشفى المجتهد', 'مشفى المواساة الجامعي',
            'مشفى العيون', 'مشفى التوليد الجامعي', 'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي',
            'مشفى المجتهد', 'مشفى الأسد الجامعي', 'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي',
            'مشفى المواساة الجامعي', 'مشفى المجتهد', 'مشفى الأسد الجامعي', 'مشفى العيون', 'مشفى المواساة الجامعي'
        ],
        'Transfer_Date': [
            datetime(2023, 3, 1), datetime(2023, 4, 15), datetime(2023, 5, 10), datetime(2023, 6, 1), datetime(2023, 7, 1),
            datetime(2023, 8, 1), datetime(2023, 9, 15), datetime(2023, 10, 1), datetime(2023, 11, 1), datetime(2023, 12, 1),
            datetime(2024, 1, 1), datetime(2024, 2, 15), datetime(2024, 3, 10), datetime(2024, 4, 1), datetime(2024, 5, 1),
            datetime(2024, 6, 1), datetime(2024, 7, 15), datetime(2024, 8, 1), datetime(2024, 9, 1), datetime(2024, 10, 1),
            datetime(2024, 11, 1), datetime(2024, 12, 15), datetime(2025, 1, 10), datetime(2025, 2, 1), datetime(2025, 3, 1),
            datetime(2024, 4, 1), datetime(2024, 5, 15), datetime(2024, 6, 10), datetime(2024, 7, 1), datetime(2024, 8, 1)
        ],
        'Reason': [
            'حاجة القسم', 'تدريب تخصصي', 'توزيع الخبرات', 'تبادل خبرات', 'دوام تخصصي',
            'حاجة القسم', 'تدريب جراحي', 'تدريب تخصصي', 'حاجة القسم', 'توزيع الخبرات',
            'تبادل خبرات', 'دوام تخصصي', 'حاجة القسم', 'تدريب تخصصي', 'توزيع الخبرات',
            'تدريب جراحي', 'حاجة القسم', 'تبادل خبرات', 'دوام تخصصي', 'تدريب تخصصي',
            'حاجة القسم', 'تدريب جراحي', 'تبادل خبرات', 'توزيع الخبرات', 'دوام تخصصي',
            'حاجة القسم', 'تدريب تخصصي', 'تبادل خبرات', 'توزيع الخبرات', 'دوام تخصصي'
        ]
    }
    transfers_df = pd.DataFrame(transfers_data)

    hospitals_data = {
        'Name': [
            'مشفى المجتهد', 'مشفى المواساة الجامعي', 'مشفى الأطفال', 'مشفى التوليد الجامعي',
            'مشفى العيون', 'مشفى الأسد الجامعي', 'مشفى القلب الجراحي'
        ],
        'Type': ['حكومي', 'جامعي', 'تخصصي', 'جامعي', 'تخصصي', 'جامعي', 'تخصصي'],
        'Location': [
            'دمشق - المجتهد', 'دمشق - المزة', 'دمشق - المزة', 'دمشق - المزة',
            'دمشق - المجتهد', 'دمشق - المزة', 'دمشق - المزة'
        ],
        'Beds': [400, 500, 200, 150, 100, 600, 200],
        'Departments': [
            'جراحة عامة، باطنة، إسعاف، عظمية',
            'جراحة عامة، باطنة، أطفال، نسائية، عظمية، عصبية',
            'أطفال، جراحة أطفال، حديثي ولادة، عناية مشددة',
            'نسائية وتوليد، عناية حديثي ولادة',
            'جراحة عيون، عيون أطفال، شبكية',
            'جراحة عامة، باطنة، قلبية، عصبية، عظمية',
            'جراحة قلب، قسطرة، عناية مشددة'
        ]
    }
    hospitals_df = pd.DataFrame(hospitals_data)

    return df, transfers_df, hospitals_df

def main():
    st.title("👨‍⚕️ نظام متابعة الأطباء المقيمين")
    
    # Load data
    df, transfers_df, hospitals_df = load_sample_data()
    
    # Sidebar with hospital info and quick filters
    with st.sidebar:
        st.title("🏥 معلومات المشافي")
        selected_hospital_info = st.selectbox(
            "اختر مشفى لعرض معلوماته",
            hospitals_df['Name'].tolist()
        )
        
        hospital_info = hospitals_df[hospitals_df['Name'] == selected_hospital_info].iloc[0]
        st.markdown(f"""
        ### {hospital_info['Name']}
        
        **النوع:** {hospital_info['Type']}  
        **الموقع:** {hospital_info['Location']}  
        **عدد الأسرة:** {hospital_info['Beds']}  
        
        **الأقسام:**  
        {hospital_info['Departments']}
        """)
        
        st.divider()
        
        # Quick filters
        st.subheader("⚡ تصفية سريعة")
        hospital_type = st.radio(
            "نوع المشفى",
            ["الكل", "حكومي", "جامعي", "تخصصي", "خاص"]
        )
        
        if hospital_type != "الكل":
            filtered_hospitals = hospitals_df[hospitals_df['Type'] == hospital_type]['Name'].tolist()
            df = df[df['Hospital'].isin(filtered_hospitals)]
    
    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["📋 القائمة الرئيسية", "🔄 سجل النقل", "📊 التقارير"])
    
    with tab1:
        # Quick Stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_doctors = len(df)
            st.metric("إجمالي الأطباء", total_doctors)
            
        with col2:
            ending_soon = len(df[df['End_Date'] <= datetime.now() + timedelta(days=90)])
            st.metric("إقامات تنتهي خلال 3 أشهر", ending_soon)
            if ending_soon > 0:
                st.warning(f"⚠️ {ending_soon} أطباء تنتهي إقامتهم قريباً")
        
        with col3:
            specialties_count = len(df['Specialty'].unique())
            st.metric("عدد التخصصات", specialties_count)
            
        with col4:
            hospitals_count = len(df['Hospital'].unique())
            st.metric("عدد المشافي", hospitals_count)
        
        # Filters
        col1, col2 = st.columns(2)
        with col1:
            selected_hospital = st.selectbox(
                "المشفى",
                ["الكل"] + list(df['Hospital'].unique())
            )
        
        with col2:
            selected_specialty = st.selectbox(
                "التخصص",
                ["الكل"] + list(df['Specialty'].unique())
            )
        
        # Apply filters
        filtered_df = df.copy()
        if selected_hospital != "الكل":
            filtered_df = filtered_df[filtered_df['Hospital'] == selected_hospital]
        if selected_specialty != "الكل":
            filtered_df = filtered_df[filtered_df['Specialty'] == selected_specialty]
        
        # Search
        search = st.text_input("🔍 بحث عن طبيب", "")
        if search:
            filtered_df = filtered_df[
                filtered_df['Name'].str.contains(search, case=False) |
                filtered_df['Specialty'].str.contains(search, case=False) |
                filtered_df['Hospital'].str.contains(search, case=False)
            ]
        
        # Display data with expanders for each doctor
        st.subheader("📋 قائمة الأطباء المقيمين")
        for _, row in filtered_df.iterrows():
            with st.expander(f"{row['Name']} - {row['Specialty']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"🏥 المشفى: {row['Hospital']}")
                    st.write(f"👨‍⚕️ التخصص: {row['Specialty']}")
                    st.write(f"📅 تاريخ البدء: {row['Start_Date'].strftime('%Y-%m-%d')}")
                with col2:
                    st.write(f"🆔 رقم التعريف: {row['ID']}")
                    st.write(f"📊 الحالة: {row['Status']}")
                    end_date = row['End_Date']
                    days_remaining = (end_date - datetime.now()).days
                    if days_remaining <= 90:
                        st.warning(f"⚠️ تنتهي الإقامة في: {end_date.strftime('%Y-%m-%d')} (متبقي {days_remaining} يوم)")
                    else:
                        st.write(f"📅 تاريخ الانتهاء: {end_date.strftime('%Y-%m-%d')}")
                
                # Show transfer history for this doctor
                doctor_transfers = transfers_df[transfers_df['Doctor_ID'] == row['ID']]
                if not doctor_transfers.empty:
                    st.write("🔄 سجل النقل:")
                    for _, transfer in doctor_transfers.iterrows():
                        st.info(
                            f"تم النقل من {transfer['From_Hospital']} إلى {transfer['To_Hospital']} "
                            f"بتاريخ {transfer['Transfer_Date'].strftime('%Y-%m-%d')} "
                            f"- السبب: {transfer['Reason']}"
                        )
    
    with tab2:
        st.subheader("🔄 سجل النقل")
        # Transfer history with filters
        transfer_hospital = st.selectbox(
            "تصفية حسب المشفى",
            ["الكل"] + list(set(transfers_df['From_Hospital'].unique()) | set(transfers_df['To_Hospital'].unique()))
        )
        
        filtered_transfers = transfers_df
        if transfer_hospital != "الكل":
            filtered_transfers = transfers_df[
                (transfers_df['From_Hospital'] == transfer_hospital) |
                (transfers_df['To_Hospital'] == transfer_hospital)
            ]
        
        for _, transfer in filtered_transfers.iterrows():
            try:
                doctor_info = df[df['ID'] == transfer['Doctor_ID']]
                doctor_name = doctor_info.iloc[0]['Name'] if not doctor_info.empty else "غير معروف"
            except:
                doctor_name = "غير معروف"
            
            st.info(
                f"الطبيب: {doctor_name}\n"
                f"من: {transfer['From_Hospital']} ➡️ إلى: {transfer['To_Hospital']}\n"
                f"التاريخ: {transfer['Transfer_Date'].strftime('%Y-%m-%d')}\n"
                f"السبب: {transfer['Reason']}"
            )
    
    with tab3:
        st.subheader("📊 التقارير الإحصائية")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Specialty distribution
            specialty_counts = df['Specialty'].value_counts().reset_index()
            specialty_counts.columns = ['Specialty', 'Count']
            fig_specialty = px.pie(
                specialty_counts,
                values='Count',
                names='Specialty',
                title='توزيع التخصصات'
            )
            st.plotly_chart(fig_specialty, use_container_width=True)
        
        with col2:
            # Hospital distribution
            hospital_counts = df['Hospital'].value_counts().reset_index()
            hospital_counts.columns = ['Hospital', 'Count']
            fig_hospital = px.bar(
                data_frame=hospital_counts,
                x='Count',
                y='Hospital',
                orientation='h',
                title='عدد الأطباء في كل مشفى'
            )
            st.plotly_chart(fig_hospital, use_container_width=True)
        
        # Transfer trends
        st.subheader("اتجاهات النقل")
        transfers_per_month = transfers_df.groupby(transfers_df['Transfer_Date'].dt.strftime('%Y-%m'))['Doctor_ID'].count()
        fig_transfers = px.line(
            x=transfers_per_month.index,
            y=transfers_per_month.values,
            title='عدد عمليات النقل شهرياً',
            labels={'x': 'الشهر', 'y': 'عدد عمليات النقل'}
        )
        st.plotly_chart(fig_transfers, use_container_width=True)

if __name__ == "__main__":
    main()
