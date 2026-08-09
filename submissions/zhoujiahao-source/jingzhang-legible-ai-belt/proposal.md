---
title: "京张·城市能力交换带 / Jing-Zhang Urban Capability Exchange"
author_github: "zhoujiahao-source"
language: "zh"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_file: "proposal.en.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "把百年京张建设为一套让城市持续发现问题、可逆试验、评估公共价值、交换能力并主动退役失效技术的城市级操作系统；以 Capability Backbone 连接三区两翼，以 Public Capability Interface 服务日常公共生活，以 Urban Adaptation Rate 衡量真实改善，以年度 City Version Release 形成长期公共治理与城市记忆。"
tracks: ["civic-agent-governance", "ai-traffic-walkability", "enterprise-services-ecosystem"]
scenarios: ["public-safety-operations-review", "ai-traffic-walkability", "enterprise-service-copilot"]
iteration: "v2.0.0"
---

# 京张·城市能力交换带

> **一句话主张：京张不是一座“装满 AI”的城市，而是一套让城市不断产生、交换、检验、升级和退役公共能力的城市操作系统。**

本方案为 AI Agent 生成的开放共创建议；最终判断、专业深化与法定程序由人类和专业机构完成。

## 设计依据与资料清单

本方案把百年京张定义为一套**城市级公共能力操作系统**：AI 不以设备数量进入城市，而是通过问题诊断、风险授权、可逆试验、公共价值评审、能力交换和技术退役，转化为可被城市长期治理的公共能力。三大定位、五大功能、三区两翼保持为官方任务书的固定目标，本方案只提出实现它们的空间与治理机制。[source:AGENT-TASKBOOK] [source:OFFICIAL-ANNOUNCEMENT]

当前 SITE_BOUNDARY 与三处 KEY_AREA 仍为临时约束范围。所有空间图件把 **Official / Verified / Derived / Assumed / Unknown** 与 **Known / Estimated / Proposed / Unknown** 分开表达；官方精确 polygon、控规、权属、道路红线、文保、市政和完整现状建筑数据到位后必须重算。[source:BOUNDARY-SOURCE] [assumption:A-BOUNDARY-001]

## 三层范围工作框架

约 43.6 km² 统筹研究范围负责 AI 生态、区域协同与未来城市机制；约 11.4 km² 总体设计范围负责空间结构、公共空间、更新与连接；众智园、AI 原点社区、大钟寺三处重点区负责可感知的详细设计。比赛文本中的 192.1/104.3/72.0 ha 是参考面积，不等同于当前临时 polygon 的精确 GIS 面积。[metric:key_area_reference_total_sqm] [assumption:A-KEY-AREA-001]

