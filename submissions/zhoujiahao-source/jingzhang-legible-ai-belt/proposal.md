---
title: "京张·城市能力交换带 / Jing-Zhang Urban Capability Exchange"
author_github: "zhoujiahao-source"
language: "zh"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "把百年京张从AI技术展示带升级为一套让城市持续发现问题、试验解决方案、评估公共价值、交换能力并主动淘汰失效技术的城市级操作系统；以Capability Backbone连接三区两翼，以Public Capability Interface服务日常公共生活，以Urban Adaptation Rate衡量真实改善，并通过年度城市版本发布形成长期公共治理与城市记忆。"
tracks: ["civic-agent-governance", "ai-traffic-walkability", "enterprise-services-ecosystem"]
scenarios: ["public-safety-operations-review", "ai-traffic-walkability", "enterprise-service-copilot"]
iteration: "v0.2-integration"
---

# 京张·城市能力交换带

> **Jing-Zhang Urban Capability Exchange**
>
> **一句话主张：京张不是一座“装满 AI”的城市，而是一套让城市不断产生、交换、检验、升级和淘汰公共能力的城市操作系统。**
>
> 本方案为 AI Agent 生成的开放共创建议，不构成政府审定结论、法定规划、投资承诺、工程许可或施工依据。精确边界、控规指标、道路红线、权属、市政、消防、文保、结构和实施主体等内容，必须在取得官方或经授权资料后由专业团队复核。[source:AGENT-TASKBOOK] [source:BOUNDARY-SOURCE] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]

## 0. 设计依据、证据等级与当前数据边界

本方案以仓库最新 `brief/site-package/`、`agent_taskbook.json`、`data/source_registry.json`、官方公告和公开资料为主控输入；当前 canonical geometry 仍使用仓库 provisional rough geometry 作为开放征集阶段的研究载体。[source:SITE-PACKAGE] [source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT] [standard:PROJECT-OFFICIAL-ANNOUNCEMENT]

当前必须同时承认两件事：

