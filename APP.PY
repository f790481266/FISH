import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="私人案件進度管理系統", page_icon="📋", layout="wide"
)

st.title("📋 私人案件與進度歷程追蹤管理系統")
st.caption(
    "橫式互動表格：支援自由新增、修改、刪除項目，資料如 Excel 般直覺。"
)

# 初始化符合你 13 個條件的空白/示範資料
if "case_management_data" not in st.session_state:
  st.session_state.case_management_data = pd.DataFrame([
      {
          "編號": "001",
          "申請者": "範例申請者",
          "年月日": "2026-07-22",
          "公所/來文文號": "南市區字第12345號",
          "類型": "地面型",
          "審查進度": "審查中",
          "實況": "無",
          "提供給承辦日期(最新一次)": "2026-07-22",
          "最新進度日期(包含去函或來函)": "2026-07-22",
          "補正次數(局函的次數)": 0,
          "補正時間": "2026-07-22",
          "詳細歷程": "初次收件建立檔案",
      }
  ])

# 核心：互動式橫式表格 (data_editor)
edited_df = st.data_editor(
    st.session_state.case_management_data,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "類型": st.column_config.SelectboxColumn(
            "類型", options=["地面型", "屋頂型"], required=True
        ),
        "年月日": st.column_config.DateColumn("年月日", format="YYYY-MM-DD"),
        "提供給承辦日期(最新一次)": st.column_config.DateColumn(
            "提供給承辦日期(最新一次)", format="YYYY-MM-DD"
        ),
        "最新進度日期(包含去函或來函)": st.column_config.DateColumn(
            "最新進度日期(包含去函或來函)", format="YYYY-MM-DD"
        ),
        "補正時間": st.column_config.DateColumn("補正時間", format="YYYY-MM-DD"),
        "補正次數(局函的次數)": st.column_config.NumberColumn(
            "補正次數(局函的次數)", min_value=0, step=1
        ),
    },
)

# 儲存按鈕
if st.button("💾 儲存表格變更"):
  st.session_state.case_management_data = edited_df
  st.success("✅ 案件資料已成功更新！")

st.divider()

# 簡單總計
st.subheader("📊 總覽統計")
if not edited_df.empty:
  total_cases = len(edited_df)
  ground_count = len(edited_df[edited_df["類型"] == "地面型"])
  roof_count = len(edited_df[edited_df["類型"] == "屋頂型"])

  c1, c2, c3 = st.columns(3)
  c1.metric("總案件數", f"{total_cases} 件")
  c2.metric("地面型案件", f"{ground_count} 件")
  c3.metric("屋頂型案件", f"{roof_count} 件")
