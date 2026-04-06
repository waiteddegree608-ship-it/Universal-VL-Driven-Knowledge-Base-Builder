# PDF_Chapter_34

### Page/Slide 1



### 文字与公式提取  
1. **章节标题**  
   - Chapter 34  
   - Information Technology  

2. **正文内容**  
   - **Introduction**：信息技术革新了生产与消费方式；现有经济学工具足以分析信息技术经济问题。  
   - **34.1 (2)**  
     - *背景*：MightySoft公司拟推出操作系统DoorKnobs，其用户价值依赖市场占有率（因文件交换便利性）。  
     - *定义*：  
       - **感知市场份额** $ s $：公众认为使用DoorKnobs的电脑占比。  
       - **实际市场份额** $ x $：价格 $ p $ 时，愿支付 $ p $ 的电脑占比。  
     - *核心关系*：当感知份额为 $ s $、价格为 $ p $ 时，实际份额 $ x $ 满足公式：  
       $$
       p = 256s(1 - x) \tag{1}
       $$  
     - *长期均衡*：长期中感知份额 $ s $ 必须等于实际份额 $ x $（真相显现）。  
     - *问题 (a)*：当 $ s = 1/2 $ 时，绘制价格 $ p $ 与实际份额 $ x $ 的需求曲线。  
     - *问题 (b)*：当 $ s = 1/2 $ 且 $ x = 1/2 $ 时，求价格 $ p $，答案为 **\$64**。  

---

### 核心概念解析（基于网络外部性框架）  
1. **需求端网络外部性**  
   DoorKnobs的价值随用户规模递增，体现为**价格 $ p $ 与感知份额 $ s $ 正相关**（公式中 $ s $ 作为乘数）。消费者支付意愿不仅取决于自身需求，还依赖对“他人是否使用”的预期（$ s $），这是典型**需求侧网络效应**。  

2. **短期 vs 长期动态**  
   - **短期**：企业可通过营销（广告、赠品）人为抬升 $ s $，从而提升当前价格 $ p $（公式 (1) 中 $ s $ 为外生变量）。  
   - **长期**：$ s = x $ 时系统达到均衡（公众信念与实际使用一致），此时公式 (1) 简化为 $ p = 256x(1 - x) $。  

---

### 问题解析  
#### (a) $ s = 1/2 $ 时的需求曲线  
- 代入 $ s = 1/2 $ 到公式 (1)：  
  $$
  p = 256 \cdot \frac{1}{2} \cdot (1 - x) = 128(1 - x)
  $$  
- **曲线特征**：  
  - 线性递减函数，斜率 $-128$。  
  - 当 $ x = 0 $（无人实际使用），价格上限 $ p = 128 $；  
  - 当 $ x = 1 $（全民使用），价格降至 $ p = 0 $。  
- **含义**：短期中，即使实际用户少 ($ x $ 小)，只要公众相信系统流行 ($ s $ 高)，企业仍可设定高价。  

#### (b) $ s = 1/2 $ 且 $ x = 1/2 $ 时的价格  
- 直接代入公式 (1)：  
  $$
  p = 256 \cdot \frac{1}{2} \cdot \left(1 - \frac{1}{2}\right) = 256 \cdot \frac{1}{2} \cdot \frac{1}{2} = 64
  $$  
- **经济逻辑**：当公众 belief（$ s = 1/2 $）与真实需求（$ x = 1/2 $）一致时，市场出清价格为 \$64，体现网络效应下“信念-需求”匹配的均衡点。

---
### Page/Slide 2



### 文字与公式提取  
1. **章节与页码**  
   - 页码：410  
   - 章节：INFORMATION TECHNOLOGY (Ch. 34)  

2. **正文内容**  
   - **(c)** 在同一图表上，为 DoorKnobs 的感知市场份额 $ s $ 取以下值时，绘制并标注单独的需求曲线：$ s = \frac{1}{8}, \frac{1}{4}, \frac{3}{4}, \frac{7}{8}, 1 $。  
   - **(d)** 在感知份额 $ s = \frac{1}{4} $ 的需求曲线上，标记实际份额 $ x = \frac{1}{4} $ 的点（即 $ x $ 轴上对应 $ x = \frac{1}{4} $ 的正上方点）。当感知份额为 $ \frac{1}{4} $ 时，实际份额也为 $ \frac{1}{4} $ 的价格为 **\$48**。  
   - **(e)** 为 $ s = \frac{1}{8}, \frac{3}{4}, \frac{7}{8}, 1 $ 的需求曲线标注红点，显示当感知份额为 $ s $ 时，实际份额恰好等于 $ s $ 的价格。  
   - **(f)** 绘制 DoorKnobs 的长期需求曲线：假设感知份额 $ s $ 等于实际份额 $ x $（即 $ s = x $），则需求曲线为 $ p = 256x(1 - x) $。在图表上绘制关键点并近似画出曲线（需通过所有已标记的红点）。  
   - **(g)** 若 MightySoft 设定价格为 \$48 且保持不变，则存在三种不同的感知市场份额 $ s $，使得实际购买意愿的消费者比例（即实际份额 $ x $）等于 $ s $。  

3. **公式**  
   - 短期需求关系：$ p = 256s(1 - x) $  
   - 长期均衡条件：$ s = x $，代入得 $ p = 256x(1 - x) $  
   - （d）中验证：$ s = \frac{1}{4} $、$ x = \frac{1}{4} $ 时，$ p = 256 \times \frac{1}{4} \times \left(1 - \frac{1}{4}\right) = 48 $  

---

### 图表变化含义解析（结合上文）  
图表展示了 **$ s $ 作为外生变量对需求曲线的短期影响**，以及 **长期均衡路径的形成**，核心在于网络外部性机制：  

1. **多条短期需求曲线的分布与含义**  
   - 图中每条直线对应固定 $ s $ 的短期需求：  
     - $ s = 1 $：$ p = 256(1 - x) $，截距 256（$ x = 0 $ 时最高支付意愿）  
     - $ s = \frac{7}{8} $：$ p = 224(1 - x) $  
     - $ s = \frac{3}{4} $：$ p = 192(1 - x) $  
     - $ s = \frac{1}{2} $：$ p = 128(1 - x) $（上文已分析）  
     - $ s = \frac{1}{4} $：$ p = 64(1 - x) $  
     - $ s = \frac{1}{8} $：$ p = 32(1 - x) $  
   - **关键解释**：  
     - $ s $ 增大时，整条需求曲线上移（斜率不变），体现 **正向网络外部性**：更高感知份额（即消费者相信系统更流行）直接提升当前支付意愿，使企业在短期可通过营销推高 $ s $ 并维持高价（如上文所述，即使实际用户 $ x $ 低）。  
     - 例如，$ s = 1 $ 曲线远高于 $ s = \frac{1}{8} $，表明当公众认为 “全民使用” 时，即使零用户实际支付，企业也能索价 \$256。  

2. **红点（s = x 的均衡点）的经济学意义**  
   - （d）和（e）中标记的红点对应实际份额等于感知份额的市场出清点（即长期均衡下的价格-份额组合），例如：  
     | $ s = x $ | $ x $（六十分之一） | 价格 $ p $ | 计算验证 |  
     |-----------|---------------------|-----------|----------|  
     | $ \frac{1}{4} $ | 4 | \$48 | $ 256 \times \frac{1}{4} \times \frac{3}{4} = 48 $ |  
     | $ \frac{1}{2} $ | 8 | \$64 | 上文已推导 |  
     | $ \frac{3}{4} $ | 12 | \$48 | $ 256 \times \frac{3}{4} \times \frac{1}{4} = 48 $ |  
   - **动态含义**：这些点代表“信念-现实”一致的均衡，即公众预期 $ s $ 与实际需求 $ x $ 匹配时的市场状态。短期策略（如广告）可改变 $ s $ 以调整位置，但长期系统必然收敛于此路径。  

3. **长期需求曲线的几何形成（f）**  
   - 由 $ p = 256x(1 - x) $ 定义，是开口向下的抛物线：  
     - 顶点在 $ x = \frac{1}{2} $, $ p = 64 $（与上文 (b) 一致）  
     - 通过所有红点（如 $ x = \frac{1}{4} $ 和 $ x = \frac{3}{4} $ 均对应 $ p = 48 $）  
   - **在图表中的绘制逻辑**：  
     - 该曲线是短期需求曲线的 **包络线**，仅在 $ s = x $ 时有效。  
     - 比如，当 $ x = \frac{1}{2} $，所有短期曲线交于 $ p = 128 $，但长期均衡点取包络上的 $ p = 64 $，反映长期中 $ s $ 无法脱离 $ x $ 人为维持高位。  

4. **p = \$48 的多重均衡（g）的补充说明**  
   - 设定 $ p = 48 $ 时，解 $ 256s(1 - x) = 48 $ 且要求 $ x = s $，得方程 $ 48 = 256s(1 - s) $。  
   - 解得 $ s = \frac{1}{4} $ 或 $ s = \frac{3}{4} $（即 $ x = \frac{1}{4} $ 或 $ \frac{3}{4} $），但（g）提“三种”可能隐含：  
     - 低均衡：$ s = x = \frac{1}{4} $（小众偏好，易因短暂信号波动而失稳）  
     - 高均衡：$ s = x = \frac{3}{4} $（主流选择，具有正反馈稳定性）  
     - **第三种情况**：通常被忽略的 **天然垄断/空手** 均衡（$ s = x = 0 $，但支付意愿为 0 不参与市场；或 $ s = x = 1 $，$ p = 0 $），反映网络效应下市场饱和时的边界特性，与上文“长期中 $ s $ 必等于 $ x $”一致。  
   - 该结果凸显网络商品的 **路径依赖性**：初始感知碎片决定最终均衡点。

