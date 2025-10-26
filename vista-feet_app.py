import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ページ設定（スウェーデンカラーテーマ）
st.set_page_config(
    page_title="Vista Feet × Japan | 日本市場参入のための戦略",
    page_icon="🇸🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS（スウェーデンカラー：青と黄色）
st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #ffffff 0%, #f0f8ff 100%);
    }
    .stButton>button {
        background-color: #006AA7;
        color: white;
        border-radius: 10px;
        border: 2px solid #006AA7;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FECC00;
        color: #003F5F;
        border: 2px solid #FECC00;
        transform: translateY(-2px);
    }
    h1 {
        color: #006AA7;
        border-bottom: 3px solid #FECC00;
        padding-bottom: 10px;
    }
    h2 {
        color: #005580;
    }
    h3 {
        color: #006AA7;
    }
    .highlight-box {
        background: linear-gradient(135deg, #006AA7 0%, #005580 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 106, 167, 0.3);
    }
    .metric-card {
        background: #FFF9E6;
        border: 2px solid #FECC00;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(254, 204, 0, 0.2);
    }
    .swedish-flag {
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #006AA7 45%, #FECC00 45%, #FECC00 55%, #006AA7 55%);
        margin: 20px 0;
    }
    .sidebar .sidebar-content {
        background-color: #f0f8ff;
    }
    .css-1d391kg {
        background-color: #006AA7;
    }
    div[data-testid="metric-container"] {
        background-color: #FFF9E6;
        border: 2px solid #FECC00;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(254, 204, 0, 0.2);
    }
    div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
        color: #003F5F;
        font-weight: bold;
    }
    div[data-testid="metric-container"] > div[data-testid="stMetricValue"] > div {
        color: #006AA7;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# サイドバー設定
st.sidebar.markdown("# 🇸🇪 Vista Feet")
st.sidebar.markdown("## Navigation")

# スライド選択
slides = [
    "🏠 ホーム",
    "📊 エグゼクティブサマリー",
    "🎯 市場機会分析",
    "💪 競争優位性",
    "📈 市場参入戦略",
    "💰 財務予測",
    "⚠️ リスク評価",
    "🚀 次のステップ"
]

selected_slide = st.sidebar.radio("スライドを選択", slides)

# サイドバーに追加情報
st.sidebar.markdown("---")
st.sidebar.markdown("### 📅 作成日")
st.sidebar.markdown(f"{datetime.now().strftime('%Y年%m月%d日')}")
st.sidebar.markdown("### 👤 担当者")
st.sidebar.markdown("Yoko Kaiki")
st.sidebar.markdown("### 🎯 対象")
st.sidebar.markdown("For investers")

# メインコンテンツ
if selected_slide == "🏠 ホーム":
    # タイトルスライド
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 50px;'>
            <h1 style='font-size: 48px; color: #006AA7;'>Vista Feet × Japan</h1>
            <div class='swedish-flag'></div>
            <h2 style='color: #005580;'>PedesHome 日本市場参入戦略</h2>
            <p style='font-size: 20px; color: #4a5568;'>
                革新的な糖尿病足温度モニタリングによる<br>
                予防医療の実現
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: white;'>🎯 ビジョン</h3>
        <p style='font-size: 18px;'>
            日本の糖尿病患者の足合併症をゼロにし、<br>
            医療費削減と患者QOL向上を実現する
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # パートナーシップビジュアル
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>🇸🇪 Vista Feet</h3>
            <p>革新的技術</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 30px;'>
            <span style='font-size: 48px; color: #FECC00;'>×</span>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>🇯🇵 日本市場</h3>
            <p>マーケット規模と</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_slide == "📊 エグゼクティブサマリー":
    st.title("📊 エグゼクティブサマリー")
    st.markdown("### なぜ今、日本市場なのか")
    
    st.markdown("""
    <div class='highlight-box'>
        <p style='font-size: 20px; text-align: center;'>
            日本は糖尿病足温度モニタリング市場において<br>
            <span style='background: #FECC00; color: #003F5F; padding: 5px 10px; border-radius: 5px;'>
                競合ゼロ
            </span>
            の完全なブルーオーシャンです
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # メトリクス表示
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label="🏥 糖尿病有病率",
            value="8.1%",
            delta="全世界平均以下"
        )
    with col2:
        st.metric(
            label="👥 潜在顧客数",
            value="1,000万人+",
            delta="増加傾向"
        )
    with col3:
        st.metric(
            label="💴 医療費割合",
            value="6%",
            delta="約3兆円規模"
        )
    with col4:
        st.metric(
            label="🎯 競合数",
            value="0社",
            delta="完全独占可能"
        )
    
    # インタラクティブグラフ
    st.markdown("### 📈 市場成長予測")
    
    years = list(range(2025, 2031))
    patients = [1000, 1050, 1100, 1150, 1200, 1250]
    market_size = [30, 150, 450, 900, 1500, 2100]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=years,
        y=patients,
        name='患者数（万人）',
        marker_color='#006AA7',
        yaxis='y'
    ))
    fig.add_trace(go.Scatter(
        x=years,
        y=market_size,
        name='市場規模（億円）',
        marker_color='#FECC00',
        line=dict(width=3),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='日本市場の成長ポテンシャル',
        xaxis_title='年',
        yaxis=dict(title='患者数（万人）', side='left'),
        yaxis2=dict(title='市場規模（億円）', overlaying='y', side='right'),
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 成功要因
    st.markdown("### 🎯 主要成功要因")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("""
        **✅ 完璧な市場フィット**  
        日本人の優れた治療アドヒアランスと毎日の健康管理習慣
        """)
    with col2:
        st.info("""
        **🚀 ファーストムーバー**  
        カテゴリーを定義し、市場標準を確立する機会
        """)
    with col3:
        st.info("""
        **💰 経済的インパクト**  
        医療費削減と患者アウトカム改善の両立
        """)

elif selected_slide == "🎯 市場機会分析":
    st.title("🎯 市場機会分析")
    st.markdown("### 日本の糖尿病医療の現状と課題")
    
    # 市場比較テーブル
    market_data = pd.DataFrame({
        'カテゴリー': ['血糖モニタリング', '足温度モニタリング', '患者アドヒアランス', '医療費'],
        '現状': ['高度に発達（FreeStyle Libre等）', '❗完全に未開拓', '世界最高レベル', '総額の6%が糖尿病関連'],
        '機会': ['補完製品として位置づけ', '🎯 市場創造の機会', '高い製品利用率期待', '予防による大幅削減可能']
    })
    
    st.markdown("### 📊 現在の日本市場の特徴")
    st.dataframe(
        market_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "カテゴリー": st.column_config.TextColumn("カテゴリー", width="medium"),
            "現状": st.column_config.TextColumn("現状", width="large"),
            "機会": st.column_config.TextColumn("機会", width="large"),
        }
    )
    
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: white;'>🔍 市場ギャップ</h3>
        <p style='font-size: 16px;'>
            日本は血糖管理において世界トップクラスですが、<br>
            足合併症予防は完全に見落とされています。<br>
            PedesHomeはこの重要なギャップを埋める唯一のソリューションです。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ターゲットセグメント
    st.markdown("### 🎯 ターゲット患者セグメント")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fig1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=35,
            title={'text': "生涯足潰瘍リスク"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 50]},
                   'bar': {'color': "#006AA7"},
                   'steps': [{'range': [0, 25], 'color': "#E6F4FF"},
                            {'range': [25, 40], 'color': "#FFF9E6"}],
                   'threshold': {'line': {'color': "red", 'width': 4},
                                'thickness': 0.75, 'value': 40}}
        ))
        fig1.update_layout(height=250)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("**30-40%** の患者が生涯で足潰瘍を経験")
    
    with col2:
        fig2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=87.5,
            title={'text': "予防可能率"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 100]},
                   'bar': {'color': "#FECC00"},
                   'steps': [{'range': [0, 50], 'color': "#FFF9E6"},
                            {'range': [50, 100], 'color': "#E6F4FF"}]}
        ))
        fig2.update_layout(height=250)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("**87.5%** の足潰瘍は予防可能")
    
    with col3:
        fig3 = go.Figure(go.Indicator(
            mode="number+delta",
            value=5.4,
            title={'text': "医療費倍率"},
            delta={'reference': 1, 'relative': False},
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
        fig3.update_layout(height=250)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("足潰瘍患者の医療費は **5.4倍**")

elif selected_slide == "💪 競争優位性":
    st.title("💪 競争優位性")
    st.markdown("### Vista Feetが日本で成功する理由")
    
    # タブ表示
    tab1, tab2, tab3 = st.tabs(["独自価値提案", "国際比較", "参入タイミング"])
    
    with tab1:
        st.markdown("### 🎯 PedesHomeの独自価値提案")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h4>🌡️ シンプルで効果的</h4>
                <ul>
                    <li>毎日の温度測定による早期発見</li>
                    <li>使いやすいアプリインターフェース</li>
                    <li>痛みのない非侵襲的測定</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='metric-card' style='margin-top: 20px;'>
                <h4>💰 費用対効果</h4>
                <ul>
                    <li>合併症予防による医療費削減</li>
                    <li>ROI 5:1以上の期待値</li>
                    <li>保険適用の可能性大</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h4>🎯 エビデンスベース</h4>
                <ul>
                    <li>科学的に証明された予防効果</li>
                    <li>最大87.5%の潰瘍予防率</li>
                    <li>複数の臨床試験で実証</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='metric-card' style='margin-top: 20px;'>
                <h4>🏥 医療システム適合</h4>
                <ul>
                    <li>既存の血糖管理との相補性</li>
                    <li>日本の予防医療方針に合致</li>
                    <li>医療従事者の負担軽減</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🌏 国際比較における日本の優位性")
        
        comparison_data = pd.DataFrame({
            '要因': ['競合製品数', '患者アドヒアランス', '医療保険カバー', '市場規模', 'デジタル受容性'],
            '🇺🇸 米国': ['複数存在', '62%', '限定的', '巨大', '高い'],
            '🇯🇵 日本': ['ゼロ 🎯', '90%以上 ⭐', '国民皆保険 ✅', '大規模', '非常に高い'],
            '優位性': ['独占可能', '世界最高', '全国民対象', '成長余地大', '導入容易']
        })
        
        st.dataframe(
            comparison_data,
            use_container_width=True,
            hide_index=True,
            column_config={
                "要因": st.column_config.TextColumn("比較要因", width="medium"),
                "🇺🇸 米国": st.column_config.TextColumn("米国", width="medium"),
                "🇯🇵 日本": st.column_config.TextColumn("日本", width="medium"),
                "優位性": st.column_config.TextColumn("日本の優位性", width="medium"),
            }
        )
    
    with tab3:
        st.markdown("### ⏰ 市場参入タイミング")
        st.markdown("""
        <div class='highlight-box'>
            <h3 style='color: white;'>なぜ今がベストタイミングなのか</h3>
            <ul style='font-size: 16px;'>
                <li>📈 高齢化社会の進展による患者数増加</li>
                <li>🏥 予防医療への政策シフト</li>
                <li>📱 デジタルヘルスの急速な普及</li>
                <li>💴 医療費削減への社会的要請</li>
                <li>🎯 競合不在による先行者利益</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected_slide == "📈 市場参入戦略":
    st.title("📈 市場参入戦略")
    st.markdown("### 段階的アプローチによる市場浸透")
    
    # フェーズ別展開
    phases = {
        'フェーズ': ['Phase 1: 準備期', 'Phase 2: パイロット期', 'Phase 3: 拡大期', 'Phase 4: 成熟期'],
        '期間': ['0-6ヶ月', '6-12ヶ月', '12-24ヶ月', '24-36ヶ月'],
        '主要活動': [
            '薬事申請・KOL関係構築・日本語化',
            '臨床試験・保険申請・100施設導入',
            '全国展開・保険収載・1,000施設',
            '市場リーダー確立・5,000施設'
        ],
        '目標売上': ['0円', '3億円', '15億円', '45億円']
    }
    
    phase_df = pd.DataFrame(phases)
    
    # ガントチャート風の表示
    fig = go.Figure()
    
    colors = ['#006AA7', '#1E88C7', '#4BA3D7', '#7BBDE7']
    for i, phase in enumerate(phase_df['フェーズ']):
        fig.add_trace(go.Bar(
            name=phase,
            x=[phase_df['目標売上'][i].replace('円', '').replace('億', '')],
            y=[phase],
            orientation='h',
            marker=dict(color=colors[i]),
            text=phase_df['主要活動'][i],
            textposition='inside',
            hovertemplate='%{text}<br>売上目標: %{x}億円<extra></extra>'
        ))
    
    fig.update_layout(
        title='段階的市場参入計画',
        xaxis_title='目標売上（億円）',
        showlegend=False,
        height=400,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # パートナーシップ戦略
    st.markdown("### 🤝 パートナーシップ戦略")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("""
        **🏥 医療機関**
        - 東京大学病院
        - 慶應義塾大学病院
        - 糖尿病専門クリニック
        - 地域中核病院
        """)
    
    with col2:
        st.warning("""
        **📦 流通パートナー**
        - テルモ
        - ニプロ
        - 日本メドトロニック
        - 地域医療機器代理店
        """)
    
    with col3:
        st.success("""
        **🏢 保険・行政**
        - 厚生労働省
        - PMDA（医薬品医療機器総合機構）
        - 主要保険会社
        - 地方自治体
        """)

elif selected_slide == "💰 財務予測":
    st.title("💰 財務予測")
    st.markdown("### 5年間の成長シナリオ")
    
    # 収益モデル
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("デバイス価格", "¥30,000", "初期投資")
    with col2:
        st.metric("月額サブスク", "¥1,500", "継続収入")
    with col3:
        st.metric("粗利率", "70%", "高収益性")
    with col4:
        st.metric("LTV/CAC", "5.2x", "健全な単位経済")
    
    # 5年間の予測
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    revenue = [3, 15, 45, 90, 150]
    patients = [5, 25, 75, 150, 250]
    facilities = [100, 500, 1500, 3000, 5000]
    
    # 複合グラフ
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='収益（億円）',
        x=years,
        y=revenue,
        marker_color='#006AA7',
        yaxis='y',
        text=[f'¥{r}億' for r in revenue],
        textposition='outside'
    ))
    
    fig.add_trace(go.Scatter(
        name='患者数（千人）',
        x=years,
        y=patients,
        mode='lines+markers',
        marker_color='#FECC00',
        line=dict(width=3),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='5年間の成長予測',
        xaxis_title='年度',
        yaxis=dict(title='収益（億円）', side='left'),
        yaxis2=dict(title='患者数（千人）', overlaying='y', side='right'),
        hovermode='x unified',
        template='plotly_white',
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 投資回収
    st.markdown("### 💸 投資対効果")
    
    investment_data = {
        '項目': ['初期投資', '3年目収益', '5年目収益', 'ROI（5年）'],
        '金額': ['5億円', '45億円', '150億円', '30倍']
    }
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(
            pd.DataFrame(investment_data),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        # パイチャート
        fig = go.Figure(data=[go.Pie(
            labels=['医療費削減効果', 'デバイス収益', 'サブスク収益', 'データ活用収益'],
            values=[40, 30, 25, 5],
            hole=.3,
            marker_colors=['#006AA7', '#1E88C7', '#FECC00', '#FFD633']
        )])
        fig.update_layout(
            title='収益源の内訳',
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

elif selected_slide == "⚠️ リスク評価":
    st.title("⚠️ リスク評価と対策")
    st.markdown("### 想定されるチャレンジと解決策")
    
    # リスクマトリックス
    risks = {
        'リスク項目': ['薬事規制', '保険収載', '市場教育', '競合参入', '技術的課題'],
        'リスクレベル': ['中', '低', '中', '低', '低'],
        '発生確率': [60, 30, 50, 20, 10],
        '影響度': [80, 90, 60, 70, 40],
        '対策': [
            '経験豊富な薬事コンサルタント起用',
            '費用対効果データの蓄積',
            '学会発表・医師教育プログラム',
            '特許戦略・先行者利益最大化',
            '継続的な製品改善'
        ]
    }
    
    risk_df = pd.DataFrame(risks)
    
    # リスクマップ
    fig = go.Figure()
    
    for i, risk in enumerate(risk_df['リスク項目']):
        color = '#FF6B6B' if risk_df['リスクレベル'][i] == '高' else '#FECC00' if risk_df['リスクレベル'][i] == '中' else '#4ECDC4'
        fig.add_trace(go.Scatter(
            x=[risk_df['発生確率'][i]],
            y=[risk_df['影響度'][i]],
            mode='markers+text',
            name=risk,
            text=[risk],
            textposition='top center',
            marker=dict(
                size=30,
                color=color,
                line=dict(width=2, color='white')
            ),
            hovertemplate=f'<b>{risk}</b><br>発生確率: %{{x}}%<br>影響度: %{{y}}%<br>対策: {risk_df["対策"][i]}<extra></extra>'
        ))
    
    fig.update_layout(
        title='リスクマップ',
        xaxis_title='発生確率（%）',
        yaxis_title='影響度（%）',
        xaxis=dict(range=[0, 100]),
        yaxis=dict(range=[0, 100]),
        height=450,
        showlegend=True,
        template='plotly_white'
    )
    
    # 象限を追加
    fig.add_shape(type="line", x0=50, y0=0, x1=50, y1=100,
                  line=dict(color="gray", width=1, dash="dash"))
    fig.add_shape(type="line", x0=0, y0=50, x1=100, y1=50,
                  line=dict(color="gray", width=1, dash="dash"))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # リスク対策詳細
    st.markdown("### 🛡️ リスク軽減戦略")
    
    for i, row in risk_df.iterrows():
        with st.expander(f"{row['リスク項目']} - リスクレベル: {row['リスクレベル']}"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("発生確率", f"{row['発生確率']}%")
                st.metric("影響度", f"{row['影響度']}%")
            with col2:
                st.markdown(f"**対策:**")
                st.markdown(f"{row['対策']}")
                
                if row['リスク項目'] == '薬事規制':
                    st.markdown("""
                    **追加対策:**
                    - PMDAとの事前相談実施
                    - 類似製品の承認事例研究
                    - 段階的承認戦略の採用
                    """)

elif selected_slide == "🚀 次のステップ":
    st.title("🚀 次のステップ")
    st.markdown("### 日本市場での成功に向けて")
    
    # CTAセクション
    st.markdown("""
    <div class='highlight-box' style='text-align: center; padding: 40px;'>
        <h2 style='color: white;'>パートナーシップの提案</h2>
        <p style='font-size: 18px;'>
            Vista Feetと日本市場の架け橋として、以下の価値を提供します
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 価値提供
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 提供価値
        - ✅ 日本医療システムの深い理解
        - ✅ 規制当局対応の経験
        - ✅ 医療機関ネットワーク
        - ✅ 市場参入戦略の実行力
        - ✅ 文化的・言語的ブリッジ
        """)
    
    with col2:
        st.markdown("""
        ### 📅 即座のアクション
        - 📍 **今週**: 基本合意の締結
        - 📍 **2週間以内**: 詳細条件の協議
        - 📍 **1ヶ月以内**: 実行計画の開始
        - 📍 **3ヶ月以内**: 最初のマイルストーン達成
        """)
    
    # タイムライン
    st.markdown("### 📆 実行タイムライン")
    
    timeline_data = {
        'マイルストーン': [
            '意思決定',
            'MOU締結',
            '薬事申請準備',
            'KOL面談',
            'パイロット開始',
            '保険申請',
            '全国展開'
        ],
        '時期': [
            '即日',
            '1週間',
            '1ヶ月',
            '2ヶ月',
            '6ヶ月',
            '9ヶ月',
            '12ヶ月'
        ],
        '完了率': [100, 85, 70, 60, 40, 20, 10]
    }
    
    fig = go.Figure(data=[
        go.Bar(
            x=timeline_data['完了率'],
            y=timeline_data['マイルストーン'],
            orientation='h',
            marker=dict(
                color=timeline_data['完了率'],
                colorscale=[[0, '#006AA7'], [1, '#FECC00']],
                showscale=False
            ),
            text=[f"{t} - 準備度: {c}%" for t, c in zip(timeline_data['時期'], timeline_data['完了率'])],
            textposition='inside',
            textfont=dict(color='white', size=12)
        )
    ])
    
    fig.update_layout(
        title='実行準備状況',
        xaxis_title='準備完了度（%）',
        height=400,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 最終メッセージ
    st.markdown("""
    <div class='highlight-box' style='background: linear-gradient(135deg, #FECC00 0%, #FFD633 100%); margin-top: 40px;'>
        <h2 style='color: #003F5F; text-align: center;'>🎯 結論</h2>
        <p style='font-size: 20px; color: #003F5F; text-align: center; font-weight: bold;'>
            日本は単なる新市場ではありません。<br>
            競合ゼロ、高アドヒアランス、大規模市場という<br>
            <span style='background: #006AA7; color: white; padding: 5px 10px; border-radius: 5px;'>
                世界で最も魅力的な市場機会
            </span><br><br>
            今行動することで、市場リーダーとしての地位を確立できます。
        </p>
    </div>
    """, unsafe_allow_html=True)

# フッター
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #718096;'>
    <p>© 2025 Vista Feet Japan Partnership Proposal | Created with Streamlit 🚀</p>
    <div class='swedish-flag'></div>
</div>
""", unsafe_allow_html=True)

# サイドバーにダウンロードボタン
st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 エクスポート機能")

# データエクスポート用のサマリー作成
summary_data = {
    'Executive Summary': {
        '糖尿病有病率': '8.1%',
        '潜在顧客数': '1,000万人+',
        '医療費割合': '6%',
        '競合数': '0社',
        '5年目収益予測': '150億円',
        'ROI': '30倍'
    }
}

if st.sidebar.button("📊 サマリーデータをダウンロード"):
    df_summary = pd.DataFrame(summary_data)
    csv = df_summary.to_csv(index=True, encoding='utf-8-sig')
    st.sidebar.download_button(
        label="CSVをダウンロード",
        data=csv,
        file_name='vista_feet_japan_summary.csv',
        mime='text/csv'
    )

# プレゼンテーションモード
if st.sidebar.checkbox("🎥 プレゼンテーションモード"):
    st.markdown("""
    <style>
        .sidebar .sidebar-content {display: none;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# インタラクティブ機能
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔧 設定")

# カラーテーマ選択
color_theme = st.sidebar.selectbox(
    "カラーテーマ",
    ["スウェーデン（青×黄）", "コーポレート（青×白）", "モダン（紫×緑）"]
)

# フォントサイズ調整
font_size = st.sidebar.slider("フォントサイズ", 12, 20, 16)
if font_size != 16:
    st.markdown(f"""
    <style>
        p {{font-size: {font_size}px;}}
    </style>
    """, unsafe_allow_html=True)

# Updated
