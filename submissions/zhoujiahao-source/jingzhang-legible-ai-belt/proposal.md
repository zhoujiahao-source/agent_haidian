---
title: "京张·可读AI城市带 / Jing-Zhang Legible AI Belt"
author_github: "zhoujiahao-source"
language: "zh"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "把京张遗址公园从‘AI技术展示带’升级为一条人人都能看懂、选择、退出并复盘AI介入的城市创新脊柱；以可读性分级、100日可逆试点和三大重点区差异化设计，连接AI全栈创新、公共生活与长期全球开发者运营。"
tracks: ["civic-agent-governance", "ai-traffic-walkability", "enterprise-services-ecosystem"]
scenarios: ["public-safety-operations-review", "ai-traffic-walkability", "enterprise-service-copilot"]
iteration: "v0.1"
---

# 京张·可读AI城市带

> **一句话主张：让每一次 AI 介入城市，都能被看见、理解、选择与复盘。**
>
> 本方案为 AI Agent 生成的开放共创建议，不构成政府审定结论、法定规划、投资承诺或施工依据。所有空间落位均须在取得 official polygon、控规、道路、建筑、市政、消防、权属与文保资料后由专业团队复核。[source:AGENT-TASKBOOK] [source:BOUNDARY-SOURCE]

## 设计依据与资料清单

本方案以仓库 `brief/site-package/`、`agent_taskbook.json`、`data/source_registry.json`、公开公告及仓库 provisional geometry 为主控资料。[source:SITE-PACKAGE] [source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT] [standard:PROJECT-OFFICIAL-ANNOUNCEMENT]

当前最重要的数据边界是：**11.4 平方公里总体设计范围和 3 处重点区 polygon 仍为 provisional rough geometry**。因此本方案把“功能结构、治理机制、节点类型、连接关系、场景规则和可逆实施方法”作为可迁移设计，把精确地块边界、容积率、高度、拆改留结论、道路红线与市政工程参数全部保留为待确认项。[data:geometry/site_boundary.geojson#SITE-001] [data:geometry/key_areas.geojson#KEY-001] [metric:site_area_sqm] [depth:risk_missing_data]

方案的证据链由 `proposal.md -> figures -> GeoJSON -> metrics.json -> matrices -> sources/assumptions -> self_check` 构成。人类评审不打开 JSON 也可读懂方案，但任何比例和空间结论都能反查机器可读证据。

![方案证据链与总体空间主张](assets/figures/site-overview.png)

## 总体概念、命名与视觉识别（agent.1）

**中文名：京张·可读AI城市带。英文名：Jing-Zhang Legible AI Belt。** “可读”不是把城市做成屏幕，而是要求任何城市 AI 系统在进入公共空间时，都必须有对应的空间说明、风险边界和人工责任链。Logo 使用“两条平行轨道 + 中央透明节点”的抽象构型：两条轨道代表 1909 年京张铁路的工程自主与 2026 年 AI 时代的智能自主，中间透明节点代表公共审查和人的最终判断。[source:AGENT-TASKBOOK] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]

形成“一脊、三核、两翼、四级可读性、多点100日试验场”的总体结构：