---
### Page/Slide 3



# 微观经济学解析：网络外部性下的动态均衡与企业策略

## 1. 提取图片文字与公式

### 文字内容
- market share is 0. What are the other two possibilities? **s = 1/4** and **s = 3/4**
- (h) Suppose that by using its advertising and media influence, MightySoft can temporarily set its perceived market share at any number between 0 and 1. If DoorKnobs's perceived market share is x and if MightySoft charges a price $ p = 256x(1 - x) $, the actual market fraction will also be x and the earlier perceptions will be reinforced and maintained...
- 34.2 (1) Suppose that demand for DoorKnobs is as given in the previous problem, and assume that the perceived market share in any period is equal to the actual market share in the previous period. Then where $ x_t $ is the actual market share in period t, the equation $ p = 256x_{t-1}(1 - x_t) $ is satisfied...

### 公式内容
- 价格函数：$ p = 256x(1 - x) $
- 收入函数：$ R = px = 256x^2(1 - x) $
- 一阶条件：$ \frac{d}{dx}256(x^2 - x^3) = 0 \implies 2x = 3x^2 $
- 二阶条件：仅当 $ x = 2/3 $ 时满足
- 最优价格：$ p = 256 \times \frac{1}{3} \times \frac{2}{3} = \$56.89 $
- 动态需求方程：$ x_t = 1 - \frac{p}{256x_{t-1}} $（当 $ \frac{p}{256x_{t-1}} \leq 1 $）
- 实际计算示例：
  - $ x_1 = 0.5 \to x_2 = 0.75 \to x_3 = 0.833 $
  - $ x_4 = 0.8529 $, $ x_5 = 0.8534 $, $ x_6 = 0.853553 $

## 2. 结合上文的关键解析

### (h)部分：短期策略优化模型
- **核心逻辑**：向上文所述，企业可通过短期营销操作感知份额 $ s $。此处 **具体化优化问题**：当 $ s = x $ 时（即实现信念-现实一致），企业选择 $ x $ 使收入最大化。
- **机制延伸**：
  - 在 $ p = 256x(1 - x) $ 框架下，收入 $ R = 256x^2(1 - x) $ 是典型的网络效应收益函数。
  - 一阶条件解得 **最优市场占有率 $ x = \frac{2}{3} $**（远高于对称均衡点 $ x = \frac{1}{2} $），说明网络效应下垄断倾向更强。
  - $ x = \frac{2}{3} $ 处于 $ s = x = \frac{3}{4} $（高均衡）与 $ s = x = \frac{1}{2} $ 之间，**验证了高价主导战略**：通过短期塑造 $ s = \frac{2}{3} $，企业可维持 $ p \approx \$56.89 $，高于长期对称均衡价 \$64（因远离顶点）。

### 34.2(1)部分：动态收敛机制实证
- **核心逻辑**：解释上文 "长期系统必然收敛" 的具体路径，**填补了静态均衡模型的动态过程**。
- **关键推导**：
  - 感知份额动态规则 $ s_t = x_{t-1} $ 直接实现 **"预期基于历史" 的合理性**，与上文红点 $ s = x $ 的长期约束一致。
  - 在固定价 $ p = \$32 $ 下，迭代过程 $ x_t = 1 - \frac{32}{256x_{t-1}} $ 以 **单调递增** 方式收敛（由 $ x_1 = 0.5 \to x_6 \approx 0.8536 $）。
- **收敛性含义**：
  - 稳定点 $ x^* $ 满足 $ x^* = 1 - \frac{32}{256x^*} \implies 8x^{*2} - 8x^* + 1 = 0 $，解得 $ x^* = \frac{2+\sqrt{2}}{4} \approx 0.8536 $（在 $ \frac{1}{2} $ 与 $ \frac{3}{4} $ 之间）。
  - 该值 **落于长期需求曲线 $ p = 256x(1 - x) $**：代入得 $ p = 256 \times 0.8536 \times 0.1464 \approx \$32 $，**认证动态过程与长期均衡的一致性**。
- **与上文多重均衡的关联**：
  - 价格 $ p = \$32 $ 位于 $ \$48 $（双重均衡价）以下，系统自动偏向 **高均衡区域**（$ x^* > \frac{3}{4} $）。
  - 印证上文路径依赖特性：起始点 $ x_1 = 0.5 $ 离高均衡更近，系统选择性收敛至 $ x^* \approx 0.85 > 0.75 $。

### 综合洞察
- **短期-长期衔接**：(h)部分展示企业如何利用短期 $ s $ 操控实现超额利润（如 $ x = \frac{2}{3} $ 时 $ p \approx \$56.89 $），但 34.2(1) 证明 **价格无法永久偏离曲线**——固定价格策略下系统仍向长期曲线趋近。
- **网络效应实证**：动态收敛过程量化说明 "正向反馈机制"：实际份额增长 → 下期感知份额提升 → 企业可维持高价（此处 $ p = \$32 $ 不变时，实际份额从 0.5 逐步提升至 0.8536）。
- **政策启示**：企业若想锁定长期高均衡（$ x^* \approx 0.85 > \frac{3}{4} $），初期需确保实际份额 $ x_1 > 0.5 $（避开低均衡引力场），否则可能陷入 $ x = \frac{1}{4} $ 相关的低均衡轨迹。

---
### Page/Slide 4



# 提取文字与公式

## 文字内容
- 412 INFORMATION TECHNOLOGY (Ch. 34)
- (b) Notice that when price is held constant at $ p $, if DoorKnobs’s market share converges to a constant $ \bar{x} $, it must be that $ \bar{x} = 1 - (p/256\bar{x}) $. Solve this equation for $ \bar{x} $ in the case where $ p = \$32 $. What do you make of the fact that there are two solutions? This equation implies $ x^2 - x + 1/8 = 0 $. Solutions are $ x = 0.853355 $ and $ x = 0.14645 $. Both are equilibrium market shares with a price of $ \$32 $.
- 34.3 (1) A group of 13 consumers are considering whether to connect to a new computer network. Consumer 1 has an initial value of $ \$1 $ for hooking up to the network, consumer 2 has an initial value of $ \$2 $, consumer 3 has an initial value of $ \$3 $, and so on up to consumer 13. Each consumer’s willingness to pay to connect to the network depends on the total number of persons who are connected to it. In fact, for each $ i $, consumer $ i $’s willingness to pay to connect to the network is $ i $ times the total number of persons connected. Thus if 5 people are connected to the network, consumer 1’s willingness to pay is $ \$5 $, consumer 2’s willingness to pay is $ \$10 $ and so on.
  - (a) What is the highest price at which 9 customers could hook up to the market and all of them either make a profit or break even? $ \$45 $
  - (b) Suppose that the industry that supplies the computer network is competitive and that the cost of hooking up each consumer to the network is $ \$45 $. Suppose that consumers are very conservative and nobody will sign up for the network unless her buyer value will be at least as high as the price she paid as soon as she signs up. How many people will sign up if the price is $ \$45 $? 0
  - (c) Suppose that the government offers to subsidize “pioneer users” of the system. The first two users are allowed to connect for $ \$10 $ each. After the first two users are hooked up, the government allows the next two to connect for $ \$25 $. After that, everyone who signs up will have to pay the full cost of $ \$45 $. Assume that users remain so conservative that will sign up only if their buyer values will be at least equal to the price they are charged when they connect. With the subsidy in place, how many consumers in toto will sign up for the network? 9
- 34.4 (2) Professor Kremepuff has written a new, highly simplified economics text, *Microeconomics for the Muddleheaded*, which will be published by East Frisian Press. The first edition of this book will be in print for two years, at which time it will be replaced by a new edition. East

## 公式
- 稳态条件：$ \bar{x} = 1 - \frac{p}{256 \bar{x}} $
- 当 $ p = 32 $ 时：$ \bar{x}^2 - \bar{x} + \frac{1}{8} = 0 $
- 解：$ \bar{x} = 0.853355 $ 和 $ \bar{x} = 0.14645 $

# 关键解析

## 动态稳态的数学验证与均衡分裂
- 图片中 34.2(b) 的稳态方程 $ \bar{x} = 1 - \frac{p}{256 \bar{x}} $ 是上文 **动态需求方程 $ x_t = 1 - \frac{p}{256 x_{t-1}} $** 的长期收敛条件。两解直接证明 **网络效应市场的多重均衡本质**：
  - **高均衡** $ \bar{x} \approx 0.8534 $：与上文迭代序列 $ x_6 = 0.853553 $ 完全吻合，验证了当 $ x_1 = 0.5 $ 时系统向高均衡收敛的路径。
  - **低均衡** $ \bar{x} \approx 0.1465 $：上文隐含但未显式计算的第二个稳态点，揭示系统可能陷入低效率均衡（若起始点 $ x_1 < 0.5 $）。

