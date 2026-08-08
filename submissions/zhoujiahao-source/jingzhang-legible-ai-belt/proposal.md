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
> 本方案为 AI Agent 生成的开放共创建议，不构成政府审定结论、法定规划、投资承诺、工程许可或施工依据。精确边界、控规指标、道路红线、权属、市政、消防、文保、结构和实施主体必须在取得官方或经授权资料后由专业团队复核。[source:AGENT-TASKBOOK] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]

## 设计依据与资料清单

本方案以当前仓库 `brief/site-package/`、任务书、公开公告、公共 source registry 和可追溯公开资料为主控输入。[source:SITE-PACKAGE] [source:SOURCE-REGISTRY] [source:PROCESSED-FACT-PACK] [source:OFFICIAL-ANNOUNCEMENT] [source:AGENT-TASKBOOK] [source:JINGZHANG-THREE-AREAS-TWO-WINGS]

当前提交中的 SITE_BOUNDARY 与 KEY_AREA 仍来自仓库 provisional rough geometry，因此只承担开放征集阶段的研究约束，不是官方红线、权属或法定控规边界。[source:BOUNDARY-SOURCE] [source:KEY-AREA-SOURCE] [data:geometry/site_boundary.geojson#SITE-001] [data:geometry/key_areas.geojson#KEY-001] [data:geometry/constraints.geojson#CONSTRAINT-PROV-SITE] [assumption:A-BOUNDARY-001] [assumption:A-KEY-AREA-001] [depth:existing_conditions_diagnosis] [depth:risk_missing_data]

本方案采用两套同时可见的不确定性语言：数据证据等级为 **Official / Verified / Derived / Assumed / Unknown**；图纸状态为 **Known / Estimated / Proposed / Unknown**。成功找到一条公开数据并不自动使其成为 Verified，更不使其成为 Official。[assumption:A-EVIDENCE-001]

![](assets/figures/site-overview.png)

## 三层范围工作框架

| 层级 | 任务文本参考尺度 | 本方案关注 | 数据边界 |
| --- | ---: | --- | --- |
| 统筹研究范围 | 约 43.6 km² | AI生态、文化、区域协同 | 文本范围，不据此创造精确 GIS |
| 总体设计范围 | 约 11.4 km² | 空间结构、公共空间、连接与更新 | 当前 polygon 为 provisional |
| 三处重点区域 | 约 368.4 ha | 可感知详细设计、场景与节点 | 三处 polygon 仍为 provisional |

任务文本给出的三处重点区参考面积为：众智园约 192.1 ha、北京 AI 原点社区约 104.3 ha、大钟寺约 72.0 ha；这些数值与当前 provisional polygon 的复算必须分开表达。[metric:key_area_count] [metric:key_area_reference_total_sqm] [metric:key_area_zhongzhiyuan_reference_sqm] [metric:key_area_ai_origin_reference_sqm] [metric:key_area_dazhongsi_reference_sqm] [depth:three_level_scope_framework]

官方固定的三条定位——**百年京张文化带、都市 AI 生活体验带、AI 融合创新带**——以及五项功能——**AI 全栈自主创新体系、世界级 AI 创新生态、AI+ 场景赋能新范式、智能化 AI 活力城市、AI 治理全球话语权**——均作为方案必须闭环回应的目标，不被新概念替换。[source:AGENT-TASKBOOK]

![](assets/figures/land-use-structure.png)

## 统筹研究范围产业与未来城市研究

### 城市操作系统：从“部署 AI”转向“产生公共价值”

项目核心不是增加 AI 设备，而是让城市获得一种新的公共能力：**持续学习**。城市能够诊断问题、允许有边界的试验、评估真实公共价值、修改或停止无效系统，再将已验证能力交换到其他片区。

统一学习循环为：

**诊断 → Eligible Issue Gate → 风险授权 → 基线与非 AI 对照 → Bounded Test → 公共价值评审 → STOP / MODIFY / CONTINUE / SCALE → TRANSFER / RETIRE → Annual City Version Release。**

“Legible AI / 可读 AI”保留为治理和信息设计原则：影响公共生活的智能系统必须说明其状态、责任、数据边界、人工替代和退出方式，但不再作为方案总概念。

### 六个全球生态案例的机制转译（agent.2）

| 案例 | 可学习机制 | 京张转译 | 不照搬 |
| --- | --- | --- | --- |
| Punggol Digital District | living lab、产学协同、区域数字平台 | 能力从实验室进入真实区域验证 | 不承诺同规模平台或投资 [source:GLOBAL-PUNGGOL] |
| Seoul Digital Inclusion | 老年支持、辅助访问、社区数字教育 | 公共服务保留人工与非 AI 等价路径 | 不移植其绩效值 [source:GLOBAL-SEOUL-INCLUSION] |
| Enabling Village | 通用设计、辅助技术、包容服务 | PCI 把可达性作为基础设施 | 不复制机构治理 [source:GLOBAL-ENABLING-VILLAGE] |
| Toyota Woven City | 真实环境共创测试 | 众智园设置受控测试与回退 | 公共城市不能默认同意 [source:GLOBAL-WOVEN-CITY] |
| Decidim Barcelona | 开源、可追踪公众参与 | 问题、变更、STOP、申诉留痕 | 不把平台参与当正式授权 [source:GLOBAL-DECIDIM] |
| Kalasatama | 混合生活、公共交通、滨水连续 | AI 场景进入普通通勤与公共空间 | 不复制规划指标 [source:GLOBAL-KALASATAMA] |

京张的差异化不是“更智能”，而是把**公共价值、能力交换、风险授权、失败公开和技术退役**同时写入城市设计。

## 总体设计范围城市更新与控规深度城市设计

### 一条 Capability Backbone + 五个 Learning Units

总体结构为一条 **Capability Backbone / 城市能力交换骨干**，连接五个按真实资源禀赋分工的学习单元。[metric:capability_backbone_layer_count] [depth:overall_spatial_structure] [standard:MOHURD-URBAN-DESIGN-MEASURES]

Capability Backbone 由六层叠加：
1. 历史记忆层：铁路轨迹、旧站、材料和里程标；
2. 慢行与可达层：步行、骑行、无障碍与轨道接驳；
3. 公共空间层：日常停留、儿童、老人、夜间与应急；
4. 蓝绿生态层：遮阴、热舒适、雨洪和滨水连续；
5. 能力节点层：调用、测试、交换、状态披露与人工接管；
6. 事件运营层：季度试验、版本发布、文化与开发者活动。

五个学习单元采用“主能力 + 次能力”，没有唯一中央发动机：
- **众智园**：技术生产与高风险验证；2026 年公开城市更新信息只作为当前背景，不替代比赛 KEY_AREA。[source:SRC-BJ-CITYUPDATE-ZZY-20260713]
- **北京 AI 原点社区**：社会学习、人才日常与公共服务；公开人才服务设施可证明公共服务属性，不支持覆盖率推断。[source:SRC-BJ-AIORIGIN-TALENT-20260720]
- **大钟寺**：市场与 AI-native 服务验证；更新与道路微循环信息只作现状背景，不是道路红线。[source:SRC-BJ-CITYUPDATE-DZS-20260713] [source:SRC-BJ-DZS-ROAD-20260225]
- **中关村科技服务翼**：IP、资本、法律、标准、产业服务和国际资源交换。
- **小月河场景赋能翼**：高温、雨洪、慢行与蓝绿公共生活测试；当前建设与管线信息意味着任何试验先核验工程和生态条件。[source:SRC-BJ-XIAOYUEHE-WATER-20260112] [source:SRC-BJ-XIAOYUEHE-WORKS-20260121]

现有 `ROAD-001` 仅作为连续关系的设计研究载体，东西向线条不被解释为已经核验的桥、隧道、道路或法定通道。[data:geometry/roads.geojson#ROAD-001] [assumption:A-ROAD-001]

### 永久 / 适应 / 实验三层

- **Permanent Infrastructure**：普通步行、树荫、无障碍、照明、传统公共服务、消防和市政等非 AI 基线；
- **Adaptive Layer**：可更换标识、模块家具、服务点、季节活动与可升级接口；
- **Experimental Layer**：明确时间、空间边界、非参与者旁路、人工停机和撤除条件的试验。

即使 AI 离线，基本公共服务与普通公共空间仍必须可用。[assumption:A-NONAI-001]

![](assets/figures/key-areas.png)

## AI 创新生态、人才画像与 AI+ 场景

### Public Capability Interface

公共空间不是 AI 展厅，而是 **Public Capability Interface / 公共能力接口**。每个接口至少包含：Non-AI Baseline、Ambient Layer、Consent Layer、Human Override、Failure-Safe Mode、Public Learning Record。

节点库采用八类，不要求机械铺满：Backbone Exchange Hub、District Learning Node、Neighborhood Interface、Blue-Green Capability Node、Test & Validation Node、Market & Service Node、Memory & Archive Node、Emergency / Human Override Node。[metric:public_capability_node_type_count]

### 八类 Persona

1. AI 研究者 / 创业者；
2. 高校学生 / 开发者；
3. 周边居民与家庭；
4. 老年人；
5. 残障、低视力与听障用户；
6. 骑手、保洁、安保及现场运营者；
7. 商户 / 服务运营者；
8. 国际访问者 / 产业伙伴。[metric:persona_count]

### 12 张场景卡

| # | 场景 | 主要空间 | 风险/类型 | 非 AI 基线与人工接管 | 评价重点 |
| --- | --- | --- | --- | --- | --- |
| S01 | 京张铁路文化解释与路线 | 主轴/记忆节点 | Low | 实体导视、人工讲解 | 准确性、可达性 |
| S02 | 无障碍路线辅助 | 全带慢行网 | Low | 标准无障碍导视、人工咨询 | 绕行、失败率 |
| S03 | 老年公共服务导航 | AI 原点社区 | Low | 人工服务台、电话、实体窗口 | 完成率、接管 |
| S04 | 夜间安全回程协助 | 轨道—社区节点 | Medium | 普通照明、保安、公共交通信息 | 误报、投诉 |
| S05 | 高温避暑节点编排 | 公园/小月河 | Low-Medium | 树荫、饮水、普通开放空间 | 热舒适、弱势覆盖 |
| S06 | 社区活动与空间编排 | AI 原点/社区 | Low | 人工排期、公告栏 | 使用多样性、公平 |
| S07 | AI-native 商业服务验证 | 大钟寺 | Medium | 普通人工消费/咨询 | 等待、成本、投诉 |
| S08 | **机器人末端配送测试** | 众智园受控空间 | **High / testing_and_validation** | 人工配送、旁路、停机 | near miss、接管 |
| S09 | **低速自动移动载具测试** | 众智园指定测试段 | **High / testing_and_validation** | 步行/人工接驳、旁路 | 安全、接管 |
| S10 | **边缘算力—能源协同测试** | 众智园设施节点 | **Medium-High / testing_and_validation** | 常规设施控制 | 能耗、故障、回退 |
| S11 | **热/雨洪环境响应测试** | 小月河蓝绿节点 | **Medium / testing_and_validation** | 普通市政/园林操作 | 环境改善、副作用 |
| S12 | 公众提案摘要与进度追踪 | 线上线下接口 | Low | 原文公开、人工受理 | 可追溯、申诉 |

每个场景记录问题来源、非 AI 对照、数据来源、风险等级、试验边界、持续时间、人工责任人、退出方式、基线、指标、事故和最终状态。[metric:scenario_card_count] [metric:testing_scenario_count] [assumption:A-GOVERNANCE-001]

## 用地、建筑规模与拆改留方案

`land_use.geojson` 是总体功能结构的概念表达，不构成法定用地调整。[data:geometry/land_use.geojson#LU-001] [depth:land_use_layout] [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]

`buildings.geojson` 中的 6 个包络只表达研发、服务、档案、测试和公共接口可能需要的空间类型，不代表现状建筑或确认的新建规模。在没有完整现状测绘、权属、文保、结构、碳排和运营评价前，不作具体拆除结论。[data:geometry/buildings.geojson#BLDG-11] [metric:building_footprint_area_sqm] [metric:building_density_ratio] [assumption:A-BUILDING-001] [depth:retain_renovate_demolish] [standard:MOHURD-ARCH-DESIGN-DEPTH-2016]

总建筑面积、FAR、建筑高度、法定建筑密度、绿地率和退界保持 Unknown，不使用 schema 的 sanity range 冒充审批值。[metric:total_floor_area_sqm] [metric:floor_area_ratio] [depth:development_intensity_controls] [standard:MOHURD-CONTROL-DETAILED-PLANNING]

## 交通、轨道、市政与公共服务设施

交通优先级为：**普通步行 / 骑行 / 无障碍与轨道接驳 > 公共空间品质 > AI 辅助 > 自动化设备**。[depth:traffic_rail_slow_parking]

现有概念网络长度只用于比较设计关系，不是工程里程。[metric:conceptual_mobility_network_length_m]。当前没有可用于面积计算的核实道路红线，因此 road area 保持 Unknown。[metric:road_area_ratio]

机器人和自动移动设备只允许在证据、工程与安全条件满足后的受控测试区运行。边缘算力、充电、网络、传感器、主动降温等新型基础设施必须与传统市政检修、消防、配电、排水和防洪一起深化。[assumption:A-MUNICIPAL-001] [depth:municipal_new_infrastructure]

公共服务必须提供与服务性质相匹配的人工或非 AI 路径；缺少智能手机、账号、语言能力，或退出数据处理，不应导致失去基本公共服务。[assumption:A-NONAI-001]

![](assets/figures/mobility-bluegreen.png)

## 蓝绿空间、公共空间与城市风貌

现有 `green_space.geojson` 是设计提议，不是现状或法定绿地边界；当前概念绿地比率也不是法定绿地率。[data:geometry/green_space.geojson#GREEN-001] [metric:green_ratio] [depth:blue_green_public_space]

北京市公开公园信息支持京张铁路遗址公园作为公共空间与遗产载体，但不提供本征集的 official GIS boundary。[source:SRC-BJ-JZPARK-CATALOG-20250724]

### Landmark as Memory：1909 → 2026 → Future → Retired

1. **1909 Railway Memory Ground / 铁路记忆地**：实体轨迹、材料、遗构与历史解释；
2. **2026 City Learning Archive / 城市学习档案**：公开成功、MODIFY、STOP、投诉、事故和公共价值结果；
3. **Future Open Test Station / 未来开放实验站**：容纳仍无答案、可撤除、可旁路、可停机的测试；
4. **Retired Capability Archive / 城市能力退役档案**：保存重要退役能力的版本、贡献、失败、数据清理和替代关系。

前三项构成至少 3 个 AI 地标/荣誉节点，第四项补足退出制度。[data:geometry/public_space.geojson#PUBLIC-001] [metric:pilgrimage_landmark_count] [metric:retired_capability_archive_count] [metric:public_space_ratio] [assumption:A-PUBLIC-001] [depth:three_key_area_detailed_design]

风貌采用 **Public Service Aesthetic**：清楚、可信、友好、低眩光。视觉 DNA 来自双轨、站点、道岔、里程标，Logo 核心为 **Open Node**；拒绝赛博朋克、霓虹科技城、巨型 AI 屏幕和通用芯片/大脑图标。[depth:height_massing_character]

## 更新项目清单、实施政策与分期计划

City OS 的实施不以一次性“建成”为目标，而采用 **Permanent / Adaptive / Experimental** 组件级演进。[depth:renewal_project_list] [depth:phasing_implementation]

现有 `phasing.geojson` 三块大范围 polygon 仍是早期概念载体，不应被读成政府建设时序；最终建议逐步替换为组件级 `implementation_layer / delivery_phase / reversibility / evidence_status` 属性。[data:geometry/phasing.geojson#PHASE-001] [metric:phase_area_sqm]

### Public Stewardship

公共机构承担规则、风险授权、数据治理、公共价值判断、事故响应和最终 STOP / SCALE / RETIRE 责任；高校、科研机构、企业、开发者、社区和市民参与问题提出、开发、测试、审查和反馈。任何具体真实机构名称目前都不是已确认承诺。[assumption:A-INSTITUTION-001]

能力进入系统有双入口：
- **Problem Track**：City Agent / 公共机构发现问题 → 人工确认 → 城市挑战 → 社会解决；
- **Capability Track**：社会提出能力 → 证明真实公共需求、非 AI 对照、可逆、可维护与退出 → 测试。

### Annual City Version Release

城市全年持续迭代，每年举行 **Jing-Zhang City Learning Assembly / 京张城市学习大会**，发布 `Jing-Zhang City v20XX`：
Added / Modified / Scaled / Responsible STOP / Retired / Suspended / Unresolved / Metric & Audit Changes。

长期建立 **Capability Registry** 与 **Retired Capability Archive**，让模型、机器人、云平台和厂商可以更换，而公共责任、证据、版本、迁移与退出机制长期存在。

## 指标体系、面积复算与合规矩阵

旗舰指标为 **Urban Adaptation Rate / 城市适应率**：在预先锁定的合格问题 cohort 中，到评价时点真正实现可验证公共价值改善的问题比例。

`UAR_h = verified_improved_problem_records_at_h / evaluable_qualified_problem_records_at_h`

建议同时报告 UAR-90 与 UAR-365，但目前没有真实运行的 eligible issue / experiment / outcome registry，所以值必须保持 Unknown/null。[metric:urban_adaptation_rate_90d] [metric:urban_adaptation_rate_365d] [assumption:A-UAR-001]

**Responsible STOP** 是负责任的学习结果，但不自动算作问题已改善，不虚增 UAR。[metric:responsible_stop_rate]

统一公共价值底线至少包括 Safety、Equity、Privacy、Environment、Cost，并同时检查 Accessibility、Human Override 与 Non-AI parity。[metric:public_value_floor_pass_rate] [metric:human_override_success_rate]

跨区能力交换必须重新验证目标区域人群、空间、运营、数据和风险，不因源区域 SCALE 就自动部署。[metric:capability_transfer_revalidation_rate]

### 当前可复算 / 可核对指标

| 指标 | 当前值或状态 | 解释 |
| --- | --- | --- |
| provisional 总体设计面积 | 约 11.413 km² | 当前 rough polygon，仅研究用 [metric:site_area_sqm] |
| 三处重点区数量 | 3 | 任务固定 [metric:key_area_count] |
| 重点区文本参考总面积 | 368.4 ha | 与 provisional polygon 分开 [metric:key_area_reference_total_sqm] |
| 众智园文本参考面积 | 192.1 ha | 官方任务文本参考 [metric:key_area_zhongzhiyuan_reference_sqm] |
| AI 原点文本参考面积 | 104.3 ha | 官方任务文本参考 [metric:key_area_ai_origin_reference_sqm] |
| 大钟寺文本参考面积 | 72.0 ha | 官方任务文本参考 [metric:key_area_dazhongsi_reference_sqm] |
| 概念建筑包络面积 | 97,492.376 sqm | 非现状建筑量 [metric:building_footprint_area_sqm] |
| 概念建筑密度 | 0.854% | 非法定建筑密度 [metric:building_density_ratio] |
| 概念绿地比例 | 28.1% | 非法定绿地率 [metric:green_ratio] |
| 概念公共节点面积比例 | 0.38% | 非全部公共空间 [metric:public_space_ratio] |
| 概念连接网络 | 15.36 km | 非工程里程 [metric:conceptual_mobility_network_length_m] |
| Persona | 8 | [metric:persona_count] |
| 场景 | 12 | [metric:scenario_card_count] |
| testing / validation | 4 | [metric:testing_scenario_count] |
| 主要地标 | 3 | [metric:pilgrimage_landmark_count] |
| 退役档案系统 | 1 | [metric:retired_capability_archive_count] |
| 全球案例 | 6 | [metric:global_case_count] |
| Backbone 层数 | 6 | [metric:capability_backbone_layer_count] |
| PCI 节点类型 | 8 | [metric:public_capability_node_type_count] |

每一次 official geometry / controls 更新，都必须从 geometry 重新计算 metrics，并同步 proposal、figures、matrices、manifest、HTML 和 PDF，不允许手工只改一个表格。[depth:metrics_recalculation]

![](assets/figures/metrics-evidence.png)

## 风险、版权与合规说明

### 当前主要 Unknown

- exact official SITE_BOUNDARY / KEY_AREA polygons；
- FAR、总建筑面积、建筑高度、法定密度、绿地率、退界和道路红线；
- 完整建筑现状、权属、文保 GIS；
- 地下市政、消防、结构、排水、防洪和配电；
- 未来 Public Steward 的真实机构、预算、人员和法定授权；
- 所有 AI 城市能力的真实运营绩效。

### 设计红线

不允许把 provisional geometry 称为官方红线；不允许把概念包络写成已确定拆建；不允许 AI 默认替代人工公共服务；不允许高风险测试强迫普通通行者参与；不允许用平均效率掩盖弱势群体、事故、投诉和人工干预；不允许因为沉没成本拒绝 STOP/RETIRE；不允许把未来合作主体写成已经承诺参与。

版权与数据方面，只使用公开、用户许可或仓库允许的资料；OSM/Overpass 候选数据遵循 ODbL attribution，[source:SRC-OSM-OVERPASS-LIVE]；Microsoft Global ML Building Footprints 只作为 Derived 建筑候选并保留 CDLA-Permissive-2.0 条件，[source:SRC-MS-GLOBAL-BUILDINGS-20260724]；不把商业地图瓦片作为 submission 数据。

本方案以概念城市设计深度回应开放征集，不替代后续建筑、工程、市政、交通、文保和法定规划设计文件。[standard:MOHURD-URBAN-DESIGN-MEASURES] [standard:MOHURD-ARCH-DESIGN-DEPTH-2016]

## 参考资料

- 项目官方公告、任务书、site package、source registry 与本地专业标准快照。[source:OFFICIAL-ANNOUNCEMENT] [source:AGENT-TASKBOOK] [source:SITE-PACKAGE] [source:SOURCE-REGISTRY]
- 三区两翼公开背景。[source:JINGZHANG-THREE-AREAS-TWO-WINGS]
- 众智园、大钟寺、AI 原点社区和小月河 2026 年公开背景资料。[source:SRC-BJ-CITYUPDATE-ZZY-20260713] [source:SRC-BJ-CITYUPDATE-DZS-20260713] [source:SRC-BJ-AIORIGIN-TALENT-20260720] [source:SRC-BJ-DZS-ROAD-20260225] [source:SRC-BJ-XIAOYUEHE-WATER-20260112] [source:SRC-BJ-XIAOYUEHE-WORKS-20260121]
- 京张铁路遗址公园公开资料。[source:SRC-BJ-JZPARK-CATALOG-20250724]
- 六个全球案例仅作机制背景，不转移规划指标或绩效承诺。[source:GLOBAL-PUNGGOL] [source:GLOBAL-SEOUL-INCLUSION] [source:GLOBAL-ENABLING-VILLAGE] [source:GLOBAL-WOVEN-CITY] [source:GLOBAL-DECIDIM] [source:GLOBAL-KALASATAMA]

## 结论：二十年后留下城市能力交换网络

1909 年京张铁路把工程自主能力写进真实城市；今天不需要用某一代 AI 技术复制一个纪念物。真正值得留下的是一套城市公共能力：

**发现真实问题 → 谨慎授权 → 可逆试验 → 公开失败 → 验证公共价值 → 通过 Capability Backbone 交换 → 目标区重新验证 → 版本发布 → 退役与记忆。**

最终长期遗产是 **Urban Capability Exchange Network / 城市能力交换网络**。即使今天的大模型、机器人、云平台和传感器在二十年后全部过时，只要这套网络仍能让普通人安全、平等、可选择地获得公共服务，京张就仍然是一座会学习的城市。