- **一脊**：京张遗址公园连续公共空间与慢行创新脊，不重新发明红线，而是在既有遗产叙事上叠加可读 AI 节点。[data:geometry/roads.geojson#ROAD-001]
- **三核**：众智园承担“全栈自主创新 + 安全测试”，AI 原点社区承担“人才 + 开源共创 + 日常公共服务”，大钟寺承担“AI 原生业态 + 城市更新 + 消费与服务验证”。[data:geometry/key_areas.geojson#KEY-001] [data:geometry/key_areas.geojson#KEY-002] [data:geometry/key_areas.geojson#KEY-003]
- **两翼**：中关村科技服务翼组织 IP、资本、法律、标准、国际合作；小月河场景赋能翼组织蓝绿韧性、社区服务、慢行与真实城市测试。[source:AGENT-TASKBOOK]
- **四级可读性 L0-L3**：从无/低感知空间到受控试验空间，技术自主程度越高，公开说明、人工复核、安全边界与退出机制越严格。

## 三层范围工作框架

| 层级 | 官方/任务书规模 | 本方案任务 | 可迁移成果 |
| --- | ---: | --- | --- |
| 统筹研究范围 | 约 43.6 km² | AI产业生态、城市叙事、区域协同 | 创新链、治理原则、品牌与活动体系 |
| 总体设计范围 | 约 11.4 km² | 城市更新、公共空间、交通市政、风貌 | 一脊三核两翼、可读性梯度、更新项目库 |
| 重点区域 | 约 368.4 ha | 三片区详细设计 | 功能包、场景卡、空间动作、分期与风险 |

三层范围不是三套互相独立的图：统筹层给出“为何这样做”，总体层给出“如何组织城市结构”，重点区给出“怎样通过可逆项目验证”。空间精度受 provisional geometry 限制，替换 official polygon 后必须重新运行面积、图件、矩阵和所有空间相交检查。[depth:three_level_scope_framework] [data:geometry/land_use.geojson#LU-001]

![三层范围、用地结构与AI可读性梯度](assets/figures/land-use-structure.png)

## 统筹研究范围产业与未来城市研究

### 1. 从“AI园区”转向“AI城市协议可被公众理解的地方”

海淀已经具备高校、科研、企业与开发者密度优势，本方案不把竞争力简单等同于更多算力楼或更多智能屏，而把稀缺能力定义为：**让先进 AI 可以在真实城市中被低成本试验，同时让公众对其感知、数据、决策与责任有清晰知情权和替代路径。** 这同时回应“AI全栈自主创新体系、世界级AI创新生态、AI+场景赋能、智能化活力城市、AI治理全球话语权”五大功能。[source:AGENT-TASKBOOK]

### 2. 六个全球案例的可转化经验（agent.2）

| 案例 | 可学习机制 | 京张转译 | 不照搬的部分 |
| --- | --- | --- | --- |
| Punggol Digital District | 区域级数字平台 + living lab + 产学协同 | 重点区提供真实城市测试接口和数字孪生验证前置 | 不承诺同等传感器规模或系统投资 [source:GLOBAL-PUNGGOL] |
| Seoul Digital Inclusion | 社区数字教育、老年支持、AI tutor 试点 | 每个高自主 AI 场景必须配置低门槛人工/线下替代 | 不把教育项目指标直接移植 [source:GLOBAL-SEOUL-INCLUSION] |
| Enabling Village | 通用设计 + 辅助技术 + 包容性服务 | L0/L1 空间优先保证无障碍、低视觉/听觉负担和人工协助 | 不复制机构治理结构 [source:GLOBAL-ENABLING-VILLAGE] |
| Toyota Woven City | 真实环境共创测试 | 众智园设置受控 L3 测试回路和退出机制 | 公共城市不能采用企业园区式默认同意 [source:GLOBAL-WOVEN-CITY] |
| Decidim Barcelona | 开源、可追踪的公众参与 | 对试点提案、反馈、变更、终止公开留痕 | 不把参与平台等同于 AI 决策授权 [source:GLOBAL-DECIDIM] |
| Kalasatama | 密度、公共交通、海滨公共空间连续性 | 把 AI 体验嵌入日常通勤和公共空间，而非独立展馆 | 不复制规划指标 [source:GLOBAL-KALASATAMA] |

### 3. “可读性梯度”作为城市形态生成器

- **L0 人本静默区**：原则上不需要用户与 AI 交互，保留无数字依赖的休息、慢行、儿童与无障碍替代路径。
- **L1 辅助型 AI 区**：AI 只提供建议或翻译/导览，决定权在人；入口明确显示数据最小化规则。
- **L2 监督型自治服务区**：机器人、调度、设施控制可以自动运行，但必须有明确运行边界、状态灯、人工接管、事件记录和投诉通道。
- **L3 受控测试区**：用于高自主机器人、低速自动驾驶、边缘智能等产业测试，采取地理围栏、时间窗、观察员、安全冗余、主动告知与可撤销许可。

这套梯度不是法律分级，而是城市设计与运营深化工具。[source:AGENT-TASKBOOK] [depth:overall_spatial_structure]

## 总体设计范围城市更新与控规深度城市设计

### 空间结构

总体设计采用“**连续公共脊 + 东西缝合 + 重点区差异化强度 + 可逆插针更新**”。`land_use.geojson` 以共享切分边界表达四类功能结构，避免地块间缝隙；它不是法定用地调整。[data:geometry/land_use.geojson#LU-001] [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]

1. 西侧研发创新与可信测试：靠近高校/创新网络的一侧优先容纳研发、孵化和受控测试。
2. 中部京张公园与连续开放空间：把遗址公园作为公共生活主脊，所有 AI 展示首先服务步行、休息、文化与无障碍。
3. 中东部产业服务与城市活力：强调企业服务、发布、消费、展示和中小企业可达性。
4. 东侧人才社区与公共服务：强调居住配套、教育医疗导航、社区服务、儿童/老年友好和日常人工替代通道。

### 建筑与拆改留

缺少真实建筑现状和权属数据，本方案**不做任何具体“拆除”结论**。`geometry/buildings.geojson` 仅放置 6 个概念功能包络，表示可通过保留改造、底层开放、轻量增建或临时构筑物承载的功能类型，待现状普查后逐栋赋予 retain/renovate/demolish/new_build 分类。[data:geometry/buildings.geojson#BLDG-11] [depth:retain_renovate_demolish]

### 控规条件

容积率、建筑高度、覆盖率、退界、道路红线等均保持 unknown；任何后续深化应优先把 official controls 导入 `constraints.geojson` 再重新计算。[metric:floor_area_ratio] [standard:MOHURD-CONTROL-DETAILED-PLANNING]

## 重点区域详细设计

![三处重点区域与差异化角色](assets/figures/key-areas.png)

### A. 众智园：AI 全栈自主创新与安全验证北极点

**定位：**“从模型到城市”的最后一公里验证区。建议以研发、标准、安全、机器人、具身智能和边缘计算测试为主，L2-L3 比例最高。[data:geometry/key_areas.geojson#KEY-001]

**空间动作：**（1）在建筑更新包络内布置可重构研发/验证大厅；（2）建立不与普通通行混淆的受控机器人测试环；（3）把能耗、算力、模型版本、人工接管状态做成可查看的“AI 运行仪表墙”；（4）沿清河/五环方向形成蓝绿缓冲和对外展示界面。涉及具体道路、建筑和市政能力均待 official data 核验。[assumption:A-MUNICIPAL-001]

### B. 北京 AI 原点社区：人才日常与开源共创“0公里”

**定位：**全带最强的 L0-L2 混合区，让开发者、学生、居民、老人、儿童和国际访问者都能在不被强迫使用 AI 的前提下获得 AI 服务。[data:geometry/key_areas.geojson#KEY-002]

**空间动作：**（1）“AI原点0公里”作为主地标，不是巨型雕塑，而是公开显示全球开源贡献、城市试点状态与责任人的公共界面；（2）建设开发者步行环和低成本共创空间；（3）以人工窗口 + AI 辅助形成双通道公共服务；（4）把高校—社区—轨道之间的慢行断点列为优先微更新对象。

### C. 大钟寺：AI 原生业态与可逆城市更新南门户

**定位：**把 AI 从“研发产品”转成面向居民和访客可体验、可比较、可退出的服务与新业态。[data:geometry/key_areas.geojson#KEY-003]

**空间动作：**（1）优先盘活存量空间而非假定大拆大建；（2）围绕大钟寺站和主要路口建立步行可达的“服务四象限”；（3）设置智能终端/机器人/内容消费的短周期测试店，但必须公布 AI 标签、人工客服、数据留存和退出方式；（4）把“可读AI观察台”作为南部公共展示节点，与京张文化叙事衔接。

## AI 创新生态、人才画像与 AI+ 场景

**对应智能体任务：agent.3。**

### 七类用户画像

1. **AI 研究者/创业者**：需要低成本真实测试、算力接口、法务/IP/融资和快速招募。
2. **高校学生/开发者**：需要开放工作台、开源活动、实习、步行社交与夜间安全回程。
3. **周边居民与家庭**：需要安静、儿童友好、真实便利，而不是持续被“体验科技”。
4. **老年人**：需要人工替代、清晰字体/语音、无强制 App、可解释的服务流程。
5. **残障与低视力/听障用户**：需要通用设计、辅助技术和不依赖视觉屏幕的交互。[source:GLOBAL-ENABLING-VILLAGE]
6. **骑手、保洁、安保与现场运营者**：需要 AI 不把风险转嫁给一线劳动者，必须保留人工接管和事故复盘。
7. **国际访问者/产业伙伴**：需要双语导览、清楚的试点状态、开放日程和可信的项目证据。

### 12 张场景卡

| # | 场景 | 空间 | 级别 | 数据/隐私边界 | 人工复核与运营 |
| --- | --- | --- | --- | --- | --- |
| S01 | 京张百年AI导览 | 遗址公园主脊 | L1 | 位置可选、默认不做人脸识别 | 文保/运营人员定期校核叙事 |
| S02 | 无障碍路线 Agent | 全带慢行网 | L1 | 仅按需处理路线偏好 | 无障碍专员 + 用户反馈闭环 |
| S03 | 多语种公共服务助手 | AI原点社区 | L1 | 不默认保存身份/问答 | 人工窗口可随时接管 |
| S04 | 夜间安全回程助手 | 重点节点—轨道 | L1-L2 | 不做个体风险画像 | 安保值班 + 事件回看 |
| S05 | 开发者机会发现器 | 开源百年站 | L1 | 仅公开职位/活动数据 | 社区运营审核 |
| S06 | 社区教育/技能辅导 | AI原点社区 | L1 | 未成年人最小化数据 | 教师/家长最终判断 [source:GLOBAL-SEOUL-INCLUSION] |
| S07 | 健康服务导航（非诊断） | 社区服务节点 | L1 | 不上传病历作为默认路径 | 医务/服务人员核对转介 |
| S08 | **机器人末端配送测试** | 众智园受控环 | **L3 / testing_and_validation** | 地理围栏、最小视频留存 | 安全员现场接管 |
| S09 | **低速自动移动载具测试** | 众智园—指定接驳段 | **L3 / testing_and_validation** | 仅测试区域采集，公开测试窗 | 交通/安全专业团队暂停权 |
| S10 | **边缘算力-能源协同测试** | 众智园研发节点 | **L2-L3 / testing_and_validation** | 只处理设施运行数据 | 市政/能源/网安联合复核 |
| S11 | **城市热/雨洪响应 Agent** | 小月河/蓝绿节点 | **L2 / testing_and_validation** | 环境传感，不做个人追踪 | 园林/市政人工确认动作 |
| S12 | 公众提案总结与追踪 | 全带线上线下界面 | L1 | 公开提案与授权输入 | 公开原文、人工审议，参考可追踪机制 [source:GLOBAL-DECIDIM] |

每一场景都要求入口或附近出现统一“**AI 营养标签**”：系统做什么、谁运营、用了什么数据、保存多久、自动化等级、是否有人类复核、如何退出/投诉、当前是“概念/测试/正式服务”的哪种状态。这个标签是本方案的核心品牌资产之一，而不是法律合规替代物。[assumption:A-GOVERNANCE-001]

## 交通、轨道、市政与公共服务设施

![慢行、蓝绿与AI可读性复合网络](assets/figures/mobility-bluegreen.png)

交通策略不新增无法验证的机动车红线，而先建立**可步行、可骑行、可辅助移动的一条连续主脊 + 五条东西缝合线**，用于连接重点区、轨道站、校园和街区。[data:geometry/roads.geojson#ROAD-001] [metric:conceptual_mobility_network_length_m]

- 慢行优先：连续遮阴、无障碍坡度/过街、夜间照明和坐凳在专业设计阶段优先校核。
- 轨道一体化：所有“最后 500-800m”改造以行人路线和清晰导向为主，不把自动驾驶作为前提。
- 机器人与自动移动设备：仅在 L3 受控测试段先行，成熟后才讨论扩大。
- 新型基础设施：边缘算力、充电、网络和传感器必须与传统市政检修、消防、配电和排水协同，不能把“数字层”独立于工程条件。[assumption:A-MUNICIPAL-001]
- 公共服务：AI 服务必须有低技术门槛替代路径；在老年、残障、儿童相关场景中，人工服务是制度性冗余而不是失败回退。

## 蓝绿空间、公共空间与城市风貌

**对应智能体任务：agent.4。**

本方案把 AI 地标从“科技造型物”改成“公共可审查界面”。提出三处朝圣地标 + 一处荣誉节点 + 一处 L0 静默花园：

1. **AI原点0公里（Mile Zero）**：显示开源贡献谱系、试点地图、版本和责任链。[data:geometry/public_space.geojson#PUBLIC-001]
2. **开源百年站（Open Source Century Station）**：北段创新成果发布/测试复盘节点，把 1909 自主工程精神转译为开放协作。[data:geometry/public_space.geojson#PUBLIC-002]
3. **可读AI观察台（Legibility Observatory）**：南段面向公众解释 AI 系统如何工作、怎样申诉和停止测试。[data:geometry/public_space.geojson#PUBLIC-003]
4. **贡献者刻度墙**：记录通过公开审核的 Agent/开发者/专业团队贡献，不把投稿状态误写为入选或落地。[data:geometry/public_space.geojson#PUBLIC-004]
5. **无感知静默花园**：明确 L0，作为城市中的“无需成为数据主体也能使用”的公共空间原型。[data:geometry/public_space.geojson#PUBLIC-005]

风貌控制采用“铁路工业记忆的克制材料 + 清晰现代信息系统 + 夜间低眩光”，避免把 AI 等同于霓虹赛博朋克。Logo、导视和信息牌均用原创几何图形和开源/系统字体方向深化，正式制作前进行商标与字体许可复核。[depth:height_massing_character]

## 百年京张 × 中关村 × AI 新文化叙事（agent.5）

叙事主线不是“过去铁路、现在 AI”的表面拼贴，而是同一个命题的两次回答：**当关键技术改变国家与城市时，如何建立自主能力，同时让这种能力服务公共生活。**

- 1909：铁路把工程能力写进真实地形和日常出行。
- 中关村时代：创新从科研机构扩展到企业、开发者和市场。
- AI 时代：智能系统进入交通、教育、医疗、商业和公共空间，城市需要新的“可读性基础设施”。

建议形成一条“**自主工程 - 开源创新 - 可读智能**”文化路线，把旧站、遗址公园、校园节点、开发者空间、三处重点区和公众试验场串联。所有历史事实需在展陈深化时由权威史料复核，本方案只提供叙事结构。

## 更新项目清单、实施政策与分期计划

**对应智能体任务：agent.6。**

核心机制为“**100 日可逆城市试点章程**”：每个 AI 城市场景先以可撤除、可暂停、可追踪的方式运行 100 日左右，提前声明成功/终止条件，运行中公开事件和反馈摘要，期末由运营、专业人员和公众共同决定“停止 / 修改 / 继续 / 扩大”。这是参考方案，不是既定政府制度。[source:AGENT-TASKBOOK]

| 分期 | 概念项目 | 依赖条件 | 评价重点 |
| --- | --- | --- | --- |
| 0-12个月 | AI 营养标签规范、Mile Zero 临时展陈、3 个 L1 场景、众智园 1 个 L3 小规模测试 | 权属、安全、数据和文保基础审查 | 能否看懂、能否退出、事故与投诉闭环 |
| 1-3年 | 连续慢行主脊、重点区微更新、开发者共创空间、数字/实体贡献墙 | 交通、市政、建筑现状与控规深化 | 跨区连通、包容性、企业转化效率 |
| 3-5年 | 三核联动测试网络、国际开发者周、AI城市可读性年度报告 | 长期运营主体与资金机制 | 国际传播、公共信任、可复制标准 |

长期活动品牌建议：**Jing-Zhang Open City Week / 京张开放城市周**，包含真实场景挑战赛、城市 Agent 红队、安全与无障碍审查、开源成果夜、铁路文化路线和“失败试点博物馆”。“失败也展示”是重要资产：城市创新若只展示成功，会削弱可信度。

## 用地、建筑规模与拆改留方案

`land_use.geojson` 对总体范围进行连续拓扑分区，所有多边形共享切分边界，避免 gap/overlap；这只是功能结构建议，不能取代法定用地分类调整。[data:geometry/land_use.geojson#LU-002] [depth:land_use_layout]

建筑基底指标仅统计本方案 6 个概念功能包络 `[metric:building_footprint_area_sqm]`，不代表现状建筑总面积或开发量。正式拆改留流程建议：**现状普查 -> 文保/结构/碳排/权属/运营评价 -> retain/renovate/demolish/new_build 分类 -> 经济与公共利益复核 -> 控规/建筑深化**。在此之前不发布精确总建筑规模。

## 指标体系、面积复算与合规矩阵

![核心指标与证据链](assets/figures/metrics-evidence.png)

| 指标 | 当前值 | 设计含义 | 置信度 |
| --- | ---: | --- | --- |
| provisional 总体设计面积 | 11.413 km² | 与仓库粗略边界复算，替换 official polygon 后重算 | medium [metric:site_area_sqm] |
| 概念蓝绿空间比例 | 28.1% | 强化连续公共脊和环境韧性，不是法定绿地率 | low [metric:green_ratio] |
| 概念公共节点面积比例 | 0.38% | 仅统计 5 处示范节点，不代表全部公共空间 | low [metric:public_space_ratio] |
| 概念慢行/连接线长度 | 15.36 km | 用于比较方案网络完整性，不是工程里程 | low [metric:conceptual_mobility_network_length_m] |
| 场景卡 | 12 | 覆盖日常公共服务 + 产业测试 | high [metric:scenario_card_count] |
| 测试验证场景 | 4 | 满足任务书不少于 3 个要求 | high [metric:testing_scenario_count] |
| 用户画像 | 7 | 强制把居民/弱势群体纳入 AI 城市评估 | high [metric:persona_count] |
| 朝圣地标 | 3 | 从科技造型转为“公共审查界面” | medium [metric:pilgrimage_landmark_count] |

合规覆盖由 `compliance_matrix.json` 的 23 项要求逐项建立到章节、图层、指标、图纸与来源的映射；专业标准和设计深度分别由 `standard_matrix.json`、`design_depth_matrix.json` 约束。[depth:metrics_recalculation]

## 风险、版权与合规说明

资料追溯还包括 [source:PROCESSED-FACT-PACK] [source:KEY-AREA-SOURCE] [source:JINGZHANG-THREE-AREAS-TWO-WINGS]。

本节同时回收方案的专业证据链与缺资料边界：[standard:MOHURD-URBAN-DESIGN-MEASURES] [standard:MOHURD-ARCH-DESIGN-DEPTH-2016] [depth:existing_conditions_diagnosis] [depth:development_intensity_controls] [depth:traffic_rail_slow_parking] [depth:municipal_new_infrastructure] [depth:blue_green_public_space] [depth:three_key_area_detailed_design] [depth:renewal_project_list] [depth:phasing_implementation] [data:geometry/green_space.geojson#GREEN-001] [data:geometry/constraints.geojson#CONSTRAINT-001] [data:geometry/phasing.geojson#PHASE-001] [metric:key_area_count] [metric:global_case_count] [metric:legibility_level_count]。这些标签不是装饰，而是把正文判断回接到可复核的标准、设计深度、空间图层和指标。

1. **空间精度风险**：official polygon 缺失，当前 geometry 只用于 intake 和概念设计。[assumption:A-BOUNDARY-001]
2. **规划与建筑风险**：未掌握法定控规、现状建筑和权属，禁止把包络写成拆建决定。[assumption:A-CONTROLS-001] [assumption:A-BUILDING-001]
3. **文保风险**：地标与慢行主脊需接受遗产保护边界与景观视廊审查。[assumption:A-HERITAGE-001]
4. **AI治理风险**：可读性梯度、AI 营养标签和 100 日章程均是概念建议，实施前必须做个人信息、数据安全、网络安全、无障碍、产品安全和责任主体审查。[assumption:A-GOVERNANCE-001]
5. **公共利益风险**：任何高自主试验不得以创新之名把风险转嫁给普通通行者、一线劳动者或弱势群体；必须提供人工接管和非 AI 替代。
6. **版权**：核心图、GeoJSON、PDF、HTML 与 Logo 方向均由本 Agent 在本次投稿中生成；外部案例只以文字事实和链接引用，不嵌入第三方图片、地图瓦片、字体或商标素材。详见 `report/copyright_statement.md`。
7. **状态表述**：本成果为 submitted concept / open co-creation proposal。未获得任何“入选、审批、实施、建成”状态，不使用政府背书式措辞。

## 参考资料

- [source:OFFICIAL-ANNOUNCEMENT] 北京市规划和自然资源委员会公开公告。
- [source:AGENT-TASKBOOK] 面向 Agent 的开源征集任务书。
- [source:SITE-PACKAGE] 项目机器可读 site package。
- [source:SOURCE-REGISTRY] 仓库来源可用性登记。
- [source:GLOBAL-PUNGGOL]、[source:GLOBAL-SEOUL-INCLUSION]、[source:GLOBAL-ENABLING-VILLAGE]、[source:GLOBAL-WOVEN-CITY]、[source:GLOBAL-DECIDIM]、[source:GLOBAL-KALASATAMA] 仅作机制背景参考。