## 多重均衡的机制解读
- **价差定位**：$ p = \$32 $ 低于双重均衡临界价 \$48（上文 34.2(1) 部分），导致两个解分属不同区域：
  | 均衡类型 | 市场占有率 | 与上文关联 | 收敛条件 |
  |---|---|---|---|
  | 高均衡 | $ \bar{x} \approx 0.8534 $ | $ x^* = \frac{2+\sqrt{2}}{4} $ | $ x_1 > \text{低均衡值} $ |
  | 低均衡 | $ \bar{x} \approx 0.1465 $ | 未显式计算但逻辑存在 | $ x_1 < 0.5 $（路径依赖） |
- **收敛方向决定权**：上文实际迭代 $ x_1=0.5 \to x_2=0.75 $ 跳过 $ x=0.1465 $ 的引力场，直接进入高均衡轨道。图片通过解析解量化了双重均衡的边界，印证了 **"初始份额是策略性关键"** 的洞察。

## 与上文模型的统一验证
- 高均衡解 $ \bar{x} = 0.853355 $ 代入长期需求曲线 $ p = 256x(1-x) $：
  $$
  p = 256 \times 0.853355 \times (1 - 0.853355) \approx 256 \times 0.853355 \times 0.146645 = \$32
  $$
  与图片 "price of \$32" 完全一致，**确证动态过程严格约束于长期需求曲线**。
- 低均衡解同理：$ p = 256 \times 0.14645 \times (1 - 0.14645) \approx \$32 $，说明**单一定价可支持多个稳态**，企业短期策略需规避低均衡陷阱（呼应上文 "初期确保 $ x_1 > 0.5 $" 的政策启示）。

> 注：34.3 与 34.4 部分为独立消费者网络问题，未涉及上文网络效应核心模型，故不展开关联分析。

---
### Page/Slide 5



### 当前图片内容提取

#### 文字内容
Frisian Press has already made all its fixed cost investments in the book and must pay a constant marginal cost of $c for each copy that it sells.  
Let \( p_1 \) be the price charged for new copies sold in the first year of publication and let \( p_2 \) be the price charged for new copies sold in the second year of publication. The publisher and the students who buy the book are aware that there will be an active market for used copies of *Microeconomics for the Muddleheaded* one year after publication and that used copies of the first edition will have zero resale value two years after publication. At the end of the first year of publication, students can resell their used textbooks to bookstores for 40% of the second-year price, \( p_2 \).  
The net cost to a student of buying the book in the first year, using it for class, and reselling it at the end of the year is \( p_1 - 0.4p_2 \). The number of copies demanded in the first year of publication is given by a demand function, \( q_1 = D_1(p_1 - 0.4p_2) \).  
Some of the students who use the book in the first year of publication will want to keep their copies for future reference, and some will damage their books so that they cannot be resold. The cost of keeping one’s old copy or of damaging it is the resale price \( 0.4p_2 \). The number of books that are either damaged or kept for reference is given by a “keepers” demand function, \( D^k(0.4p_2) \). It follows that the number of used copies available at the end of the first year will be \( D_1(p_1 - 0.4p_2) - D^k(0.4p_2) \).  
Students who buy *Microeconomics for the Muddleheaded* in the second year of publication will not be able to resell their used copies, since a new edition will then be available. These students can, however, buy either a new copy or a used copy of the book. For simplicity of calculations, let us assume that students are indifferent between buying a new copy or a used copy and that used copies cost the same as new copies in the book store. (The results would be the same if students preferred new to used copies, but bookstores priced used copies so that students were indifferent between buying new and used copies.) The total number of copies, new and used, that are purchased in the second year of publication is \( q_2 = D_2(p_2) \).  
(a) Write an expression for the number of new copies that East Frisian Press can sell in the second year after publication if it sets prices \( p_1 \) in year 1 and \( p_2 \) in year 2. \( D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2) \).  
(b) Write an expression for the total number of new copies of *Microeconomics for the Muddleheaded* that East Frisian can sell over two years at prices \( p_1 \) and \( p_2 \) in years 1 and 2. \( D_1(p_1 - 0.4p_2) + D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2) = D_2(p_2) + D^k(0.4p_2) \).  
(c) Would the total number of copies sold over two years increase, decrease, or remain constant if \( p_1 \) were increased and \( p_2 \) remained constant? It would remain constant.  

#### 公式列表
- \( q_1 = D_1(p_1 - 0.4p_2) \)
- Used copies available at end of year 1: \( D_1(p_1 - 0.4p_2) - D^k(0.4p_2) \)
- \( q_2 = D_2(p_2) \)
- Part (a): New copies in year 2 = \( D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2) \)
- Part (b): Total new copies over two years = \( D_1(p_1 - 0.4p_2) + [D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2)] = D_2(p_2) + D^k(0.4p_2) \)
- Part (c): Total sales invariant to \( p_1 \) when \( p_2 \) fixed

---

### 解析：二手市场动态与需求补偿机制

本部分内容属于【上文知识点总结】中提及的独立消费者网络问题（34.4），虽未关联网络效应核心模型，但展现了**价格动态对总需求的非敏感性**。与上文34.2的多重均衡路径依赖不同，此模型通过二手市场实现**需求自动补偿**，体现市场机制的独特鲁棒性。

#### 关键机制解读
1. **净成本驱动的一期需求**  
   - 第一年需求 \( q_1 = D_1(p_1 - 0.4p_2) \) 依赖净成本（价格减预期残值），反映消费者对价格变化的敏感性。
   - **对比上文网络效应**：34.2中消费者决策基于他人参与度（动态外部性），此处则受跨期价格影响（无直接网络外部性）。当 \( p_1 \) 上升，\( q_1 \) 下降，但通过二手渠道传递替代效应。

2. **二手市场实现总需求稳定**  
   - 第二年新书销量（Part a） = \( D_2(p_2) - [D_1(p_1 - 0.4p_2) - D^k(0.4p_2)] \)  
     其中 \( D_1(p_1 - 0.4p_2) - D^k(0.4p_2) \) 为可用二手书数量，**直接抵消第一年需求变动**。
   - 总新书销量（Part b）简化为 \( D_2(p_2) + D^k(0.4p_2) \)，**仅依赖 \( p_2 \)**:
     - \( D_2(p_2) \): 第二年新/旧书总需求（规模固定）。
     - \( D^k(0.4p_2) \): 二手书"保留成本"效用（正比于 \( p_2 \) ）。
   - **与上文关键差异**：34.2（网络效应）中价格变化可能引发多重均衡跃迁；此处价格 \( p_1 \) 变化被二手市场内生吸收，总销量恒定（Part c），**消除了路径依赖风险**。

3. **市场机制隐含含义**  
   - **补偿效应**：提高 \( p_1 \) 减少第一年新书需求，但增加可售二手书（因 \( q_1 \) 下降），第二年新书销量反向调整至原水平。系统通过二手渠道传递**负外部性内化**，确保总社会福利不变。
   - **政策启示**：若出版社仅控制 \( p_2 \)，可精准管理长期销量（因总销量与 \( p_1 \) 无关）；但控制 \( p_1 \) 无法影响总量，仅调整新/旧销量分布。这与上文"初期确保 \( x_1 > 0.5 \) 以防低均衡"的主动干预逻辑**截然相反**——此处市场自身维持总量稳定。

> 注：本模型属于耐用品跨期定价范畴（非网络效应），与上文34.2的动态需求曲线 \( p = 256x(1-x) \) 无直接关联。其核心贡献在于揭示**二手市场作为自动稳定器**，使总需求对单期价格具有弹性补偿能力，避免了网络效应中的协调失败风险。

---
### Page/Slide 6



### 延伸解析：企业收益与利润最大化决策  
当前图片内容为上文需求模型的**企业实践延伸**，聚焦出版社如何基于已建立的销量机制设计定价策略以实现利润最大化。核心逻辑延续上文"总新书销量与 $ p_1 $ 无关"的结论，但将分析维度从**市场需求**升级至**企业收益函数**，揭示价格策略的微观决策机制。

---

#### 1. 关键公式与文字提取
| 部分 | 文字内容 | 公式 |
|------|----------|------|
| (d) | 总收入表达式 | $ p_1 D_1(p_1 - 0.4p_2) + p_2 \left[ D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2) \right] $ = $ (p_1 - p_2)D_1(p_1 - 0.4p_2) + p_2 \left[ D_2(p_2) + D^k(0.4p_2) \right] $ |
| (e) | 利润函数推导 | $ (p_1 - p_2)D_1(p_1 - 0.4p_2) + (p_2 - c) \left[ D_2(p_2) + D^k(0.4p_2) \right] $ |
|  | 可变成本说明 | $ c \left( D_2(p_2) + D^k(0.4p_2) \right) $ |
| (f) | 统一价格下的净收益 | $ (p - c) \left( D_2(p) + D^k(0.4p) \right) $ |
| 34.5(2) | 具体需求函数 | $ D_1(p_1 - 0.4p_2) = 100(90 - p_1 + 0.4p_2) $<br>$ D_2(p_2) = 100(90 - p_2) $<br>$ D^k(0.4p_2) = 100(90 - 0.8p_2) $ |

---

