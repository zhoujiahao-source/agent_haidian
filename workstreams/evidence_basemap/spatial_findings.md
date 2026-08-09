# Spatial Findings — 可验证空间问题与机会

以下按“证据 → 诊断 → 设计接口”表达。诊断不是法定结论；涉及未公开 GIS 的位置精度保持 Unknown/Derived。

| id | finding | evidence / confidence | opportunity or constraint | integration interface |
|---|---|---|---|---|
| SF-01 | 京张铁路遗址公园是南北约9 km的连续公共空间框架，源于铁路入地后的线性释放空间。 | SRC-BJ-JZPARK-20240920 + SRC-BJ-JZPARK-20211216 / High | **Opportunity:** Capability Backbone 可以借用真实公共空间连续性，而非虚构新轴线。 | 把主轴表达为能力交换/公共接口层；保留遗产与日常公园优先级。 |
| SF-02 | 官方规划回顾明确指出旧铁路线造成东西向分割，“弥合东西交通联系”是遗址公园的重要目标。 | SRC-BJ-JZPARK-20211216 / High | **Constraint + Opportunity:** 东西缝合是已存在的城市问题，不是本方案发明的口号。 | 下一轮应测量每个现状穿越点、绕行、无障碍、夜间安全，而不是只画箭头。 |
| SF-03 | 京张公园一期已形成公共活动、雨洪/绿地和智慧体验的复合公共空间先例。 | official park opening / High | **Opportunity:** AI公共能力应嵌入公园日常服务，避免独立展馆。 | Public Capability Interface 优先叠加真实入口/活动/休憩/无障碍节点。 |
| SF-04 | 众智园更新片区同时面对低效产业空间、配套、市政与生态资源；清河/小月河被明确列为资源。 | SRC-BJ-CITYUPDATE-ZZY-20260713 / High | **Opportunity:** 技术验证可与存量更新、蓝绿韧性联动。 **Constraint:** 不能假设可任意新建。 | 先做 retain/renovate potential survey，再决定测试空间。 |
| SF-05 | AI原点社区拥有密集高校科研/人才/创业服务的公开证据，但统计边界大于赛事重点区。 | SRC-BJ-AIORIGIN-20260105 + SRC-BJ-AIORIGIN-20260324 / Medium-High | **Opportunity:** 最适合验证社会反馈、人才社区和公共服务学习。 **Constraint:** 不可伪造精确资源热力。 | 建立真实POI/入口/开放时间/服务容量表后，再画可达性。 |
| SF-06 | 大钟寺更新类型横跨住宅、厂房、楼宇、商业、公共空间和基础设施。 | SRC-BJ-CITYUPDATE-DZS-20260713 / High | **Constraint:** 单一产业园式设计会忽略真实居民与更新成本。 **Opportunity:** 市场/AI-native服务可在复合更新中验证。 | 场景卡必须绑定既有使用者、替代路径、噪声/物流/交通和运营时段。 |
| SF-07 | 2026小月河滨水空间工程正在推进，治理段/慢行/绿化具有可核验工程信息。 | current Haidian Water + Beijing public resources / High | **Constraint:** 施工、水务、生态与安全优先。 **Opportunity:** 完工后可形成连续、可观察的低风险公共场景测试带。 | Integration 时把“在建/计划/已建”分层，不把计划长度当现状完成长度。 |
| SF-08 | 中关村科技服务翼的功能角色有官方支持，但精确边界与机构全量空间分布缺失。 | SRC-BJ-KW-THREE-WINGS-20260403 / High for role; Unknown geometry | **Constraint:** 不得画假精确IP/资本服务聚集面。 | 先以“服务网络/候选机构点”表达，取得地址与边界后再做服务覆盖。 |
| SF-09 | 赛事 SITE_BOUNDARY/KEY_AREA 官方 polygon 仍缺失，仓库只提供 provisional rough polygons。 | SRC-REG-PROVISIONAL-BOUNDARY + upstream geometry audit / High | **Hard constraint:** 所有边界派生面积/相交/比例只能 intake-grade。 | official geometry 到达后必须全量 rerun maps, metrics, intersections and legends。 |
| SF-10 | FAR、高度、密度、绿地率、退界等正式控制仍为 missing。 | `planning_limits.json` / High | **Hard constraint:** 不能从 schema bounds、新闻、影像或参考面积倒推出开发强度。 | 设计 Agent 只能提出类型/机制/敏感性区间，法定强度保留 Unknown。 |
| SF-11 | 现有 submission 的建筑、道路、绿地、公共空间多为概念性几何/低置信度指标。 | existing metrics + assumptions / High | **Risk:** downstream visual may mistake conceptual envelopes for existing basemap. | Integration 必须显著区分 Existing/Estimated/Proposed，并优先替换概念现状层。 |
| SF-12 | 京张公园历史本身已存在“政府组织—专家—部门—公众参与”的共创实践。 | SRC-BJ-JZPARK-20211216 / High | **Opportunity:** Public Stewardship 有本地治理先例可连接。 | 城市学习大会/版本发布可建立在已有公众参与传统上，而非纯软件隐喻。 |

## 对设计影响最大的 10 项（优先级）

**P0 hard constraints:** SF-09 official geometry gap; SF-10 statutory controls gap.  
**P1 spatial structure:** SF-01 north-south public spine; SF-02 east-west seams; SF-07 Xiaoyuehe active blue-green construction.  
**P1 differentiated learning units:** SF-04 Zhongzhiyuan renewal/ecology; SF-05 Origin talent/research/services; SF-06 Dazhongsi mixed renewal/market; SF-08 service-wing geometry gap.  
**P2 governance/history:** SF-12 existing co-creation precedent.

These ten should be visible in future maps/boards, with uncertainty labels rather than hidden in appendix notes.