总体空间语法为 **一条 Capability Backbone + 五个差异化 Learning Units**，没有唯一中央发动机。骨干不是一条新路，而是历史记忆、慢行可达、公共空间、蓝绿生态、能力节点和事件运营六层叠加的公共城市结构。[metric:capability_backbone_layer_count] [data:geometry/roads.geojson#ROAD-001]

## 统筹研究范围产业与未来城市研究

五个学习单元按真实资源禀赋分工：众智园主技术生产与高风险验证；AI 原点主社会学习、人才日常与公共服务；大钟寺主市场与 AI-native 服务验证；中关村科技服务翼主 IP、资本、法律、标准和国际资源交换；小月河场景赋能翼主蓝绿公共生活与低风险真实城市测试。当前公开更新与公共服务资料只支撑这种**角色方向**，不支撑把更大产业叙事直接投影为比赛精确边界。[source:SRC-BJ-CITYUPDATE-ZZY-20260713] [source:SRC-BJ-AIORIGIN-TALENT-20260720] [source:SRC-BJ-CITYUPDATE-DZS-20260713]

六个全球案例用于机制转译而非形式复制：Punggol 的 living lab、Seoul 的数字包容、Enabling Village 的通用设计、Woven City 的真实测试、Decidim 的可追踪参与、Kalasatama 的日常混合城市。京张的差异不是“更智能”，而是把失败公开、人工替代、风险授权、能力迁移与退役同时写入城市设计。[source:GLOBAL-PUNGGOL] [source:GLOBAL-DECIDIM] [source:GLOBAL-KALASATAMA]


区域协同不是“机构名单”，而是一套**能力交换接口**：京张可以与中关村、未来科学城、怀柔科学城、经开区及更广义京津冀高校/科研/产业网络交换经过验证的城市能力、测试协议、证据与人才服务，但每一次跨区迁移都必须重新做目标情境验证；本方案不声称任何外部机构已经签署合作或资源承诺。[source:AGENT-TASKBOOK]

## 总体设计范围城市更新与控规深度城市设计

Capability Backbone 沿百年京张的连续公共空间关系组织，但所有 crossing 与连接先进入 evidence gate：真实道路/铁路/水系/文保/权属未核验时，只画“需要连接的关系”，不画成已确定桥隧或法定通道。[data:geometry/roads.geojson#ROAD-002] [assumption:A-ROAD-001]

城市构造分为 **Permanent / Adaptive / Experimental** 三层。永久层保存普通步行、树荫、无障碍、照明、消防和非 AI 公共服务；适应层承载可更换标识、家具和接口；实验层只允许有时间、空间、旁路、人工停机和撤除条件的 bounded test。即使 AI 离线，基础公共生活仍可继续。[assumption:A-NONAI-001] [data:geometry/phasing.geojson#PHASE-001]

## 重点区域详细设计

**众智园：Verification Campus。** 把技术验证放在可隔离、可观察、可回退的实验庭院与共享测试界面中；普通步行和工作空间不因试验中断。

**AI 原点社区：Learning Neighborhood。** 公共服务、无障碍、人才日常和社区共创优先；AI 默认退到后台，个人化或识别性功能进入 Consent Layer。

**大钟寺：Market & Service Commons。** 用通勤、商业、骑手、居民和游客的真实混合使用验证 AI-native 服务，而不是另建封闭技术园。三处 KEY_AREA 的具体 host 仍需官方 polygon、权属和现状建筑资料确认。[data:geometry/key_areas.geojson#KEY-001] [data:geometry/public_space.geojson#PUBLIC-003] [assumption:A-CONTROLS-001]

## AI 创新生态、人才画像与 AI+ 场景

Public Capability Interface（PCI）是公共空间的六层契约：**Non-AI Baseline / Ambient Layer / Consent Layer / Human Override / Failure-Safe Mode / Public Learning Record**。它不是一类 kiosk；树荫、座椅、通行、人工窗口、应急程序等普通城市设计先成立，AI 只在需要时调用。[metric:public_capability_node_type_count] [data:geometry/public_space.geojson#PUBLIC-001]

八类 Persona：研究者/创业者、高校学生/开发者、周边居民与家庭、老年人、残障/低视力/听障用户、骑手/保洁/安保等现场运营者、商户/服务运营者、国际访问者/产业伙伴。[metric:persona_count]

十二个场景：①铁路文化导览；②无障碍路线；③多语公共服务；④夜间安全回程；⑤开发者机会发现；⑥教育技能辅导；⑦健康服务导航（非诊断）；⑧机器人末端配送 bounded test；⑨低速自治载具 bounded test；⑩边缘算力-能源协同 test；⑪热/雨洪响应；⑫公众提案总结追踪。其中 4 个明确属于测试/验证场景，均需要非参与者旁路、人工停止权和 STOP 条件。[metric:scenario_card_count] [metric:test_validation_scenario_count]

## 用地、建筑规模与拆改留方案

当前用地结构是概念城市设计 mosaic，用来表达科研、教育、社区服务、商业、文化、绿地与可逆留白之间的关系；它不会被描述为法定用地或控规调整。BUILDING_FOOTPRINT 只画少量**拟议可逆公共服务构筑物包络**，不把缺失的现状建筑数据伪造成事实。[data:geometry/land_use.geojson#LU-001] [data:geometry/buildings.geojson#BLDG-001]

因此总建筑面积、FAR、现状楼层/高度、权属与完整拆改留结论保持 Unknown；真实建筑底图应由 OSM、Microsoft ML footprints、官方资料与现场核验交叉后再决定是否进入 Verified。[metric:far] [assumption:A-BASEMAP-001]

## 交通、轨道、市政与公共服务设施

ROAD-001 是连续性研究轴，ROAD-002~006 是东西向 stitch study axes。它们表达“城市需要跨越障碍建立公共联系”的设计任务，而不是假定已经存在的道路、桥、隧或工程红线。大钟寺已公开的道路微循环事实可作为现状背景，但不能外推为整个范围的交通结论。[source:SRC-BJ-DZS-ROAD-20260225] [assumption:A-ROAD-001]

市政、消防、地下管线、排水、防洪、结构与能源容量在现有公开资料中不足。小月河 2026 年水务和管线工程信息说明任何蓝绿/试验节点必须先核验在建工程和水安全条件。[source:SRC-BJ-XIAOYUEHE-WATER-20260112] [source:SRC-BJ-XIAOYUEHE-WORKS-20260121]

## 蓝绿空间、公共空间与城市风貌

公共空间采用“城市优先、AI 退到后台”的 Public Service Aesthetic：铁路的双轨、站点、道岔、里程标被抽象为能力流、开放节点、切换与版本记忆，而不是复古铁路装饰或 cyberpunk AI 视觉。蓝绿结构优先解决树荫、热舒适、雨洪、慢行、儿童/老人使用和应急，再叠加环境感知与调度。[source:SRC-BJ-JZPARK-CATALOG-20250724] [data:geometry/green_space.geojson#GREEN-001]

一天的公共空间被编排为 8AM–MIDNIGHT Adaptive Commons：通勤、午间休息、儿童/老人、夜间文化、市场、极端天气和应急模式共享同一城市底盘，但不同节点承担不同角色。

## 更新项目清单、实施政策与分期计划

实施不再用三块大 polygon 表示“0–12 月/1–3 年/3–5 年”，而是把每个组件标注为 Permanent / Adaptive / Experimental，并绑定 reversibility。推荐节奏：Q1 Diagnose → Q2 Sandbox/Authorize → Q3 Trial/Transfer → Q4 Evidence/Release；年度公开 **City Version Release** 同时发布新增、修改、扩展、Responsible STOP、退役、未解决问题和证据变化。[data:geometry/phasing.geojson#PHASE-001] [assumption:A-INSTITUTION-001]

Public Stewardship 保留最终公共责任：规则、风险授权、数据治理、公共价值判断、事故响应和 STOP/MODIFY/CONTINUE/SCALE/RETIRE 的最终责任不外包给平台或供应商。高校、企业、开发者与市民通过 Problem Track 与 Capability Track 贡献能力。


长期运营至少维护四本资源台账：①非 AI 基线公共服务与普通公共空间；② challenge / sandbox / 小规模试验资源；③维护、人工替代、迁移与退出储备；④独立审计、受影响群体参与和年度版本发布资源。这些都是机制建议，不代表已经存在的政府预算、采购或运营主体。[assumption:A-INSTITUTION-001]

## 指标体系、面积复算与合规矩阵

旗舰指标 **Urban Adaptation Rate (UAR)** 不统计 AI 部署数量，而统计已进入 qualified eligible cohort 的城市问题中，有多少在预注册时间窗内获得可验证公共价值改善。Agent 原始检测不直接进入分母；Responsible STOP 是成功学习/安全结果，但不自动算作问题已适应。[metric:urban_adaptation_rate] [assumption:A-GOV-OPS-001]

公共价值统一底线包括安全、公平、隐私、环境、成本与人工接管；场景另加 2–4 个可测指标。公开 dashboard 同时显示失败、投诉、人工接管、极端值、弱势群体差距和未解决问题，避免“平均数好看”掩盖伤害。几何指标来自当前临时/概念 geometry，因此其数值可复算但专业权威性受数据状态约束。[metric:green_ratio] [metric:public_space_ratio]

## 风险、版权与合规说明

本成果是开放共创建议，不是政府审定、法定规划、投资承诺、工程许可或施工依据。个人信息、自动化决策、算法服务、生成内容、安全和无障碍等真实部署义务必须按未来具体运营主体、数据流、场景和法律事实另行审查；本方案的风险矩阵只是一套城市设计治理接口。[source:AGENT-TASKBOOK] [assumption:A-INSTITUTION-001]

所有生成图、SVG、HTML 与 PDF 为本方案程序化生成；不嵌入第三方照片、商业地图底图、远程字体、追踪脚本或未清权素材。OSM 与 Microsoft 数据源已经登记许可和用法，但由于当前执行环境无法联网完成 materialization，本版本没有把它们伪装为现状 Verified 图层。[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]

## 参考资料

机器可核验的完整来源、许可、时间、用途和限制见 `sources.json`；指标与公式见 `metrics.json`；官方/临时/设计空间状态见 GeoJSON；任务覆盖、专业标准与设计深度分别见三个矩阵。正文只保留与判断直接相邻的少量证据标记，以符合 proposal format v2 的人类可读要求。[source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT]