#### 2. 模型延伸与上文的连续性分析  
##### (d) 总收入结构：动态定价的套利空间  
- **与上文衔接**：  
  总收入表达式直接基于上文Part (a)(b) 的销量公式：  
  $$ \text{第一年销量 } q_1 = D_1(p_1 - 0.4p_2), \quad \text{第二年新书销量} = D_2(p_2) - D_1(p_1 - 0.4p_2) + D^k(0.4p_2) $$  
  收入函数将销量转换为货币流，**关键简化项** $ (p_1 - p_2)D_1(\cdot) $ 揭示：  
  - 企业通过 $ p_1 > p_2 $ 可在第一年获取溢价（$ p_1 - p_2 $），但该溢价仅作用于早购群体（即 $ D_1(\cdot) $）  
  - **上文结论的强化**：$ D_1(\cdot) $ 随 $ p_1 $ 上升而下降，但溢价项 $ (p_1 - p_2) $ 可部分抵消销量损失，而第二年收入完全锁定于总需求 $ D_2 + D^k $  

##### (e) 利润最大化：成本如何改变决策焦点  
- **核心创新点**：  
  利润函数明确分离出两个独立决策变量：  
  $$ \underbrace{(p_1 - p_2)D_1(p_1 - 0.4p_2)}_{\text{跨期套利项}} + \underbrace{(p_2 - c) \left[ D_2(p_2) + D^k(0.4p_2) \right]}_{\text{总销量利润项}} $$  
  - **与上文的深刻关联**：  
    - 第二项 $ (p_2 - c)[D_2 + D^k] $ 直接依赖上文Part (b) 的核心发现——总销量 $ D_2 + D^k $ **与 $ p_1 $ 无关**  
    - 企业在 $ p_2 $ 上的定价直接影响全部利润（因总销量仅由 $ p_2 $ 决定），而 $ p_1 $ 仅通过第一项影响早购群体利润  
  - **隐含决策逻辑**：  
    > 若出版社首要目标是长期利润，应优先优化 $ p_2 $（影响总销量），$ p_1 $ 仅作为调节早购者利润的工具  

##### (f) 统一价格约束：简化的决策环境  
- **上文的延伸应用**：  
  当 $ p_1 = p_2 = p $ 时：  
  $$ \text{利润} = (p - c) \left[ D_2(p) + D^k(0.4p) \right] $$  
  - **与上文Part (c) 的呼应**：  
    总销量 $ D_2(p) + D^k(0.4p) $ 仍仅由单变量 $ p $（即原 $ p_2 $）决定，验证了"总销量与 $ p_1 $ 无关"的普适性  
  - **损失的定价能力**：  
    企业放弃 $ p_1 > p_2 $ 的溢价策略后，利润函数退化为单变量优化问题，**进一步证明 $ p_1 $ 对总量决策无实质影响**  

##### 34.5(2) 数值化验：参数化的市场机制  
- **关键验证**：  
  代入具体需求函数：  
  $$ \text{总销量} = D_2(p_2) + D^k(0.4p_2) = 100(90 - p_2) + 100(90 - 0.8p_2) = 100(180 - 1.8p_2) $$  
  - **彻底确认上文结论**：总销量仅含 $ p_2 $，与 $ p_1 $ 无关（系数为0）  
  - **垄断定价启示**：  
    企业利润函数 $ (p - 10) \times 100(180 - 1.8p) $ 为开口向下的抛物线，最大值点 $ p^* = 55 $（通过求导得）。**这直接延续上文逻辑**——利润仅由 $ p_2 $（现为 $ p $）决定，无需考虑 $ p_1 $  

---

#### 3. 机制本质的再强调  
- **动态定价的边界**：  
  即使企业拥有 $ p_1 $ 和 $ p_2 $ 两个工具，**总利润的可控维度实际只有一个**（即 $ p_2 $），因 $ p_1 $ 的变动仅通过二手市场内生补偿，最终被限制在早购群体套利范围内。  
- **与上文"需求补偿"的闭环**：  
  ```mermaid
  graph LR
    A[p₁上升] --> B[q₁下降]
    B --> C[可用二手书增加]
    C --> D[q₂新书销量反向调整]
    D --> E[总销量不变]
    E --> F[企业只能通过p₂影响总利润]
  ```  
  这一闭环使出版社的核心策略从"管理两期价格"简化为"优化 $ p_2 $ 以匹配总需求弹性"，再次凸显**二手市场作为自动稳定器**的微观基础。

---
### Page/Slide 7



### 当前图片解析

#### 1. 图片文字与公式提取
**34.5(a)**  
- 文字：*"If East Frisian Press charges the same price $ p $ for Microeconomics for the Muddleheaded in the first and second years, show that the total sales of new copies over the two years are equal to $ 18,000 - 180p $."*  
- 公式：  
  $$
  \text{Total sales are} \quad D_2(p) + D^k(0.4p) = 100(90 - p) + 100(90 - 0.8p) = 18,000 - 180p
  $$

**34.5(b)**  
- 公式：  
  $$
  (p - 10)(18,000 - 180p) = 19,800p - 180p^2 - 180,000
  $$

**34.5(c)**  
- 结论：$ p = \$55 $  
- 分项数据：  
  - First-year new copies sold: $ 5,700 $  
  - Resold used books: $ 1,100 $  
  - Second-year new copies purchased: $ 2,400 $  
  - Total net revenue: $ \$364,500 $  

**34.6 (2)(a)**  
- 新场景需求：  
  $$
  \text{Total copies over two years} = 200(90 - p)
  $$
- 利润公式：  
  $$
  200(p - 10)(90 - p)
  $$

---

#### 2. 关键公式与数值的微观含义
##### **(1) 总销量公式 $ 18,000 - 180p $ 的实证验证**
- **公式结构**：  
  $ D_2(p) + D^k(0.4p) = 100(90 - p) + 100(90 - 0.8p) $  
  - $ D_2(p) = 100(90 - p) $：第二年新书需求（与上文 $ D_2(p_2) $ 一致）  
  - $ D^k(0.4p) = 100(90 - 0.8p) $：二手书需求（隐含推导：$ 0.8p = 2 \times 0.4p $，对应价格折扣系数）  
- **与上文关联**：  
  上文结论**总销量仅由 $ p_2 $ 决定**在此被严格验证：  
  - $ p_1 $ 未出现在公式中（因 $ p_1 = p_2 = p $）  
  - 二手市场自动补偿机制使 $ p_1 $ 变动不影响总量（符合上文闭环逻辑）

##### **(2) 利润最大化点 $ p = \$55 $ 的微观逻辑**
- **计算依据**：  
  利润函数 $ \pi = (p - 10)(18,000 - 180p) $ 求导得：  
  $$
  \frac{d\pi}{dp} = 18,000 - 360p + 1,800 = 0 \implies p^* = 55
  $$
- **实证数据闭环**：  
  | 项目 | 数值 | 微观含义 |  
  |---|---|---|  
  | First-year new sales | $ 5,700 $ | $ D_1(p - 0.4p) = 100(90 - 0.6 \times 55) = 5,700 $ |  
  | Used books resold | $ 1,100 $ | $ D_1(\cdot) - q_2^{\text{new}} $ 的补偿量（验证跨期套利） |  
  | Second-year new sales | $ 2,400 $ | $ D_2(p) - [\text{used books}] = 100(90-55) - 1,100 = 2,400 $ |  
  - **总量一致性**：$ 5,700 + 2,400 = 8,100 $ 且 $ 18,000 - 180 \times 55 = 8,100 $  
  - **隐含结论**：$ p_1 $ 无独立调控空间（因 $ p_1 = p $），企业**唯一可控变量为 $ p_2 $**

##### **(3) 34.6(2) 新版场景的对照实验**
- **公式异质性**：  
  $ 200(90 - p) $ vs. $ 18,000 - 180p $  
  - 若破坏二手市场（一年后出新版），总销量**失去二手需求项** $ D^k(0.4p) $，还原为纯新书需求  
  - 需求弹性变化：$ |\frac{dQ}{dp}| = 200 $（新版场景） vs. $ 180 $（有二手市场）  
- **微观机制验证**：  
  - 二手市场存在时：总销量 $ \propto 180p $（上文核心结论）  
  - 二手市场消失时：销量仅由新书重复购买决定，证明 **$ D^k $ 是限制 $ p_1 $ 作用的关键环节**

---

#### 3. 与上文知识的连续性说明
1. **总销量独立性强化**：  
   图片中 $ 18,000 - 180p $ 的推导，本质是上文需求函数 $ D_2(p_2) + D^k(0.4p_2) $ 的具体化，**彻底排除 $ p_1 $ 影响**（与上文"系数为0"结论完全一致）。

2. **跨期定价决策失效的证据**：  
   - $ p = \$55 $ 时，第一年早购群体仅占 $ 5,700/8,100 \approx 70.4\% $  
   - 二手书销量 ($ 1,100 $) 恰好补偿新书销量损失，证实上文闭环逻辑：  
     $ p_1 \uparrow \implies q_1 \downarrow \implies \text{used books} \uparrow \implies q_2^{\text{new}} \text{ adjusts} \implies \text{total sales unchanged} $

3. **企业决策焦点一元化**：  
   34.5(c) 的 $ p^* = \$55 $ 与上文数值模型 $ p^* = 55 $ 完全吻合，证明**即使拥有两期定价工具，企业实际仅需优化 $ p_2 $**：  
   - $ p_1 $ 调整被市场内生抵消（通过二手渠道）  
   - 利润最大化高度聚焦于 $ p_2 $ 对总需求弹性的适配  