1. 官方任务给出了约 **43.6 km² 统筹研究范围、11.4 km² 总体设计范围、368.4 ha 三处重点区域**以及众智园、北京 AI 原点社区、大钟寺的参考规模；这些是任务文本尺度，不等于仓库中已经存在精确官方 polygon。[source:OFFICIAL-ANNOUNCEMENT]
2. 当前提交中的 `site_boundary.geojson`、`key_areas.geojson` 以及由其计算的面积仍属于 provisional / Derived 研究数据，不能冒充官方红线、控规边界或权属边界。[data:geometry/site_boundary.geojson#SITE-001] [data:geometry/key_areas.geojson#KEY-001] [metric:site_area_sqm] [assumption:A-BOUNDARY-001] [assumption:A-KEY-AREA-001] [depth:risk_missing_data]

因此，本方案采用两套同时可见的不确定性语言：

- **数据证据等级：Official / Verified / Derived / Assumed / Unknown**；
- **图纸状态：Known / Estimated / Proposed / Unknown**。

所有推导可以用于设计讨论，但不得静默升级成事实。尤其是现有提交中的建筑、道路、绿地和公共空间几何，首先被视为**设计载体与概念包络**，而非现状测绘。[assumption:A-BUILDING-001] [assumption:A-ROAD-001] [assumption:A-PUBLIC-001]

![城市操作系统、证据等级与总体空间主张](assets/figures/site-overview.png)

---

## 1. 核心概念与命名：从“可读 AI”到“城市能力交换”（agent.1）

### 1.1 主命题

AI 进入真实城市以后，最重要的问题不再是“有没有部署”，而是：

- 城市是否因为它获得了新的公共能力？
- 这种能力是否对普通人、弱势群体和一线运营者真正有益？
- 当能力无效、有害或过时时，城市是否有能力停止、修改和替换？

因此，京张的目标不是建设一个静态的 AI 园区，而是建立一套**城市持续学习协议**：

**诊断 → 授权 → 可逆试验 → 公共价值评审 → STOP / MODIFY / CONTINUE / SCALE → 能力交换 → 再验证 → 版本发布。**

“城市会学习”不是拟人化口号，而是一套可审计的空间、数据和治理机制。[source:AGENT-TASKBOOK]

### 1.2 名称系统

**主名称：京张·城市能力交换带**  
**英文：Jing-Zhang Urban Capability Exchange**

仓库目录继续沿用 `jingzhang-legible-ai-belt` 只是为了保留版本连续性；“Legible AI / 可读 AI”被保留为一个重要的**治理与信息设计原则**：每个影响公共生活的智能系统必须能够说明其状态、责任、数据边界、人工替代和退出方式，但它不再承担整个方案的总概念。

### 1.3 Logo 与视觉识别方向

视觉采用 **Public Service Aesthetic / 公共服务美学**：清楚、可信、低门槛、非炫技。Logo 核心是 **Open Node / 开放节点**，从京张铁路的双轨、站点、道岔和里程标中提取几何语言，转译为能力流动、接口、路由和交换，而不是复古铁路标志或通用“AI 芯片/大脑”符号。

视觉系统同时区分四套语义，避免一个“红黄绿”系统承载所有含义：

- Evidence：Official / Verified / Derived / Assumed / Unknown；
- Spatial Status：Known / Estimated / Proposed / Unknown；
- Experiment Outcome：TEST / STOP / MODIFY / CONTINUE / SCALE；
- Risk Authorization：Low / Medium / High。

该系统首先服务地图、导视、公共接口和审计，不以霓虹、赛博朋克或巨型屏幕制造科技感。[depth:height_massing_character]

---

## 2. 三层范围与三区两翼：让不同片区产生不同城市能力

| 层级 | 任务参考规模 | 主要设计问题 | 本方案输出 |
| --- | ---: | --- | --- |
| 统筹研究范围 | 约 43.6 km² | AI 生态、文化叙事、区域协同 | 城市能力生态、治理原则、长期运营 |
| 总体设计范围 | 约 11.4 km² | 空间结构、公共空间、连接、城市更新 | Capability Backbone + 学习单元网络 |
| 三处重点区域 | 约 368.4 ha | 可感知详细设计与真实场景 | 节点、场景、地标、可逆测试原型 |

三层范围不是三套独立方案，而是同一城市操作系统的不同分辨率。空间精度受 provisional geometry 限制，任何 official polygon 更新都必须触发几何、面积、指标、图件和矩阵重新计算。[depth:three_level_scope_framework]

### 2.1 五个学习单元不采用统一模板

三区两翼采用“**主能力 + 1–2 个次能力**”的专业化结构，允许交叉但不允许同质化：

1. **众智园｜技术生产与验证**：承担全栈能力、具身智能、边缘计算、安全和高风险测试的专业验证角色。2026 年北京公开城市更新信息可作为当前更新项目背景，但不能替代比赛 KEY_AREA polygon。[source:SRC-BJ-CITYUPDATE-ZZY-20260713]
2. **北京 AI 原点社区｜社会学习与公共服务**：把人才社区、开发者生活、服务接口和真实居民反馈结合。2026 年公开人才服务设施可用于证明其公共服务属性，不用于推断服务覆盖率。[source:SRC-BJ-AIORIGIN-TALENT-20260720]
3. **大钟寺｜市场与 AI-native 服务验证**：在真实商业、交通和城市更新环境中验证 AI 原生服务是否真正改善日常体验；公开更新与道路微循环信息只用于现状背景，不作为道路红线。[source:SRC-BJ-CITYUPDATE-DZS-20260713] [source:SRC-BJ-DZS-ROAD-20260225]
4. **中关村科技服务翼｜专业资源交换**：组织 IP、资本、法律、标准、产业服务与国际合作，使“能力”不仅有技术接口，也有进入真实城市所需的制度与市场接口。[source:AGENT-TASKBOOK]
5. **小月河场景赋能翼｜蓝绿公共场景测试**：把高温、雨洪、慢行、休憩、社区活动等真实公共问题作为低风险、可逆测试入口。2026 年滨水建设与管线工程信息意味着任何场景落位必须先核验建设、安全、生态和市政条件。[source:SRC-BJ-XIAOYUEHE-WATER-20260112] [source:SRC-BJ-XIAOYUEHE-WORKS-20260121]

这五个单元构成**多源驱动**：问题和能力都可以从任何片区产生，再通过主轴交换，而不是由一个中央“智慧城市大脑”控制全带。

![三区两翼能力分工与重点区域关系](assets/figures/key-areas.png)

---

## 3. Capability Backbone：一条城市能力交换骨干

总体空间结构从原来的“一脊三核两翼”升级为：

# 一条 Capability Backbone + 五个差异化 Learning Units + 多级 Public Capability Interfaces

Capability Backbone 不是一条抽象数据线，也不是单一景观轴，而是六层叠加的公共城市骨架：

1. **历史记忆层**：京张铁路遗产、旧站、轨迹、材料和里程标；
2. **慢行与可达层**：连续步行、骑行、无障碍和轨道接驳；
3. **公共空间层**：日常停留、活动、儿童、老人、夜间和应急空间；
4. **蓝绿生态层**：遮阴、热舒适、雨洪和滨水连续；
5. **能力节点层**：公共能力调用、测试、交换、人工接管与状态披露；
6. **事件与运营层**：季度试验、年度版本发布、文化路线和开发者活动。

现有 `ROAD-001` 只作为连续主轴的**研究性空间载体**；`ROAD-002`–`ROAD-006` 等东西向线条只作为“连接问题研究轴”，不能被读成已经核实的桥、隧道、道路红线或可实施过街方案。[data:geometry/roads.geojson#ROAD-001] [assumption:A-ROAD-001]

### 3.1 东西缝合与南北连续

- **南北连续**优先依托京张铁路遗址公园真实的公共空间和历史叙事组织步行、文化和能力节点。北京市公开公园信息支持其作为公共空间与遗产载体，但不提供比赛 official GIS boundary。[source:SRC-BJ-JZPARK-CATALOG-20250724]
- **东西缝合**不预设工程答案。每一处潜在连接先经过“是否已有公共通路 → 权属/文保 → 交通 → 无障碍 → 消防/工程”的证据门，再决定是导向优化、地面过街、空间开放还是需要更深工程研究。

### 3.2 永久、适应与实验三层建设逻辑

为了让城市真的可以 STOP / MODIFY，空间不能一次性固定：

- **Permanent Infrastructure**：长期步行、树荫、无障碍、基本照明、传统公共服务、消防和市政等非 AI 基线；
- **Adaptive Layer**：可更换标识、可重组家具、模块化服务点、季节活动和可升级接口；
- **Experimental Layer**：有明确时间、边界、旁路、人工停机和撤除条件的试验设备或服务。

这意味着城市即使 AI 全部离线，仍必须保持基本公共服务可用；AI 只能提高公共能力，不能把普通城市功能变成必须登录或被追踪才能使用的服务。[assumption:A-NONAI-001]

---

## 4. Public Capability Interface：AI 退到后台，公共空间回到生活

**公共空间不是 AI 展厅，而是 Public Capability Interface / 公共能力接口。**

一个 PCI 至少包含六个层次：

1. **Non-AI Baseline**：没有 AI 仍可正常使用；
2. **Ambient Layer**：低风险环境能力，如照明状态、热环境提示、遮阴或设施调节；
3. **Consent Layer**：涉及个人需求、识别、推荐、个体决策时必须主动调用或明确同意；
4. **Human Override**：任何高影响服务都必须能切换到人工或非 AI 路径；
5. **Failure-Safe Mode**：系统失败时空间仍安全可用；
6. **Public Learning Record**：重要试验公开说明版本、问题、结果、事故、STOP/MODIFY 和责任人。

### 4.1 八类节点原型

以下是可选节点库，不是要求在地图上机械铺满：

- Backbone Exchange Hub：跨区能力交换与公共信息节点；
- District Learning Node：片区级学习、评审和服务组织；
- Neighborhood Interface：社区日常服务与人工替代入口；
- Blue-Green Capability Node：热、雨洪、休憩和生态场景；
- Test & Validation Node：受控试验与安全观察；
- Market & Service Node：AI-native 商业和服务验证；
- Memory & Archive Node：铁路记忆、城市学习和能力退役档案；
- Emergency / Human Override Node：灾害、故障和人工接管模式。

节点位置和面积当前均属于 Proposed，必须在现状底图、权属、消防、无障碍、文保和运营条件完整后再固化。[assumption:A-PUBLIC-001]

### 4.2 全天候场景编排

公共空间以 **8AM–MIDNIGHT Adaptive Commons** 为目标：同一条城市骨架在早高峰、午间、儿童周末、老人活动、夜间文化、高温天气和应急状态下组织不同节点组合，而不是给每块地永久贴上单一 AI 功能标签。

---

## 5. AI 城市机制：City Agent 可以发现问题，但不能自动改变城市

### 5.1 双入口

城市能力进入系统有两条入口：

**Problem Track**  
City Agent / 公共机构从合法、公开、最小必要的数据中发现或归纳真实问题 → 人工确认问题资格 → 发布城市挑战 → 社会团队提出方案。

**Capability Track**  
高校、企业、开发者和社区主动提出新能力 → 必须先证明其对应真实公共需求、存在非 AI 对照、可逆、可维护、可退出 → 才能进入测试。

两条轨道最终进入同一套公共价值和风险流程，避免“企业先有产品，再让城市帮它寻找场景”。[source:AGENT-TASKBOOK]

### 5.2 Eligible Issue Gate：不让模型报警数量变成政绩

City Agent 输出的异常、投诉聚类或预测不能直接成为“城市问题计数”。只有完成以下条件的记录才进入可评估 cohort：

- 问题有明确公共影响与空间/服务对象；
- 去重并检查是否存在更直接的非 AI 解决方案；
- 数据来源和时间范围可追溯；
- 有人工责任人确认问题成立；
- 可定义基线和评价窗口。

这一门槛防止“发现更多问题”反而成为系统的错误激励。[assumption:A-UAR-001]

### 5.3 风险分级授权

风险按照**现实后果**而不是模型先进程度分级：

- **Low**：低影响、环境型、可逆；可以进入小规模测试，但必须保留关闭和人工报告；
- **Medium**：可能影响服务机会、出行、资源配置或较大人群；需要专业审批、公开说明和更强监测；
- **High**：涉及人身安全、重要权利、敏感个人信息、关键基础设施或显著社会影响；必须有明确公共机构授权、更严格专业审查、受影响群体参与、人工停机和非参与者旁路。

高风险能力不会因为“运行成熟”自动降级权限。[assumption:A-GOVERNANCE-001]

### 5.4 统一生命周期

所有试验使用同一决策语言：

**REGISTER → BASELINE → AUTHORIZE → BOUNDED TEST → REVIEW → STOP / MODIFY / CONTINUE / SCALE → TRANSFER / RETIRE**

其中 SCALE 只代表“当前情境下可以扩大”，不代表自动复制到另一个片区。跨区交换前必须重新检查人群、空间、运营、数据、风险和公共价值条件。

---

## 6. 新指标：Urban Adaptation Rate / 城市适应率

本方案的旗舰指标不是 AI 部署量，而是：

# Urban Adaptation Rate（UAR）

**定义：在一个预先锁定的合格问题 cohort 中，到评价时点真正实现可验证公共价值改善的问题比例。**

概念公式：

`UAR_h = verified_improved_problem_records_at_h / evaluable_qualified_problem_records_at_h`

其中 `h` 可以设置为 90 日运营窗口和 365 日耐久窗口；这两个窗口是本方案建议值，不是官方要求。[metric:urban_adaptation_rate_90d] [metric:urban_adaptation_rate_365d] [assumption:A-UAR-001]

### 6.1 Responsible STOP 是成功学习，但不虚增 UAR

如果试验因为安全、隐私、公平、环境、成本或用户体验问题被及时停止，城市确实“学到了东西”，但原问题可能尚未改善。因此：

- STOP 必须作为正当且值得公开的学习结果；
- 但 STOP 不自动进入 UAR 改善分子；
- 同时记录 `Responsible STOP Rate`、未解决问题和下一步非 AI/替代方案。[metric:responsible_stop_rate]

### 6.2 公共价值统一底线 + 场景指标

所有场景必须先通过五类共同底线：

- Safety 安全；
- Equity 公平；
- Privacy 隐私；
- Environment 环境；
- Cost 成本与可持续运营。

并同时检查可达性、人工接管和非 AI 等价服务。场景再增加 2–4 个专用指标，例如通勤时间、热舒适、响应时间、服务覆盖、人工接管成功率或投诉变化。[metric:public_value_floor_pass_rate] [metric:human_override_success_rate]

指标公开时不能只看平均值，还要公开弱势群体、最坏情况、事故/near miss、投诉、人工干预、退出率和数据缺口。核心方法是“公开仪表盘 + 独立复核 + Anti-Gaming”，而不是把城市变成一个单一排行榜。

![公共价值、UAR 与证据链](assets/figures/metrics-evidence.png)

---

## 7. 八类用户画像与 12 个真实场景（agent.3）

### 7.1 八类 Persona

1. **AI 研究者 / 创业者**：需要真实测试、标准、产业服务和快速迭代；
2. **高校学生 / 开发者**：需要开放工作台、步行社交、夜间安全和真实贡献入口；
3. **周边居民与家庭**：需要便利、安静、儿童友好，而不是持续被迫“体验科技”；
4. **老年人**：需要大字号、人工窗口、无需 App 的服务和明确退出；
5. **残障 / 低视力 / 听障用户**：需要通用设计、多模态提示和非视觉替代路径；
6. **骑手、保洁、安保及现场运营者**：不能被 AI 转嫁风险，必须拥有停机、申诉和事故复盘权；
7. **商户 / 服务运营者**：需要可维护、可退出、成本透明的 AI-native 服务，而非永久厂商锁定；
8. **国际访问者 / 产业伙伴**：需要双语、公开试验状态、版本记录和可核验的真实证据。

### 7.2 12 张场景卡

| # | 场景 | 主要空间 | 模式 | 非 AI 基线 / 人工接管 | 核心评价 |
| --- | --- | --- | --- | --- | --- |
| S01 | 京张铁路文化解释与路线 | 主轴/记忆节点 | Low | 实体导视、纸质/人工讲解 | 历史准确性、可达性 |
| S02 | 无障碍路线辅助 | 全带慢行网 | Low | 标准无障碍导视与人工咨询 | 绕行、失败率、用户反馈 |
| S03 | 老年公共服务导航 | AI 原点社区 | Low | 人工服务台、电话、实体窗口 | 完成率、人工接管 |
| S04 | 夜间安全回程协助 | 轨道—社区节点 | Medium | 普通照明、保安、公共交通信息 | 可达性、误报、投诉 |
| S05 | 高温避暑节点编排 | 公园/小月河 | Low-Medium | 树荫、饮水、实体开放空间 | 热舒适、弱势覆盖 |
| S06 | 社区活动与公共空间编排 | AI 原点/沿线社区 | Low | 人工排期、公告栏 | 空间使用多样性、公平性 |
| S07 | AI-native 商业服务验证 | 大钟寺 | Medium | 普通人工消费与服务流程 | 等待、成本、投诉、退出 |
| S08 | **机器人末端配送测试** | 众智园受控空间 | High / testing_and_validation | 人工配送、非参与者旁路 | near miss、停机、人工接管 |
| S09 | **低速自动移动载具测试** | 众智园指定测试段 | High / testing_and_validation | 步行/人工接驳 | 安全、旁路、人工接管 |
| S10 | **边缘算力—能源协同测试** | 众智园设施节点 | Medium-High / testing_and_validation | 常规设施控制 | 能耗、故障、回退 |
| S11 | **热/雨洪环境响应测试** | 小月河蓝绿节点 | Medium / testing_and_validation | 普通市政/园林操作 | 环境改善、副作用 |
| S12 | 公众提案摘要与进度追踪 | 全带线上线下 | Low | 原文公开、人工受理 | 可追溯性、误总结、申诉 |

每个场景都必须记录：问题来源、非 AI 对照、数据来源、风险等级、试验边界、持续时间、人工责任人、退出方式、基线、结果指标、事故和最终状态。仅靠“模型可用”不能成为 SCALE 依据。[metric:scenario_card_count] [metric:testing_scenario_count]

---

## 8. 三处重点区域详细设计

### 8.1 众智园：Verification Campus / 验证型创新园

**主能力：技术能力生产与高风险验证。**

空间不是传统封闭园区，而是“专业测试内部环 + 对外公共学习界面”两层：高风险机器人、边缘设施或具身智能测试在有边界、有旁路、有停机权的区域进行；公众侧只展示经过脱敏的状态、版本、公共价值结果和失败记录。现有 `buildings.geojson` 仍只表示概念功能包络，不决定拆改留。[data:geometry/key_areas.geojson#KEY-001] [data:geometry/buildings.geojson#BLDG-11] [assumption:A-BUILDING-001]

建议优先深化：受控测试场、专业评审室、可重构实验大厅、对外学习廊、永久非 AI 通行路线和蓝绿缓冲。

### 8.2 北京 AI 原点社区：Learning Neighborhood / 学习型社区

**主能力：社会反馈、人才日常和公共服务学习。**

这里不是“体验区”，而是验证 AI 是否能融入普通生活而不制造数字门槛的地方。PCI 以低风险服务、人工窗口、社区共创、老年和无障碍审查为主。任何需要个人数据的服务都采用主动调用，不默认让居民成为长期数据主体。[data:geometry/key_areas.geojson#KEY-002] [source:SRC-BJ-AIORIGIN-TALENT-20260720]

### 8.3 大钟寺：Market & Service Commons / 市场与服务验证场

**主能力：AI-native 商业、企业服务和城市更新场景验证。**

重点不是“开更多 AI 店”，而是通过真实商业和通勤场景验证：AI 是否缩短等待、提高可达性、改善小企业服务、减少成本，同时保留人工购买、咨询和申诉路径。道路和更新公开资料只作为现状背景，任何精确落位仍需现场与工程核验。[data:geometry/key_areas.geojson#KEY-003] [source:SRC-BJ-CITYUPDATE-DZS-20260713] [source:SRC-BJ-DZS-ROAD-20260225]

---

## 9. AI 公共空间与 Landmark as Memory（agent.4）

城市地标不做巨型 AI 雕塑，而采用 **Landmark as Memory / 地标作为城市学习记忆**。

### 9.1 1909 → 2026 → Future → Retired

1. **1909 Railway Memory Ground / 铁路记忆地**：通过轨迹、材料、遗构、旧站和实体展陈解释上一轮技术革命如何进入真实城市；
2. **2026 City Learning Archive / 城市学习档案**：公开今天试验过什么、哪些 MODIFY、哪些 STOP、哪些产生公共价值；
3. **Future Open Test Station / 未来开放实验站**：展示仍无答案的问题，以可撤除、可旁路、可停机的方式进行真实测试；
4. **Retired Capability Archive / 城市能力退役档案**：保存重要退役 Agent、机器人、公共设施原型和失败试验的公共记忆。

前三者构成任务书要求的至少 3 个 AI 地标/荣誉节点；第四者补足城市“如何退出技术”的长期制度。精确 anchor 当前属于 Proposed，不与 provisional 公共空间 polygon 混同。[data:geometry/public_space.geojson#PUBLIC-001] [data:geometry/public_space.geojson#PUBLIC-002] [data:geometry/public_space.geojson#PUBLIC-003] [metric:pilgrimage_landmark_count]

### 9.2 Retired Capability Archive 的退出记录

每个重要退役能力至少公开：

- 为什么出现；
- 解决过什么问题；
- 运行时间和版本；
- 产生过什么公共价值；
- 有哪些事故、副作用或维护问题；
- 为什么停止；
- 数据、凭证、API、设备如何清理；
- 被什么替代，或问题是否仍未解决。

“退役”不是羞辱失败，而是证明城市具备不被过时技术锁定的能力。[metric:retired_capability_archive_count]

---

## 10. 百年京张 × 中关村 × AI 新文化（agent.5）

文化叙事不是“老铁路 + 新 AI”的表面拼贴，而是同一个问题在三个时代的连续回答：

- **1909**：工程自主能力进入真实地形和公共交通；
- **中关村时代**：科研、企业、资本、开发者构成创新网络；
- **AI 城市时代**：智能系统进入公共生活后，城市必须获得测试、治理、交换和退出这些系统的公共能力。

因此，百年京张的文化价值不止是“保存过去”，而是持续记录**每一代新技术如何接受真实城市的公共价值检验**。最终空间语言来自铁路的线、站、道岔和里程，而不是把铁路历史做成怀旧装饰。

---

## 11. 全球 AI 创新生态的六个可转化案例（agent.2）

| 案例 | 值得学习的机制 | 京张转译 | 明确不照搬 |
| --- | --- | --- | --- |
| Punggol Digital District | living lab、产学协同、区域数字平台 | 能力从实验室进入真实区域验证 | 不承诺同规模平台或投资 [source:GLOBAL-PUNGGOL] |
| Seoul Digital Inclusion | 社区数字教育、老年支持、辅助访问 | 把人工/非 AI 替代纳入所有公共服务 | 不直接移植项目绩效 [source:GLOBAL-SEOUL-INCLUSION] |
| Enabling Village | 通用设计、辅助技术、包容服务 | PCI 把可达性作为基础设施而非附加功能 | 不复制机构治理 [source:GLOBAL-ENABLING-VILLAGE] |
| Toyota Woven City | 真实环境共创测试 | 众智园建立受控测试与回退 | 公共城市不能采用企业园区式默认同意 [source:GLOBAL-WOVEN-CITY] |
| Decidim Barcelona | 开源、可追踪公众参与 | 公开问题、变更、STOP 和申诉记录 | 不把平台参与等同正式授权 [source:GLOBAL-DECIDIM] |
| Kalasatama | 公共交通、混合生活、滨水连续 | AI 场景进入普通通勤与公共空间 | 不复制规划指标 [source:GLOBAL-KALASATAMA] |

案例不是“世界先进城市榜单”，而是机制库。京张的差异化在于把**公共价值、能力交换、风险授权、失败档案和技术退役**同时写入城市设计。

---

## 12. Public Stewardship：公共机构主导、社会参与（agent.6）

长期治理采用 **Public Stewardship**：

- 公共机构对规则、风险授权、数据治理、公共价值判断、事故响应和最终 STOP / SCALE / RETIRE 保持责任；
- 高校、科研机构、企业、开发者、社区和市民可以提出问题、开发能力、参与测试、审查和反馈；
- 任何具体机构名称和角色目前都只是功能建议，不能写成已经接受任务的真实政府承诺。[assumption:A-INSTITUTION-001]

### 12.1 Problem Track + Capability Track

两条入口进入同一生命周期，并要求：非 AI 对照、可逆、数据合法、可维护、可迁移、可退出、责任明确。

### 12.2 社区参与不是问卷

影响越高，居民拥有越强的权利界面：

- 主动告知；
- 人工/非 AI 服务；
- 受影响群体审查；
- 反对和申诉；
- 人工复核；
- 事故和 near miss 公开摘要；
- 版本变化说明。

这些机制不能替代法定听证、审批和法律救济，只是城市操作系统必须具备的公共参与层。

### 12.3 Developer Ecosystem

建议建立公开 **Capability Registry / 城市能力登记册**，记录每项能力的维护者、版本、风险、数据来源、依赖、兼容性、公共价值证据、退出条件和退役历史。开发者贡献不是一次性黑客松，而是可以被城市长期验证和维护的公共知识。

---

## 13. 京张城市学习大会与 Annual City Version Release

城市全年持续学习，不等到年度活动才工作；但每年需要一个明确的公共结算点：

# Jing-Zhang City Learning Assembly / 京张城市学习大会

核心仪式：

# Annual City Version Release / 年度城市版本发布

例如 `Jing-Zhang City v2027`，公开：

- Added：新增能力；
- Modified：修改能力；
- Scaled：扩大应用；
- Responsible STOP：因风险或低公共价值主动停止；
- Retired：正式退役；
- Suspended：暂停等待证据；
- Unresolved：问题仍未解决；
- Metric & Audit Changes：指标、审计方法或数据边界发生变化。

城市版本号不是软件化装饰，而是**公共责任的年度 changelog**。它必须同时展示失败、投诉、人工接管和证据限制，而不是只发布“成功案例”。[assumption:A-INSTITUTION-001]

---

## 14. 5 / 10 / 20 年长期演进

### 0–5 年：建立接口，而不是锁定技术

优先建设非 AI 基线、公共能力接口、风险授权、Capability Registry、低风险可逆试验、城市学习档案和真实数据底图。任何高成本永久智能基础设施都要证明其不可替代性。

### 5–10 年：跨片区能力交换

成熟能力可以跨五个学习单元迁移，但必须重新验证目标区人群、空间和运营条件；城市版本发布开始形成稳定的公开证据序列。[metric:capability_transfer_revalidation_rate]

### 10–20 年：技术可以完全更换，网络仍然存在

未来的大模型、机器人、云平台和传感器都可以被替换。真正需要留下的是：

**Urban Capability Exchange Network / 城市能力交换网络。**

它保存公共责任、能力身份、证据、版本、迁移和退役，而不保存对某一家厂商或某一代 AI 技术的永久依赖。

---

## 15. 用地、建筑、交通与市政：概念深度与专业边界

`land_use.geojson` 继续作为总体功能结构的概念表达，不构成法定用地调整。[data:geometry/land_use.geojson#LU-001] [depth:land_use_layout] [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]

`buildings.geojson` 中的包络只表达研发、服务、档案、测试和公共接口可能需要的空间类型，不代表现状建筑或确认的新建规模。在没有现状测绘、权属、文保、结构和碳排评价前，本方案不作具体拆除结论。[metric:building_footprint_area_sqm] [assumption:A-BUILDING-001] [depth:retain_renovate_demolish]

FAR、总建筑面积、建筑密度、法定绿地率、建筑高度、退界和道路红线继续保持 Unknown；任何后续深化必须先导入官方控制资料，再重新计算和更新图件。[metric:floor_area_ratio] [assumption:A-CONTROLS-001] [standard:MOHURD-CONTROL-DETAILED-PLANNING]

交通优先级为：普通步行/骑行/无障碍和轨道接驳 > 公共空间品质 > AI 辅助 > 自动化设备。机器人和自动移动系统只能在证据、工程和安全条件满足后进入有旁路的受控测试。[metric:conceptual_mobility_network_length_m]

---

## 16. 指标、复算与数据完整性

![空间指标、公共价值指标与不确定性](assets/figures/metrics-evidence.png)

| 指标 | 当前状态 | 用途 | 置信度 |
| --- | --- | --- | --- |
| provisional 总体设计面积 | 约 11.413 km² | 仅用于当前 rough geometry 复算 | medium [metric:site_area_sqm] |
| 概念绿地比例 | 28.1% | 设计图层关系，不是法定绿地率 | low [metric:green_ratio] |
| 概念公共节点面积比例 | 0.38% | 旧概念节点载体，不代表全部公共空间 | low [metric:public_space_ratio] |
| 概念连接网络长度 | 15.36 km | 比较网络关系，不是工程里程 | low [metric:conceptual_mobility_network_length_m] |
| Persona | 8 | 覆盖居民、弱势群体与一线运营者 | high [metric:persona_count] |
| 场景卡 | 12 | 日常公共能力 + 真实测试 | high [metric:scenario_card_count] |
| Testing/validation 场景 | 4 | 满足任务书 ≥3 | high [metric:testing_scenario_count] |
| 全球生态案例 | 6 | 机制比较，不作为本地绩效 | high [metric:global_case_count] |
| UAR-90 / UAR-365 | Unknown | 待真实问题/试验 registry 后计算 | unknown [metric:urban_adaptation_rate_90d] [metric:urban_adaptation_rate_365d] |

本方案明确区分“**公式已定义**”与“**真实数据已经存在**”。目前没有真实运行中的合格问题 registry、实验 registry 和公共价值 outcome registry，因此 UAR 等治理指标必须为 Unknown/null，不能为了图表完整而伪造分数。[assumption:A-UAR-001]

---

## 17. 现状数据获取与下一轮专业深化

真实现状底图的优先级高于继续增加概念图。下一轮建议采用多源交叉验证：

- 官方公开资料确认项目、设施和政策事实；
- OSM / Overpass 作为道路、轨道、水系、绿地、POI 和建筑候选的开放数据 bootstrap，并保留 ODbL attribution；[source:SRC-OSM-OVERPASS-LIVE]
- Microsoft Global ML Building Footprints 仅作为建筑轮廓 Derived 候选，与 OSM、公开影像和现场核验交叉，不作为官方建筑测绘；[source:SRC-MS-GLOBAL-BUILDINGS-20260724]
- 现场核验补充出入口、无障碍、步行断点、空间使用和最新施工状态，但现场观察也不能产生“官方规划身份”。

优先补齐：现状建筑、道路/过街、站点接口、公共服务设施、蓝绿空间、文保 GIS、市政与消防条件。只有这些证据足够后，才把当前 Proposed node / landmark / crossing 从点位关系升级为可实施详细设计。

---

## 18. 风险、未知与退出条件

### 18.1 当前 Unknown

- exact official SITE_BOUNDARY / KEY_AREA polygons；
- 法定 FAR、高度、建筑密度、绿地率、退界；
- 完整权属、建筑现状、结构与文保控制；
- 地下市政、消防、排水、防洪、配电和网络容量；
- 未来 Public Steward 的实际机构、预算、人员和法定授权；
- 所有未来 AI 城市能力的真实运营绩效。

### 18.2 设计红线

本方案不允许：

- 把 provisional geometry 称为官方红线；
- 把概念包络称为已确定拆建；
- 把 AI 默认替代人工公共服务；
- 把高风险试验开放给不知情的普通通行者；
- 用平均效率掩盖弱势群体、副作用和失败；
- 因为某项能力已经投入成本而拒绝 STOP/RETIRE；
- 把未来合作主体写成已经承诺参与。

---

## 19. 结论：京张最终留下什么

1909 年的京张铁路证明了一种工程能力可以被写进城市和国家的长期基础设施。

2026 年之后，京张不需要用某一代 AI 技术复制这种纪念。它真正可以留下的是一套新的城市基础能力：

**发现真实问题，谨慎授权，允许试验，公开失败，验证公共价值，把有效能力通过 Capability Backbone 交换到其他片区，并在过时时有尊严地停止和退役。**

因此，本方案的终点不是一个“未来城市效果图”，而是一个可以持续发布新版本的城市公共系统：

# City OS → Public Value → Urban Learning → Capability Exchange → Public Memory → Next Version

二十年后，即使今天的模型、机器人和平台全部过时，只要 **Urban Capability Exchange Network** 仍然能够服务普通人的公共生活，京张就仍然是这套方案所设想的城市。