> **注**：34.6(2) 场景通过移除二手市场，反向验证了**二手市场是 $ p_1 $ 无效性的微观基础**，与上文"动态定价的边界"论断形成双重实证支撑。

---
### Page/Slide 8



### 当前图片内容提取

#### 文字内容
- 页码信息：416 INFORMATION TECHNOLOGY (Ch. 34)
- (b) Find the price that maximizes total revenue net of variable costs.  
  $50.
- (c) The total number of new books sold in the first year would be 4,000, and the total number of books sold in the second year would be 4,000.
- (d) East Frisian’s total revenue net of variable costs, if it markets a new edition after one year, will be $320,000.
- (e) Would it be more profitable for East Frisian Press to produce a new edition after one year or after two years? After two years. Which would be better for students? (Hint: The answer is not the same for all students.) After two years is better for students who take the course in the first year of publication and plan to sell. After one year is better for the other students.
- 34.7 (3) Suppose that East Frisian Press publishes a new edition only after two years and that demands and costs are as in the previous problems. Suppose that it sets two different prices $ p_1 $ and $ p_2 $ in the two periods.
  - (a) Write an expression for the total number of new copies sold at prices $ p_1 $ and $ p_2 $ and show that this number depends on $ p_2 $ but not on $ p_1 $.  
    $ 100 \left( (70 - p_1 + .4p_2) + (140 - 1.8p_2) - (70 - p_1 + .4p_2) \right) = 100(140 - 1.8p_2) $
  - (b) Show that at prices $ p_1 $ and $ p_2 $, the difference between revenues and variable costs is equal to  
    $ 100 \left( 90p_1 + 108p_2 + 1.4p_1p_2 - p_1^2 - 2.2p_2^2 - 1,800 \right) $.  
    This difference is $ 100(p_1 - p_2)(90 - p_1 + .4p_2) + (p_2 - 10)(180 - 1.8p_2) $. Expand this expression.

#### 公式汇总
- 总销量表达式（34.7(3)(a)）:  
  $$
  100 \left( (70 - p_1 + 0.4p_2) + (140 - 1.8p_2) - (70 - p_1 + 0.4p_2) \right) = 100(140 - 1.8p_2)
  $$
- 利润表达式（34.7(3)(b)）:  
  $$
  100 \left( 90p_1 + 108p_2 + 1.4p_1p_2 - p_1^2 - 2.2p_2^2 - 1,800 \right)
  $$
  或等价形式:  
  $$
  100(p_1 - p_2)(90 - p_1 + 0.4p_2) + (p_2 - 10)(180 - 1.8p_2)
  $$

---

### 基于上文知识点的解析

#### （1）总销量独立性验证
- **核心公式与上文连续性**：  
  34.7(3)(a) 中的简化表达式 $ 100(140 - 1.8p_2) $ 直接证实了**上文总结的核心结论**：总销量仅由 $ p_2 $ 决定，与 $ p_1 $ 无关。  
  - 数学本质：表达式通过抵消项 $ (70 - p_1 + 0.4p_2) $ 被完全消除（展开后 $ p_1 $ 项相互抵消），这与上文分析中“$ p_1 $ 在总销量公式中系数为 0”的逻辑一致。  
  - 需求结构对应：  
    - 上文总销量模型 $ 18,000 - 180p $ 源于 $ D_2(p) + D^k(0.4p) $（即新书与二手书需求叠加），此处 $ 100(140 - 1.8p_2) = 14,000 - 180p_2 $ 为同类结构，仅参数因具体需求函数差异而调整（上文为 $ 90 - p $，此处为 $ 70 - p_1 + 0.4p_2 $ 类推）。  
    - **关键强化点**：二手市场内生补偿机制（$ D^k(0.4p) $ 项）的存在，使 $ p_1 $ 变动被二手渠道对冲，企业无法通过 $ p_1 $ 控制总量，这与上文“$ p_1 $ 无独立调控空间”的结论形成双重验证。

#### （2）利润函数与定价决策聚焦
- **利润表达式微观含义**：  
  34.7(3)(b) 中的利润函数可分为两类项，揭示定价逻辑：  
  - **$ p_1 $ 无效性实证**：等价形式 $ 100(p_1 - p_2)(90 - p_1 + 0.4p_2) + (p_2 - 10)(180 - 1.8p_2) $ 中：  
    - 第一项 $ (p_1 - p_2)(\cdots) $ 在 $ p_1 = p_2 $ 时为零，符合上文“$ p_1 = p $”的假设场景。  
    - 第二项 $ (p_2 - 10)(180 - 1.8p_2) $ 为纯 $ p_2 $ 依赖项，与上文利润函数 $ (p - 10)(18,000 - 180p) $ 结构一致（此处对应 $ 100(p_2 - 10)(180 - 1.8p_2) $，即 $ (p_2 - 10) \times \text{总销量} $）。  
  - **企业决策一元化**：  
    利润最大化需对 $ p_2 $ 求导，而 $ p_1 $ 仅出现在抵消项中，无法影响最优解。这直接支撑上文结论：**企业唯一可控变量为 $ p_2 $**，$ p_1 $ 调整被市场内生吸收（如上文实证数据中第一年早购群体仅占 70.4%，二手书销量补偿新书损失）。

#### （3）与上文对照场景的区分
- **新版场景（图片开头部分）的关联**：  
  - (b) 中价格 $ \$50 $、(c) 中年销量 $ 4,000 $、(d) 中净收益 $ \$320,000 $ 对应**破坏二手市场的场景**（“markets a new edition after one year”），即无二手书需求。  
  - 此场景与上文 34.6(2) 新版实验一致：  
    - 需求还原为纯新书行为（类比上文 $ 200(90 - p) $），需求弹性更强（$ |dQ/dp| = 200 $ 隐含）。  
    - 利润计算 $ \$320,000 $ 体现二手市场缺失后的效率损失，反向验证二手市场存在时总销量 $ \propto 180p $ 的弹性机制（上文“动态定价的边界”结论）。  
  - (e) 中“after two years better for profitability” 说明：企业保留二手市场（两年新版）可最大化利润，因 $ p_1 $ 无效性被抵消，而“after one year” 对部分学生更有利体现分配效应，但不影响核心机制。

> **知识连续性总结**：34.7(3) 的公式既是上文需求逻辑的具体化（$ 14,000 - 180p_2 $ 对应 $ 18,000 - 180p $），更是对“总销量独立性”和“$ p_1 $ 无效性”的严格推导。从此场景与图片开头新版场景的对比，可证实**二手市场是 $ p_1 $ 无作用的微观基础**——其消失时（如新版场景），企业才需独立优化 $ p_1 $，但此时利润低于保留二手市场的两年周期策略。

---
### Page/Slide 9



### 当前图片内容提取与解析

#### 1. 文字与公式提取
- **(c) 部分**  
  `Calculate the prices $p_1$ and $p_2$ that maximize the difference between total revenue and variable costs and hence maximize profits. $p_1 = \$80$, $p_2 = \$50$`
  
- **(d) 部分**  
  `If East Frisian Press chooses its profit-maximizing $p_1$ and $p_2$, compare the cost of using Microeconomics for the Muddleheaded for a student who buys the book when it is first published and resells it at the end of the first year with the cost for a student who buys the book at the beginning of the second year and then discards it. The former has a net cost of $\$80 - .4 \times 50 = \$60$ and the latter has a cost of $\$50$.`

- **34.8(2)(a) 部分**  
  `If the interest rate is $r = .10$ per period, what is the present value of the stream of payments made by the consumer? (Hint: a stream of payments of $x$ starting next period has a present value of $x/r$.) The total cost of ownership of Fasten is $50 + 20 / .10 = \$250$.`
  
- **34.8(2)(b) 部分**  
  `Fasten’s competitor produces an equally effective product called Czechwriter. ... This means his switching costs are $\$50$`
  
- **34.8(2)(c) 部分**  
  `Fasten is contemplating raising the price of checks to $\$30$ per period. If so, will its customers switch to Czechwriter? Explain. Yes, the present value of continuing to use Fasten are $\$300$ while the costs of switching to Czechwriter are $\$250$.`

#### 2. 结合上文知识点的解析
##### (1) 利润最大化价格与 `p₁` 无效性的验证
- **核心公式含义**：  
  $p_1 = \$80$, $p_2 = \$50$ 的结果直接印证上文结论：**`p₂` 是企业唯一可控变量**。  
  - 该价格组合使利润函数（上文推导的 $100(p_1 - p_2)(90 - p_1 + 0.4p_2) + (p_2 - 10)(180 - 1.8p_2)$）中 `p₁` 项失效。当 $p_1 = p_2$ 时，第一项为零，仅第二项 $(p_2 - 10)(180 - 1.8p_2)$ 决定最优解。  
  - 此处 $p_2 = \$50$ 满足一阶条件（对 $p_2$ 求导为零），而 $p_1$ 被固定为 $\$80$ 以平衡市场分配（如早购/晚购群体），但**不影响总量与总利润**——与上文“`p₁` 无独立调控空间”完全一致。

##### (2) 二手市场对冲机制的具体化
- **`d` 部分净成本公式的微观解释**：  
  $$ \text{净成本} = p_1 - 0.4p_2 = \$80 - 0.4 \times \$50 = \$60 $$
  - **符号含义**：$0.4p_2$ 对应上文二手价格系数 $0.4p$，表示二手书市场使早购者有效价格降至 $p_1 - 0.4p_2$。  
    - 上文已证实：总销量 $14,000 - 180p_2$ 仅由 $p_2$ 决定，因 $p_1$ 变动被 $0.4p_2$ 完全抵消。  
  - **经济含义**：  
    - 早购者净成本 $\$60$ > 晚购者成本 $p_2 = \$50$，说明尽管 `p₁` 设为 $\$80$（看似高价），但二手转售补偿使实际负担降低，**消费者调整行为强化了 `p₁` 的无效性**。  
    - 此数字差异（$\$60$ vs $\$50$）直接解释上文“第一年早购群体仅占 70.4%”：部分学生因净成本较高而推迟购买，但总量仍由 $p_2$ 独立控制，与企业定价策略无关。

##### (3) 34.8(2) 与核心逻辑的延伸关联
- **互补品定价的类比价值**：  
  虽属新场景，但与上文二手市场机制同源——**耗材（checks）定价等效于 `p₂`，主导长期利润**。  
  - **(a) 现值公式**：$50 + 20 / 0.10 = \$250$  
    - 体现消费者对互补品价格的敏感性，类比上文总销量函数 $14,000 - 180p_2$：耗材成本 $20/r$ 主导长期支出，类似二手价格系数 $0.4p_2$ 缩短新书需求动态。  
  - **(c) 切换成本分析**：  
    - 支票涨价后，继续使用现值 $\$300$（即 $30 / 0.10$） > 切换成本 $\$250$（软件费 $50$ + 耗材现值 $20/0.10$），导致客户流失。  
    - **与上文知识连续性**：  
      企业试图提高 `p₂`（耗材价）时，需权衡锁定效应边界——如同二手市场中 $p_2$ 变动会触发早购/晚购分配调整，但**不影响总量刚性**（上文 $14,000 - 180p_2$）。此处耗材涨价引发切换，本质是 `p₂` 作为唯一有效变量超出用户承受临界点，印证上文“`p₁` 无效，`p₂` 决定利润边界”。

> **知识衔接点**：当前图片中 `d` 部分的净成本公式 $p_1 - 0.4p_2$ 是上文 $(p_1 - p_2)(\cdots)$ 项的具体数值实现，直接展示二手市场对冲机制如何使 `p₁` 失去独立作用；34.8(2) 则拓展至互补品场景，证实**企业利润管理始终聚焦唯一价格变量（`p₂` 或耗材价），而次要变量（`p₁` 或初始产品价）仅影响市场分配，不改变总量逻辑**。

---
### Page/Slide 10



### 当前图片解析：互补品定价与切换成本边界

#### 1. 文字与公式提取  
**文字内容：**  
- (d) Fasten contemplates raising the price of checks to \$22 per period. Will its customers switch? No. The present value of continuing to use Fasten are \$220 while the present value of switching to Czechwriter is \$250.  
- (e) At what price for checks will Fasten’s customers just be indifferent to switching? (Hint: Let \(x\) be this amount. Compare the present value of staying with Fasten with the present value of switching to Czechwriter.) Solve the equation \(x / .10 = 250\) to find \(x = 25\).  
- (f) If it charges the highest price that it can without making its customers switch, what profit does Fasten make on checks from each of its customers per period? \$5. What is the present value of the profit per customer that Fasten gets if it sets the price of checks equal to the number determined in the last question? \(PV = 5 / .10 = 50\). How does this compare to the customer switching cost? It is the same.  
- (g) Suppose now that the cost of switching also involves several hours of data conversion that the consumer values at \$100. The total cost of switching is the cost of the new program plus the data conversion cost which is \$150.  
- (h) Making allowances for the cost of data conversion, what is the highest price that Intoot can charge for its checks? Solve \(x / .10 = 250 + 100\) for \(x = 35\). What is the present value of profit from this price? \$150. How does this compare to total switching costs? It is the same.  
- (i) Suppose that someone writes a computer program that eliminates the cost of converting data and makes this program available for free. Suppose that Intoot continues to price its check refill packages at \$25. A new customer is contemplating buying Fasten at a price of \$50 and paying \$25 per period for checks, versus paying \$50 for Czechwriter and paying \$20 for checks. If the functionality of the software is identical, which will the consumer buy? Czechwriter.  

**公式内容：**  
- \(x / 0.10 = 250\) → \(x = 25\)  
- \(PV = 5 / 0.10 = 50\)  
- \(x / 0.10 = 250 + 100\) → \(x = 35\)  
- \(PV = 150\)  

---

#### 2. 结合上文知识点的详细解析  
##### (1) 定价边界与切换成本的精准捕捉  
- **(d) 和 (e) 部分**：  
  - 当检查价格 \(p_2 = 22\) 时，继续使用 Fasten 的现值 \(= 22 / 0.10 = \$220\)，低于切换成本 \(\$250\)（上文已验证：\(\$50\) 软件费 \(+ 20 / 0.10 = \$250\)），因此顾客不切换。  
  - 无差异价格 \(x = 25\) 由方程 \(x / 0.10 = 250\) 确定，即 \(p_2\) 的临界点满足 **利润现值等于消费者切换成本的固定部分**（\(\$50\) 软件费）。  
  - **与上文连续性**：  
    此临界值直接体现 \(p_2\) 作为唯一有效变量的核心逻辑。上文指出，\(p_1\)（初始产品价）无效，因二手市场对冲机制使总销量仅由 \(p_2\) 决定；此处耗材价格 \(p_2\) 同样主导长期利润边界，企业需精确控制 \(p_2\) 以匹配消费者切换成本的现值阈值。

##### (2) 利润捕获机制与切换成本的同构性  
- **(f) 和 (h) 部分**：  
  - 最高不切换价格对应的利润现值 \(PV = 5 / 0.10 = 50\)（无转换成本时）或 \(PV = 150\)（含转换成本时），与“消费者切换成本固定部分”完全相等：  
    - 无转换成本：利润现值 \(\$50\) = 切换成本固定部分（\(\$50\) 软件费）。  
    - 含转换成本：利润现值 \(\$150\) = 新切换成本固定部分（\(\$50\) 软件费 \(+ \$100\) 转换费）。  
  - **微观机制**：  
    企业通过设置 \(p_2\) 使消费者无差异（\(p_2 / r = \text{切换成本现值}\)），利润现值精确等于切换成本中的固定支出部分，即：  
    \[
    \text{利润现值} = \frac{p_2 - c}{r} = F
    \]  
    其中 \(F\) 为固定切换成本（如软件费），\(c = 20\) 为耗材边际成本，\(r = 0.10\) 为贴现率。  
  - **与上文连续性**：  
    此机制与上文二手市场逻辑同源——上文净成本公式 \(p_1 - 0.4p_2\) 体现 \(p_1\) 被对冲而无效；此处 \(p_2\) 则成为利润捕获的唯一切入点，固定部分 \(F\) 相当于上文的 \((p_1 - p_2)\) 项无效化后留下的利润控制锚点（如上文利润函数中仅 \(p_2\) 项有效）。

##### (3) 异质转换成本对价格边界的影响  
- **(g) 和 (h) 部分**：  
  - 额外转换成本 \(\$100\) 将切换成本固定部分从 \(\$50\) 提升至 \(\$150\)，导致最高可行价格从 \(x = 25\) 上升至 \(x = 35\)（方程 \(x / 0.10 = 250 + 100\)）。  
  - **关键含义**：  
    转换成本的增加扩大了 \(p_2\) 的有效定价空间，验证上文“企业利润管理聚焦唯一价格变量 \(p_2\)”的结论——切换成本的任何变动仅影响 \(p_2\) 的临界值，不改变其主导地位。  
- **(i) 部分**：  
  - 消费者选择 Czechwriter，因总现值成本较低（Fasten: \(50 + 25/0.10 = \$300\)；Czechwriter: \(50 + 20/0.10 = \$250\)）。  
  - **与上文延伸关联**：  
    消费者决策仅取决于耗材价格现值（\(p_2\) 项），与初始软件价格（\(p_1\) 等效）无关，再次证实 **\(p_2\) 是需求动态的核心驱动因子**——如同上文二手市场中总销量函数 \(14,000 - 180p_2\) 仅由 \(p_2\) 决定。

> **知识衔接点**：当前图片深化了上文互补品定价框架：  
> - \(p_2\) 的临界值（\(x = 25\) 或 \(x = 35\)）是企业锁定利润的唯一杠杆，其变动由切换成本固定部分精确决定；  
> - 利润现值与切换成本固定部分的相等性，揭示上文“\(p_1\) 无效”的微观根源——次要变量（如软件初始价）仅改写 \(F\)，但利润边界始终由 \(p_2\) 调控。  
> 此逻辑完全延续上文核心：**企业只需瞄准 \(p_2\) 定价，无需关注 \(p_1\) 的表面波动，因总量与利润刚性由 \(p_2\) 独立维持。**

---
### Page/Slide 11



### 当前图片分析

#### 1. 提取文字与公式  
- **(j) 部分**  
  - 文字：*Intoot decides to distribute a coupon that offers a discount of $50 off of the regular purchase price. What price would it have to set to make consumers indifferent between purchasing Fasten and Czechwriter?*  
  - 公式：`Solve \( 50 + 25/.10 - d = 50 + 20/.10 \) to find that the discount should be $50.`  

- **(k) 部分**  
  - 文字：*Suppose that consumers are shortsighted and only look at the cost of the software itself, neglecting the cost of the checks. Which program would they buy if Intoot offered this coupon? Fasten. How might Czechwriter respond to the Fasten offer? Issue its own coupon for $50 and raise the price of its checks to $35.*  

- **34.9 (2) 部分**  
  - 文字：*Sol Microsystems has recently invented a new language, Guava, which runs on a proprietary chip, the Guavachip. The chip can only be used to run Guava, and Guava can only run on the Guavachip. Sol estimates that if it sells the chip for a price \( p_c \) and the language for a price \( p_g \), the demand for the chip-language system will be*  
  - 公式：\( x = 120 - (p_c + p_g) \)  

- **(a) 部分**  
  - 文字：*Sol initially sets up two independent subsidiaries, one to produce the chip and one to produce the language. Each of the subsidiaries will price its product so as to maximize its profits, while assuming that a change in its own price will not affect the pricing decision of the other subsidiary. Assume that marginal costs are negligible for each company. If the price of the language is set at \( p_g \), the chip company’s profit function (neglecting fixed costs) is*  
  - 公式：\( [120 - p_c - p_g] p_c \)  

- **(b) 部分**  
  - 文字：*Differentiate this profit function with respect to \( p_c \) and set the result equal to zero to calculate the optimal choice of \( p_c \) as a function of \( p_g \).*  
  - 公式：\( p_c = 120 - 2p_g \)  

- **(c) 部分**  
  - 文字：*Now consider the language subsidiary’s pricing decision. The optimal choice of \( p_g \) as a function of \( p_c \) is*  
  - 公式：\( p_g = 120 - 2p_c \)  

- **(d) 部分**  
  - 文字：*Solving these two equations in two unknowns, we find that \( p_c = 40 \) and \( p_g = 40 \), so that \( p_c + p_g = 80 \).*  

---

#### 2. 结合上文的详细解析  

##### (1) 消费者无差异条件与短视行为的定价动态  
- **(j) 和 (k) 部分的核心含义**：  
  - 公式 \( 50 + 25/.10 - d = 50 + 20/.10 \) 延续上文 **切换成本现值的消费者决策逻辑**：  
    - \( 50 \) 为固定软件成本（等效上文 \(\$50\) 软件费），\( 25/.10 \) 和 \( 20/.10 \) 对应耗材价格 \( p_2 \) 的现值（等效上文 \( p_2 / r \)），折扣 \( d \) 模拟针对初始价格的变动。  
    - 外部补贴（如优惠券）仅影响短期支付，但消费者无差异点仍由 \( p_2 \) 现值主导：企业需通过调整补贴 \( d \) 对冲 \( p_2 \) 差异（此处 \( d = 50 \) 使总成本现值相等）。  
    - **与上文连续性**：验证上文“\( p_2 \) 是唯一有效价格变量”的结论——补贴属于 \( p_1 \) 侧变动，但企业利润边界仍由 \( p_2 \) 决定；短期策略（如优惠券）无法改变长期利润现值，仅转移价格杠杆的显性表现。  
  - **(k) 部分短视行为**：消费者忽略检查成本（\( p_2 \) 项），导致选择基于软件价格的错误决策（选择 Fasten）。  
    - Czechwriter 的回应策略（发优惠券并提升耗材价至 \(\$35\)) 精准体现 **上文利润捕获机制**：当消费者短视时，企业可放大 \( p_2 \) 利润空间（\( \$35 \times 10 = \$350 \) 现值），使切换成本尚可接受（上文切换成本现值 \( \$250 \) 现被超越），但需预防背叛风险。  
    - **关键延伸**：短视行为暴露市场失灵，企业需通过耗材价格动态（而非软件补贴）维持长期利润，呼应上文“企业无需关注 \( p_1 \) 表面波动”。  

##### (2) 互补品双边际化与总价格的主导性  
- **34.9 (2) 部分的核心含义**：  
  - 需求函数 \( x = 120 - (p_c + p_g) \) 表明系统需求仅由 **总价格 \( P = p_c + p_g \)** 决定，等效上文“总销量仅由 \( p_2 \) 决定”：  
    - 这里 \( P \) 集中体现互补品绑定特性，类似上文 \( p_2 \) 作为耗材价格锚点，而 \( p_c \) 或 \( p_g \) 单独变动（如上文的 \( p_1 \)) 仅改写价格分配，不改变核心边界。  
  - 独立子公司定价（(b)-(d)）导致 **双边际化**：  
    - 芯片公司求解 \( p_c = 120 - 2p_g \)（(b)）与语言公司 \( p_g = 120 - 2p_c \)（(c)），均衡总价格 \( P = 80 \)。  
    - 若一体化，企业应设 \( P^* = 60 \)（垄断最优：\( \max (120 - P)P \Rightarrow P = 60 \))，但独立定价使 \( P = 80 > 60 \)，需求压缩至 \( x = 40 \)（对比如上文总销量刚性依赖核心变量）。  
    - **与上文同构性**：  
      - 双边际化效应等同上文“二手市场对冲机制”——子公司间外部性导致 \( p_c \) 和 \( p_g \) 分散定价效率低下，恰似 \( p_1 \) 因对冲而无效。  
      - 最终 \( p_c + p_g = 80 \) 的刚性结果，揭示 **利润边界仅由总价格 \( P \) 决定**，但分割定价扭曲其分配；验证上文“利润现值与切换成本固定部分相等”的微观根源，即企业需通过单一变量（此处 \( P \)，等效上文 \( p_2 \)) 捕获全部利润。  
  - **策略启示**：企业应避免子公司独立定价，转向集中控制总价格 \( P \)，如同上文聚焦 \( p_2 \) 而非 \( p_1 \)。  

> **知识衔接点**：当前图片双重印证上文核心逻辑——  
> - (j)-(k) 显示 Price 侧扰动（如优惠券）无法撼动 \( p_2 \) 的利润主导地位，仅强化消费决策对切换成本现值的敏感性；  
> - Sol 案例揭示互补品定价中总价格的不可分割性，独立变量 \( p_c \) 或 \( p_g \) 的变动如上文 \( p_1 \)，仅作为“固定切换成本重分布”载体，而利润边界刚性锁定于系统级价格（等效 \( p_2 \))。  
> 此分析延续上文结论：**企业必须将价格策略锚定于需求动态的核心驱动因子（\( p_2 \) 或总价格 \( P \))，外部价格工具仅辅助而不改变长期利润结构。**

---
### Page/Slide 12



### 当前图片内容提取  
#### 文字与公式  
1. **Sol Microsystems 案例**  
   - (e) Sol Microsystems 决定独立子公司系统繁琐，因此设立 Guava Computing 销售芯片与语言的捆绑系统。设 $ p $ 为捆绑价格。Guava Computing 的利润函数为：  
     $$[120 - p]p$$  
   - (f) 对利润函数关于 $ p $ 求导并设为零：  
     $$p = 60$$  
   - (g) 集成系统价格 vs. 独立子公司：  
     - 价格更低：**Integrated system**  
     - 对消费者更优：**Integrated system**  
     - 利润更高：**Integrated system**  

2. **South Belgium Press 案例（34.10 (2)）**  
   - 背景：South Belgium Press 出版期刊 *Nano-economics* 和 *Gigaeconomics*，每期刊年订阅费 \$1,000。200 所顶尖大学均订阅两本，每所年付费 \$2,000。按显示偏好，图书馆对每期刊支付意愿至少 \$1,000。  
   - (a) 大学结对共享期刊后：  
     - 每对中一校订阅 *Nano-economics*，一校订阅 *Gigaeconomics*，无增量成本。  
     - 每期刊销售量：**100**  
   - (b) South Belgium 提升单期刊价格上限：  
     - 可提至 **\$2,000**，因图书馆已表明愿为期刊对支付该总额。  
   - (c) 新旧方案对比：  
     - 图书馆支出与收入：**They remain the same**  

---

### 结合上文的详细解析  
#### 1. Sol Microsystems 案例与【上文知识点总结】的衔接  
- **公式 $[120 - p]p$ 的经济学含义**：  
  需求函数隐含为 $ x = 120 - p $，对应【上文】中互补品总需求由系统级价格 $ P $ 决定的逻辑（即 $ x = 120 - (p_c + p_g) $）。此处 $ p $ 直接等价于 **总价格 $ P $**，验证了“需求仅由总价格驱动”的核心结论。  
- **$ p = 60 $ 的求解逻辑**：  
  通过 $\frac{d}{dp} [ (120 - p)p ] = 0$ 得垄断最优 $ P^* = 60 $，与【上文】34.9(2) 部分一致：  
  > *“一体化时企业应设 $ P^* = 60 $（垄断最优），而独立子公司定价使 $ P = 80 > 60 $”*  
  此结果直接体现 **双边际化问题的解决**——集成系统通过消除子公司间外部性，将总价格降至社会最优水平，避免独立定价导致的需求压缩（$ x = 40 $ 时 $ P = 80 $）和利润损失。  
- **(g) 三点结论的深层含义**：  
  - **价格更低**：集成系统 $ p = 60 < $ 独立系统隐含总价格 $ 80 $，证明分割定价（如 $ p_c, p_g $）会扭曲价格分配，而总价格锚点 $ P $ 是唯一有效变量。  
  - **消费者更优**：低总价格提升需求（$ x = 60 $ vs. $ x = 40 $），呼应【上文】“企业无需关注 $ p_1 $ 表面波动”——消费者福利取决于系统级价格而非组件价格。  
  - **利润更高**：利润 $ \pi = (120 - 60) \times 60 = 3600 $ 超越独立系统（$ \pi = (120 - 80) \times 40 = 1600 $），印证 **“利润边界刚性锁定于总价格 $ P $”** 的微观根基：利润现值仅由需求曲线和 $ P $ 决定，外部价格工具（如分割定价）无法提升长期利润。  

#### 2. South Belgium Press 案例与【上文知识点总结】的呼应  
- **(a) 结对共享机制的经济学本质**：  
  - 200 所大学结对后每期刊销量降至 **100**，等效于【上文】短视消费者忽略检查成本（$ p_2 $ 项）导致需求转移。此处大学通过共享 **内化了互补品外部性**，类似【上文】“二手市场对冲机制”——免费共享使单期刊有效价格被稀释，但总价格 $ P $（每对 \$2,000）仍主导消费者决策。  
  - 该行为暴露市场失灵：若允许自由共享，企业面临“收入流失”（即【上文】中 Czechwriter 的“背叛风险”），迫使企业调整定价策略。  
- **(b) 单价提升至 \$2,000 的必然性**：  
  - South Belgium 将单期刊价格提至 \$2,000，但图书馆总支付额保持 \$2,000 不变，直接验证 **总价格 $ P $ 的不可分割性**：  
    > *“单个价格变动（如 $ p_c $ 或 $ p_g $）仅改写价格分配，不改变核心边界”*  
  - 价格上限 \$2,000 源于消费者对互补品对的总支付意愿，印证【上文】“利润边界由总价格决定”——企业无法通过分割价格创造额外利润，只能通过重分配捕获已存在的支付意愿。  
- **(c) 收入不变的深层逻辑**：  
  - 新方案中图书馆总支出与企业收入均未变化，完美重演【上文】核心结论：  
    > *“企业无需关注 $ p_1 $ 表面波动，仅需锚定核心驱动因子（此处等效总价格 $ P $）”*  
  - 收入刚性源于短视行为（大学误判单期刊价值）和互补品特性，企业通过动态调整单价格对冲外部性，但 **长期利润现值仍被锁定于消费者总支付意愿**（\$2,000/对），与 【上文】“利润捕获机制”完全同构。  

---

### 知识连续性总结  
- **双重印证总价格主导性**：  
  Sol 案例通过集成捆绑实现 $ P^* = 60 $，South Belgium 案例通过单价格提升维持 $ P = \$2,000 $，二者均证明 **分割价格（$ p_1 $ 或 $ p_c, p_g $）仅为“固定成本重分布载体”，而总价格 $ P $ 是需求动态的唯一内生锚点**。  
- **策略启示延伸**：  
  企业必须放弃独立定价（如子公司或单期刊销售），转向集中控制总价格——这既规避了【上文】双边际化导致的效率损失，又防止短视消费者行为引发的利润流失。所有价格变动仅服务于利润重分配，无法改变长期利润结构，呼应【上文】标量 $ p_2 $ 作为 “利润边界刚性锁定器” 的核心机制。

---
### Page/Slide 13



### 1. 图片文字提取  
```plaintext
NAME________________ 421
(d) If there were a cost of interlibrary loan, how would your answer change? Assuming they still bought both journals, libraries would be worse off since they would have to pay the transactions cost for interlibrary loan.
```  
- **无公式**：图片中仅含纯文本，无数学表达式或图表。

---

### 2. 经济学解析（结合上文知识点）  
#### 核心机制：交易成本对消费者福利的侵蚀  
- **交易成本显性化 vs. 短视消费者行为**：  
  上文明确指出，**短视消费者会忽略显性交易成本（如 $ p_2 $ 项）**（见South Belgium案例(a)部分），导致需求转移至共享机制（如大学结对共享）。但本问题中，馆际互借成本被**强制支付且不可忽略**（"they would have to pay"），直接降低消费者净剩余。这**强化了上文“消费者福利取决于系统级净支付成本”的隐含逻辑**：  
  - 系统级总价格 $ P $ 仍主导基础需求（如South Belgium中 $ P = \$2,000 $ 对应总支付意愿），但**显性交易成本独立于 $ P $ 且无法被企业定价对冲**，导致消费者实际负担成本 $ P + \text{transaction cost} $。  
  - 若消费者"still bought both journals"，表明总支付意愿 $ P $ 未变（企业未调整定价），但**额外交易成本从消费者剩余中直接扣除**，印证上文"利润边界刚性锁定于总价格 $ P $"的深层含义——企业无法通过价格重分配消除外部成本，仅能捕获固定支付意愿。  

- **与双边际化问题的呼应**：  
  上文分析分割定价（如 $ p_c, p_g $）时，指出独立系统因外部性推高总价格至 $ P = 80 $（导致需求压缩至 $ x=40 $）。本场景中，交易成本可视为**新引入的外部性**：  
  - 若图书馆因互借成本减少期刊购买（但问题假设"still bought"），需求曲线将左移，**等效于总价格 $ P $ 暗中上升**（需求函数隐含 $ x = 120 - P_{\text{effective}} $，其中 $ P_{\text{effective}} = P + \text{cost} $）。  
  - 但因消费者坚持购买，需求未变，**仅福利受损**，这验证了上文"(g) 结论"中"消费者更优"的逆命题——当 $ P $ 不变但交易成本增加时，消费者必然恶化，而企业利润不受影响（因收入仍由 $ P $ 锚定）。  

#### 策略启示延伸  
- **企业定价支配权的边界**：  
  上文强调企业可通过单价格重分配（如South Belgium提价至 $ \$2,000 $）维持 $ P $ 不变，但**交易成本在企业控制范围之外**。企业若未内化此成本（如提供免费互借），将导致：  
  - 消费者剩余下降 → 长期需求弹性增大（隐含需求函数 $ x = 120 - p $ 的截距左移），虽不改变短期利润（因 $ P $ 未变），但削弱市场可持续性。  
  - 这呼应上文“背叛风险”逻辑：外部成本扭曲消费者效用，迫使企业需通过捆绑或集成（如Sol案例中系统级定价）部分抵消，否则面临隐性需求流失。  
- **知识连续性落脚点**：  
  本问题实为上文“利润边界刚性”的**反向验证**——当交易成本显性且固定时，无论企业如何重新分配组件价格（$ p_c, p_g $ 或单期刊价），**总利润现值仍严格由 $ P $ 和外部成本结构决定**。消费者福利差异仅反映净支付成本变化，而企业决策核心仍为“锚定 $ P $ 以捕获支付意愿”。

---
### Page/Slide 14



### 1. 图片文字提取  
```plaintext
422 INFORMATION TECHNOLOGY (Ch. 34)
```  
- **无公式**：仅含章节标题与页码，无数学表达式或图表。

---

### 2. 经济学解析（结合上文知识点）  
#### 章节定位与理论衔接  
- **信息经济学语境下的价格刚性验证**：  
  此页属于信息经济学（*Information Technology*）章节，直接承接上文 **"总价格 $ P $ 作为需求动态唯一内生锚点"** 的核心结论。信息商品（如数字期刊、软件）具有**高固定成本、低边际成本**的典型特征，其定价策略更易暴露分割价格失效机制：  
  - 若采用子系统分割定价（如分模块收费），企业将面临**双重边际化**（*double marginalization*），导致有效总价格 $ P_{\text{effective}} > P_{\text{optimal}} $（上文案例中 $ P_{\text{effective}} = 80 $ vs. $ P_{\text{optimal}} = 60 $），直接压缩需求规模。  
  - 而集中控制总价格 $ P $ 可规避此问题，使信息商品市场维持 $ x = 120 - P $ 的原始需求关系（如上文Sol案例中通过系统级定价维持 $ P = \$2,000 $ 支付意愿）。

- **交易成本的系统性影响强化**：  
  本章节标题隐含对**非价格摩擦**（如互借成本、数据传输延迟）的分析，与上文(d)中交易成本侵蚀消费者剩余的逻辑形成递进：  
  - 信息商品的交易成本（如版权认证、格式转换）具有**规模不敏感性**，其增量成本对消费者剩余的削减效应远强于实体商品（$ \Delta CS = -\text{transaction cost} \times \text{volume} $）。  
  - 企业若未能集成此类成本（如提供一站式平台服务），将导致**有效支付意愿 $ P_{\text{willing}} $ 下移**，但总利润边界仍刚性锁定于企业可控部分（$ P_{\text{collected}} $），呼应上文"利润分配仅取决于系统级定价权"的论断。

#### 知识连续性落脚点  
- 该章节内容实为上文理论的**实践场域延伸**：信息商品市场的分割定价失效风险更高（因消费者对价格敏感度与交易摩擦高度耦合），进一步论证  
  > **"所有价格变动仅服务于利润重分配，无法改变长期利润结构"**。  
  企业需放弃多节点定价权（如云服务中的功能模块拆分），将系统级总价格 $ P $ 作为需求管理的唯一杠杆，直接规避外部成本导致的隐性利润流失。
