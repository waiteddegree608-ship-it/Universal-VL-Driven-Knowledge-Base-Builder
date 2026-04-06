# PDF_Chapter_35

### Page/Slide 1



### 1. 提取文字与公式  
#### 章节标题  
- **Chapter 35**  
- **Public Goods**  

#### 引言核心内容  
- 私人商品（private goods）具有排他性（如三明治不可同时被两人消费），而公共物品（public goods）可联合消费（如观赏烟花）。  
- 私人商品效率条件：消费者间边际替代率（MRS）相等；  
- 公共物品效率条件：**所有消费者MRS绝对值之和等于公共物品的边际成本**（以私人商品衡量）。  

#### 例题文字与公式  
- **效用函数**：$ U(X_i, G) = X_i + A_i G - B_i G^2 $  
  - $ X_i $：个人 $ i $ 用于私人商品的支出  
  - $ G $：小镇用于公共物品（街道维护）的总支出  
- **Pareto最优条件推导**：  
  1. 公共物品边际效用 = $ A_i - B_i G $  
  2. 所有消费者MRS绝对值之和：  
     $$
     \sum_i (A_i - B_i G) = \sum_i A_i - \left( \sum_i B_i \right) G
     $$  
  3. 效率要求：$ \sum_i A_i - \left( \sum_i B_i \right) G = 1 $（因公共/私人商品价格比为1，边际成本=1）  
  4. 解得最优支出：  
     $$
     G = \frac{\sum_i A_i - 1}{\sum_i B_i}
     $$  

#### 习题编号  
- **35.1 (0)**: Muskra, Ontario小镇问题（1,000人，私人商品为Labatt’s ale，公共物品为滑冰场）  

---

### 2. 公式与逻辑解析  
#### （1）效用函数的经济含义  
- **$ A_i G $**：公共物品带来的正向边际效用（规模效应）  
- **$ -B_i G^2 $**：公共物品过度供给的负向效应（如街道过度修缮导致资源浪费）  
- **$ X_i $** 与 $ G $ 的线性关系：私人消费与公共支出相互独立，符合局部公用品模型假设  

#### （2）效率条件推导的关键逻辑  
- **区别于私人商品**：  
  - 私人商品：消费者间MRS相等（$ \text{MRS}_i = \text{MRS}_j $）；  
  - 公共商品：**MRS之和等于边际成本**（$ \sum_i |\text{MRS}_i| = \text{MC}_G $）。  
- **本例特殊性**：  
  - 公共/私人商品以美元计价（价格比=1），故边际成本简化为1；  
  - 通过求解 $ \sum_i (A_i - B_i G) = 1 $，将分散的个人偏好（$ A_i, B_i $）整合为社会最优 $ G $。  

#### （3）参数 $ G $ 的经济解释  
- $ \sum_i A_i $：社会对公共物品的总需求强度  
- $ \sum_i B_i $：公共物品供给的边际成本增速  
- 分子 $ \sum A_i - 1 $：当社会需求超过单位成本时，才值得提供公共物品（体现非负供给条件）  

---

### 3. 与上文知识点的衔接  
- **承接”公共物品效率条件“**：  
  上文指出“公共物品效率要求MRS之和等于边际成本”，本例通过**具体数学形式**验证：  
  - $ \sum \text{MRS}_i = \text{MC}_G $ → $ \sum (A_i - B_i G) = 1 $；  
  - 体现“联合消费”特性：单个消费者无需单独承担全部成本，但总支付意愿必须覆盖边际成本。  
- **拓展”公共物品供给机制“**：  
  公式 $ G = \frac{\sum A_i - 1}{\sum B_i} $ 暗示：  
  1. 若 $ \sum A_i \leq 1 $，则 $ G^* = 0 $（无公共物品供给）；  
  2. 人口规模（5,000人）通过 $ \sum A_i $ 线性放大公共物品需求，体现规模效应。

---
### Page/Slide 2



### 1. 提取文字与公式  
#### 章节标识  
- **424 PUBLIC GOODS (Ch. 35)**  

#### 效用函数与参数  
- 效用函数：$ U(X_i, G) = X_i - 100/G $  
  - $ X_i $：公民 $ i $ 消费的 Labatt’s ale 瓶数  
  - $ G $：小镇滑冰场面积（单位：平方米）  
- 价格：Labatt’s ale 价格为 \$1/瓶，滑冰场价格为 \$10/平方米  
- 收入：每位居民年收入 \$1,000  

#### (a) 部分  
- 边际替代率（MRS）绝对值表达式：$ 100/G^2 $  
- 滑冰场额外一平方米的边际成本（以 ale 衡量）：$ 10 $  

#### (b) 部分  
- 效率条件方程：$ 1,000 \frac{100}{G^2} = 10 $  
- Pareto 最优解：$ G = 100 $  

#### (c) 部分  
- 滑冰场总支出：$ \$10G $  
- 个人税单：$ \frac{10G}{1,000} = G/100 $  
- 个人可负担 ale 量：$ 1,000 - G/100 $  

#### (d) 部分  
- 选民预算约束：$ X_i + G/100 = 1,000 $  
- 选民效用最大化结果：$ G = 100 $  

#### (e) 部分  
- 选民需求与 Pareto 最优比较：**The same**  

#### (f) 部分（截断）  
- 安大略省文化委员会补贴滑冰场成本的 50%，成本由全省公民分担；因多镇受益，需增加全省税收。  

---

### 2. 公式与逻辑解析  
#### （1）效用函数与 MRS 的经济含义  
- **$ U(X_i, G) = X_i - 100/G $**：  
  - $ X_i $ 为私人商品消费，$ G $ 为公共物品供给；  
  - $ -100/G $ 项体现公共物品的**正边际效用递减**（$ G $ 增大时，效用递增但增速放缓），与上文二次项 $ -B_i G^2 $ 逻辑一致，但此处为非线性递减形式。  
- **MRS $(100/G^2)$**：  
  - 表示个人为获得 1 单位 $ G $ 愿意放弃的 $ X_i $ 数量（即边际支付意愿）；  
  - $ 100/G^2 $ 随 $ G $ 增大而减小，反映公共物品消费的**饱和效应**（供给越多，边际效用损失越低）。  

#### （2）效率条件推导的核心逻辑  
- **Pareto 最优条件**：$ \sum_i |\text{MRS}_i| = \text{MC}_G $  
  - 总边际支付意愿：1,000 人相同，故 $ \sum_i |\text{MRS}_i| = 1,000 \times (100 / G^2) $；  
  - 社会边际成本：滑冰场价格 \$10/平方米，以 ale 衡量为 $ \$10 / \$1 = 10 $ 瓶/平方米；  
  - 联立得 $ 1,000 \times (100 / G^2) = 10 $，解出 $ G^* = 100 $。  
- **关键对比**：  
  - 此处 $ \sum_i |\text{MRS}_i| $ 直接等于 MC，无需上文 $ \sum A_i - \sum B_i G = 1 $ 的线性形式，但逻辑等价：均体现“社会总支付意愿覆盖边际成本”原则。  
  - 民众规模（1,000 人）通过 $ \sum_i |\text{MRS}_i| $ **线性放大社会需求**，验证上文“人口规模通过 $ \sum A_i $ 线性影响最优供给”。  

#### （3）投票机制与结果的内在一致性  
- **个人预算约束 $ X_i + G/100 = 1,000 $**：  
  - 税单 $ G/100 $ 将社会成本内部化（个人边际成本 $ \partial (\text{tax}) / \partial G = 1/100 $），使个人面临有效价格；  
  - 选民效用最大化问题：$ \max_G \left( (1,000 - G/100) - 100/G \right) $，一阶条件 $ -1/100 + 100/G^2 = 0 $，解得 $ G = 100 $。  
- **投票与最优解一致**：  
  - 由于个人充分承担相应成本份额（$ G/100 $），其投票行为 **内化了公共物品的外部性**，直接导向社会最优；  
  - 与上文公共物品供给机制呼应：当成本分担透明时，民主决策可实现效率。  

---

### 3. 与上文知识点的衔接  
- **效率条件的具体实践**：  
  - 上文抽象条件 $ \sum_i |\text{MRS}_i| = \text{MC}_G $ 在此例中具象化为 $ 1,000 \times (100/G^2) = 10 $，验证“联合消费下社会边际支付意愿需覆盖边际成本”；  
  - 当 $ \sum_i |\text{MRS}_i| < \text{MC} $（如 $ G > 100 $），供给过剩，体现上文“$ \sum A_i \leq 1 $ 时 $ G^* = 0 $”的扩展（此处 $ G^* = 100 > 0 $ 表明总支付意愿超边际成本）。  
- **公共物品供给机制的实证支持**：  
  - (d) 部分证明：**成本分担透明性是投票有效性的关键**，与上文“总支付意愿必须覆盖边际成本”一致；  
  - (e) 结论“same”强化上述观点，说明避免“搭便车”需机制设计（如本例中的等额分担），但不同于纳什均衡，此机制直接实现帕累托最优，为上文理论提供操作路径。  
- **补贴效应的预示（衔接 (f)）**：  
  - 若省级补贴导致个人边际成本降低（如 $ G/100 $ 变为 $ G/200 $），选民需求将上移，引发过度供给风险；  
  - 呼应上文“公共物品供给对价格敏感”，但跨辖区成本分摊可能破坏本地效率，为后续章节外部性讨论埋下伏笔。

---
### Page/Slide 3



### 提取内容（当前图片）

#### 文字与公式提取
- **滑冰场投票问题（相关部分）**  
  - 文本：*"is collected, so that the effect of an increase in expenditures in Muskrat on the taxes its citizens have to pay to the state can be safely neglected. Now, approximately how large a skating rink would citizens of Muskrat vote for? $ G = 100\sqrt{2} $. (Hint: Rewrite the budget constraint for individuals observing that local taxes will be only half as large as before and the cost of increasing the size of the rink only half as much as before. Then solve for the utility-maximizing combination.)"*  
  - 问题：*(g) Does this subsidy promote economic efficiency? No.*  

- **35.2 问题**  
  - 文本：*"Ten people have dinner together at an expensive restaurant and agree that the total bill will be divided equally among them."*  
  - (a) *What is the additional cost to any one of them of ordering an appetizer that costs \$20? \$2.*  
  - (b) *Explain why this may be an inefficient system. Each pays less than full cost of own meal, so all overindulge.*  

- **35.3 问题**  
  - 文本：*"Cowflop, Wisconsin, has 1,000 people. Every year they have a fireworks show on the Fourth of July. The citizens are interested in only two things—drinking milk and watching fireworks. Fireworks cost 1 gallon of milk per unit. People in Cowflop are all pretty much the same. In fact, they have identical utility functions. The utility function of each citizen $ i $ is $ U_i(x_i, g) = x_i + \sqrt{g}/20 $, where $ x_i $ is the number of gallons of milk per year consumed by citizen $ i $ and $ g $ is the number of units of fireworks exploded in the town’s Fourth of July extravaganza. (Private use of fireworks is outlawed.)"*  
  - (a) *Solve for the absolute value of each citizen’s marginal rate of substitution between fireworks and milk. $ 1/(40\sqrt{g}) $.*  
  - (b) *Find the Pareto optimal amount of fireworks for Cowflop. 625.*  

- **35.4 问题（部分截断）**  
  - 文本：*"Bob and Ray are two hungry economics majors who are sharing an apartment for the year. In a flea market they spot a 25-year-old sofa that would look great in their living room. Bob’s utility function is $ u_B(S, M_B) = (1 + S)M_B $, and Ray’s utility function is $ u_R(S, M_R) = (2 + S)M_R $. In these expressions $ M_B $ and $ M_R $ are the amounts of money that Bob and Ray have to spend on other goods, $ S = 1 $ if they get the sofa, and $ S = 0 $ if they don’t get the sofa. Bob has $ W_B $ dollars to spend, and Ray has $ W_R $ dollars."*  

---

### 解析（基于上文知识点总结）

#### 1. 滑冰场补贴问题：$ G = 100\sqrt{2} $ 与效率分析
- **公式推导逻辑**：  
  上文知识点指出，无补贴时个人预算约束为 $ X_i + G/100 = 1,000 $，对应边际支付意愿 $ 100/G^2 = 1/100 $，解得 Pareto 最优供给 $ G^* = 100 $。补贴 50% 后，当地税收和成本分担减半，个人有效价格变为 $ p = 1/200 $。  
  - 个人效用最大化条件：$ \text{MRS} = 100/G^2 = p = 1/200 $  
  - 求解：$ G^2 = 100 \times 200 = 20,000 \implies G = 100\sqrt{2} \approx 141.42 $  
  此结果与上文“补贴导致个人边际成本降低，需求上移”一致，验证了 **规模效应通过价格渠道扭曲供给决策**。

- **效率判断（$ g $ 部分）**：  
  - 答案 “No” 源于补贴引发 **过度供给**：社会最优 $ G^* = 100 $，但投票结果 $ G = 100\sqrt{2} > 100 $，表明 $ \sum_i |\text{MRS}_i| < \text{MC}_G $（上文知识点中 $ \sum_i |\text{MRS}_i| = 1,000 \times (100 / G^2) $，当 $ G > 100 $ 时小于 10）。  
  - 这直接衔接上文 “跨辖区补贴破坏本地效率” 的预示：补贴使成本分担模糊，丧失 (d) 部分中“成本分担透明性”的效率机制，强化了 **外部性未内化时民主决策失效** 的结论。

#### 2. 35.2 问题：分摊账单与低效成因
- **$2 额外成本的逻辑**：  
  10 人平摊 \$20 开胃菜成本，个人边际支出为 $ 20/10 = \$2 $。这体现了 **成本共享对私人物品的扭曲**：个人 $ \text{MC} $ 低于社会成本（\$20），与上文公共物品的“搭便车”原理同构（但针对私人物品）。  
  - 类似上文 MRS 分析：当个人承担成本比例 $ \alpha < 1 $，边际支付意愿虚高，导致 $ G_{\text{实际}} > G^* $。

- **低效本质（部分 b）**：  
  *“Each pays less than full cost of own meal, so all overindulge”* 直接对应上文 “个人边际成本降低引发过度消费”。  
  - 此案例实证了 **公共物品供给对价格敏感的核心机制**：即便私人物品，若成本分担设计不当（如 $ \alpha $ 远小于 1），同样导致 **边际成本与社会成本脱钩**，符合上文“避免搭便车需机制设计”的延伸（此处机制暴露外部性）。

#### 3. 35.3 问题：烟花的 Pareto 最优解
- **MRS 公式**：  
  $ | \text{MRS}_i | = 1/(40\sqrt{g}) $ 源于效用函数 $ U_i = x_i + \sqrt{g}/20 $：  
  - $ \mu_{g} = \frac{\partial U_i}{\partial g} = \frac{1}{40\sqrt{g}} $, $ \mu_{x_i} = 1 \implies |\text{MRS}| = \mu_g / \mu_{x_i} = 1/(40\sqrt{g}) $.  
  此形式延续上文非线性递减逻辑（对比 $ U = X_i - 100/G $），但此处 $ \sqrt{g} $ 导致 MRS 随 $ g $ 递减更缓，反映 **公共物品效用增长的次线性特征**。

- **Pareto 最优供给 $ g = 625 $ 的推导**：  
  - 社会总支付意愿：1,000 人相同，$ \sum_i |\text{MRS}_i| = 1,000 \times \frac{1}{40\sqrt{g}} $.  
  - 社会边际成本 $ \text{MC}_g = 1 $（烟花以牛奶计价，1 单位 = 1 加仑牛奶）。  
  - 效率条件：$ \frac{1,000}{40\sqrt{g}} = 1 \implies \sqrt{g} = 25 \implies g = 625 $.  
  此结果 **量化验证** 了上文核心等式 $ \sum_i |\text{MRS}_i| = \text{MC}_G $，且与上文对比：  
  - 规模效应：1,000 人使社会需求线性放大（$ \sum \text{MRS} \propto N $），呼应 “人口规模通过 $ \sum A_i $ 线性影响最优供给”。  
  - 供给量 $ g = 625 > 0 $ 确认总支付意愿覆盖边际成本，与上文“$ \sum A_i > 1 $ 时 $ G^* > 0 $”逻辑一致。

#### 4. 与上文衔接的关键点
- **补贴效率的实证强化**：滑冰场案例证明，50% 补贴虽使个人 $ G = 100\sqrt{2} $，但 $ G^* = 100 $ 要求 $ \sum |\text{MRS}| = \text{MC} $，补贴导致实际 $ \sum |\text{MRS}| = 1,000 \times (100 / (20,000)) = 5 < 10 = \text{MC} $，直接体现 **补贴加剧供给不足（相对本地需求）或过度供给（相对社会成本）**，呼应上文“补贴可能引发效率损失”。  
- **机制设计的普适性**：35.2 和 35.3 均展示成本分担方式对效率的决定性作用——  
  - 分摊账单（$ \alpha = 1/10 $）破坏效率，强化上文“搭便车源于成本分担模糊”；  
  - 烟花案例中透明的单人成本（牛奶直接计价）支持上文“机制透明性实现帕累托最优”的结论。  
- **实证案例的递进关系**：35.3 的 $ g = 625 $ 与上文 $ G^* = 100 $ 共同说明——  
  - 无论效用函数形式（$ -100/G $ 或 $ \sqrt{g}/20 $），Pareto 最优条件 $ \sum |\text{MRS}_i| = \text{MC}_G $ 普适成立；  
  - 1,000 人规模在计算中线性放大需求，无缝衔接上文“人口规模通过 $ \sum A_i $ 放大社会需求”的逻辑。

---
### Page/Slide 4



## 解析：习题 35.5 与公共物品效率条件的实证验证

### 1. 文字与公式提取

#### Bob 和 Ray 部分
- **文字**：  
  - (a) Bob 的沙发保留价格：若 $W_B = \$100$，保留价格 $p_B = W_B/2$  
  - (b) Ray 的沙发保留价格：若 $W_R = \$75$，保留价格 $p_R = W_R/3$  
  - (c) 若沙发成本 ≤ \$75，鲍买沙发可实现帕累托改进  

- **公式**：  
  - $W_B = 2(W_B - p_B) \implies p_B = W_B/2$  
  - $2W_R = 3(W_R - p_R) \implies p_R = W_R/3$  

#### Bonnie and Clyde 部分（35.5）
- **文字**：  
  - 总利润 $50H$（$H$ 为共同工作小时数）  
  - $H$ 是两人社区的公共“坏”（public bad）  
  - Bonnie 效用：$U_B(C_B, H) = C_B - .02H^2$；Clyde 效用：$U_C(C_C, H) = C_C - .005H^2$  
  - (a) 边际效用比为 $-.04H$（Bonnie）和 $-.01H$（Clyde）  
  - (b) 补偿额外 1 小时工作的金额 ≈ $.05H$；额外收入 = \$50  
  - (c) 帕累托最优方程 $.05H = 50$；解得 $H = 1,000$  

- **公式**：  
  - $U_B = C_B - 0.02H^2, \quad U_C = C_C - 0.005H^2$  
  - $\text{MRS}_B = -0.04H, \quad \text{MRS}_C = -0.01H$  
  - $\sum |\text{MRS}_i| = 0.05H, \quad \text{补偿方程: } 0.05H = 50$  
  - $H^* = 1,000$  

---

### 2. 公式与上文核心逻辑的衔接

#### (1) Bob/Ray 部分：成本分担对私人物品定价的扭曲
- **保留价格公式隐含 $\alpha < 1$ 的成本分担**：  
  Bob 的 $p_B = W_B/2$ 表明其仅愿支付总价值（$W_B$）的 50%，与上文 **10 人平摊开胃菜成本** 逻辑一致——  
  - 个人边际成本被稀释（如 $\alpha = 1/2$ 时，$p_B$ 仅反映部分社会成本）  
  - 若沙发实为**共同消费的私人物品**（如两人共享），则成本分担导致 $G_{\text{实际}} > G^*$（过度消费），**直接验证成本共享对私人物品的扭曲命题**。

- **帕累托改进阈值 \$75 的实质**：  
  \$75 限值源于 Ray 较低支付能力（$W_R = \$75$），体现上文 **“个人承担成本比例 $\alpha < 1$ 时边际支付意愿虚高”**——  
  - 当 Ray 的 $\alpha$ 隐性设定为 $1/2$（假设两人分摊），其有效支付意愿 $p_R = \$25$ 远低于真实价值 \$75  
  - 沙发成交仅需覆盖 **最低有效支付意愿**（Ray 的 $W_R/3 = \$25$），导致实际交易成本被压低至 $\min(p_B, p_R) = \$25$，**强化上文“搭便车源于成本分担模糊”的结论**。

#### (2) Bonnie and Clyde 部分：公共“坏”的帕累托最优条件
- **效用函数结构的延伸意义**：  
  - $U_i = C_i - kH^2$ 中 $H$ 是**公共坏**（负效用），与上文烟花（公共好）模型 $U_i = x_i + \sqrt{g}/20$ **形式对称**：  
    - 二者均非线性：$H^2$ 导致边际负效用递增，$\sqrt{g}$ 导致边际正效用递减  
    - 验证上文 **“无论效用函数形式，$\sum |\text{MRS}_i| = \text{MC}_G$ 普适”** 的核心论断。  

- **帕累托最优条件的等价推导**：  
  | 概念 | 烟花案例（上文） | Bonnie/Clyde 案例 | 逻辑衔接 |  
  |---|---|---|---|  
  | **社会边际收益** | $\sum |\text{MRS}_i| = 1,000/(40\sqrt{g})$ | $\sum |\text{MRS}_i| = 0.05H$ | 直接线性叠加，呼应 **“人口规模 $N$ 线性放大需求”** |  
  | **社会边际成本** | $\text{MC}_g = 1$（牛奶计价） | $\text{MC}_H = 50$（小时利润） | $H$ 作为生产要素，$50$ 是放弃闲暇的机会成本 |  
  | **最优解** | $1,000/(40\sqrt{g}) = 1 \implies g=625$ | $0.05H = 50 \implies H=1,000$ | **完全复现 $\sum |\text{MRS}_i| = \text{MC}$ 条件**，无论对象是“好”或“坏” |  

- **关键参数的实证价值**：  
  - $\sum |\text{MRS}_i| = 0.05H$ 中的 $0.05 = 0.04 + 0.01$ 体现 **个体 MRS 的加总性质**，对应上文烟花案例中 $1,000/40 = 25$ 的推导  
  - $H^* = 1,000$ 满足 **$\sum |\text{MRS}_i| > 0$ 的可行性条件**，与上文“$\sum A_i > 1$ 时 $G^* > 0$”逻辑一致  
  - **提示句“this model is formally the same...”直接印证上文“机制设计普适性”**：透明计价（劳动力以货币显性度量）使效率条件可实现，呼应上文 **“机制透明性支持帕累托最优”**。

#### (3) 整体方法论：从经验到理论
- **实证案例的递进性**：  
  Bob/Ray 部分聚焦**私人物品的成本分担扭曲**（延续上文 $2 额外成本逻辑），Bonnie/Clyde 部分转向**公共坏的最优提供**——  
  - 二者共同证明：**无论物品类型、效用形式或成本性质**，$\sum |\text{MRS}_i| = \text{MC}$ 是效率的**充分必要条件**  
  - 消除上文潜在质疑：“该条件是否仅适用于典型公共物品？”，**确认理论框架的普适性**（如上文“实证案例递进关系”所述）。

- **补贴效率问题的隐性验证**：  
  若政府强制减少 $H$（如补贴闲暇），则 $\sum |\text{MRS}_i| < \text{MC}$，导致**供给不足**（对比上文补贴滑冰场引发效率损失），**强化“机制设计需匹配 $\sum \text{MRS}$ 与 $\text{MC}$”的结论**。

---
### Page/Slide 5



### 35.6 题目解析：Lucy 与 Melvin 的公共物品配置效率

#### 1. 图片文字与公式提取  
**题目原文**：  
> 35.6 (0) Lucy and Melvin share an apartment. They spend some of their income on private goods like food and clothing that they consume separately and some of their income on public goods like the refrigerator, the household heating, and the rent, which they share. Lucy’s utility function is $2X_L + G$ and Melvin’s utility function is $X_M G$, where $X_L$ and $X_M$ are the amounts of money spent on private goods for Lucy and for Melvin and where $G$ is the amount of money that they spend on public goods. Lucy and Melvin have a total of $8,000$ per year between them to spend on private goods for each of them and on public goods.  
>  
> $(a)$ What is the absolute value of Lucy’s marginal rate of substitution between public and private goods? $1/2$. What is the absolute value of Melvin’s? $X_M / G$.  
>  
> $(b)$ Write an equation that expresses the condition for provision of the Pareto efficient quantity of the public good. $1/2 + X_M / G = 1$.  
>  
> $(c)$ Suppose that Melvin and Lucy each spend $\$2,000$ on private goods for themselves and they spend the remaining $\$4,000$ on public goods. Is this a Pareto efficient outcome? **Yes**.  
>  
> $(d)$ Give an example of another Pareto optimal outcome in which Melvin gets more than $\$2,000$ and Lucy gets less than $\$2,000$ worth of private goods. **One example: Melvin gets $\$2,500$; Lucy gets $\$500$ and $G = \$5,000$.**  
>  
> $(e)$ Give an example of another Pareto optimum in which Lucy gets more than $\$2,000$. **Lucy gets $\$5,000$; Melvin gets $\$1,000$ and $G = \$2,000$.**  
>  
> $(f)$ Describe the set of Pareto optimal allocations. **The allocations that satisfy the equations $X_M / G = 1/2$ and $X_L + X_M + G = \$8,000$.**  
>  
> $(g)$ The Pareto optima that treat Lucy better and Melvin worse will have (more of, less of, the same amount of) public good as the Pareto optimum that treats them equally. **Less of.**  

**关键公式提取**：  
- 效用函数：  
  - Lucy: $U_L = 2X_L + G$  
  - Melvin: $U_M = X_M G$  
- 预算约束： $X_L + X_M + G = 8000$  
- MRS 绝对值：  
  - Lucy: $\left| \text{MRS}_L \right| = \frac{1}{2}$  
  - Melvin: $\left| \text{MRS}_M \right| = \frac{X_M}{G}$  
- 帕累托最优条件： $\frac{1}{2} + \frac{X_M}{G} = 1$  
- 帕累托最优集约束： $\frac{X_M}{G} = \frac{1}{2} \quad \text{and} \quad X_L + X_M + G = 8000$  

---

#### 2. 基于上文知识点的解析  
**核心衔接点**：本题直接验证上文 **$\sum |\text{MRS}_i| = \text{MC}_G$ 普适性**，并强化 **“机制设计依赖透明计价”** 的结论（无需重复 Bob/Ray 或 Bonnie/Clyde 的细节，但延续其逻辑链条）。  

##### **(a) MRS 推导与理论延伸**  
- Lucy 的 MRS 恒定（$\frac{1}{2}$），源于其效用函数 $U_L = 2X_L + G$ 的**线性结构**（与上文 Bonnie/Clyde 中 $H^2$ 非线性形成对照，但 $\sum |\text{MRS}_i|$ 仍适用）。  
- Melvin 的 MRS（$\frac{X_M}{G}$）**依赖于消费水平**，反映上文 **“个体 MRS 会因偏好差异而动态变化”** 的普适性：  
  - 当 $X_M$ 增加或 $G$ 减少时，MRS 上升，体现**边际替代率递增**，与上文烟花模型 $\frac{1000}{40\sqrt{g}}$ 的递减逻辑互补（证明无论 MRS 单调性，$\sum |\text{MRS}_i|$ 加总规则不变）。  

##### **(b) 帕累托最优条件的机制本质**  
- **$\frac{1}{2} + \frac{X_M}{G} = 1$ 直接对应 $\sum |\text{MRS}_i| = \text{MC}_G$**：  
  - $\text{MC}_G = 1$（$G$ 以美元计价，边际成本隐含为 1），符合上文 **“透明计价使效率条件显性化”**（类比 Bonnie/Clyde 中 $H$ 的机会成本以小时利润度量）。  
  - $\sum |\text{MRS}_i|$ 的**线性加总性质**被进一步证明：Lucy 的常数 MRS 与 Melvin 的变量 MRS 仍严格满足 $\sum = \text{MC}_G$，呼应上文 **“人口规模 $N$ 线性放大需求”** 的抽象结论。  

##### **(c) 效率验证与成本分担扭曲的澄清**  
- 当 $X_L = X_M = 2000$，$G = 4000$ 时：  
  - $\frac{X_M}{G} = \frac{2000}{4000} = 0.5$，代入最优条件： $\frac{1}{2} + 0.5 = 1$，**满足帕累托效率**。  
  - **关键区分**：与上文 Bob/Ray 的私人物品成本共享扭曲不同（$\alpha < 1$ 导致 $G_{\text{实际}} > G^*$），此处公共物品无成本分担模糊，**直接实现 $\sum |\text{MRS}_i| = \text{MC}$**，故无搭便车问题。  

##### **(d)–(e) 与 (f) 帕累托最优集的动态性**  
- **最优分配集由两个方程约束**（$\frac{X_M}{G} = \frac{1}{2}$ 和预算约束）：  
  - **(d)** 例：$X_M = 2500$，$X_L = 500$，$G = 5000$ → $\frac{2500}{5000} = 0.5$，满足 $\frac{X_M}{G} = \frac{1}{2}$。  
  - **(e)** 例：$X_L = 5000$，$X_M = 1000$，$G = 2000$ → $\frac{1000}{2000} = 0.5$，同样满足最优条件。  
- **理论意义**：  
  - 证明帕累托最优解**不唯一**，但所有配置均强制满足 $\sum |\text{MRS}_i| = \text{MC}_G$，**验证上文“供给不足源于机制未能匹配 $\sum \text{MRS}$ 与 $\text{MC}$”**（如 Bonnie/Clyde 的 $H^*$ 压制）。  
  - 个体效用函数差异（Lucy 线性 vs. Melvin 拟线性）**不破坏效率条件**，反向确认上文 **“效用函数形式无关紧要”** 的普适性命题。  

##### **(g) 公共物品数量的分配敏感性**  
- **当 Lucy 被优先补偿时（$X_L$ 增大），$G$ 必然减少**（如 (e) 中 $X_L = 5000$ 时 $G = 2000 < 4000$）：  
  - 由 $\frac{X_M}{G} = \frac{1}{2}$ 和预算约束，$X_L \uparrow \implies X_M + G \downarrow$，且 $G$ 与 $X_M$ 成比例，故 $G$ 随 $X_L$ 上升而下降。  
- **与上文深度关联**：  
  - 呼应上文 **“帕累托改进阈值 $\$$75 源于支付能力差异”** 的逻辑——此处 $G$ 的变化率由 MRS 加总决定，揭示 **“分配公平性与供给数量负相关”** 是 $\sum |\text{MRS}_i| = \text{MC}_G$ 的内生结果。  
  - 强化 **“补贴闲暇导致 $\sum |\text{MRS}_i| < \text{MC}$ 的效率损失”** 结论：若试图通过转移支付改善某方境况（如提高 Lucy 的 $X_L$），但不调整 $G$，将破坏最优条件，引发供给不足。  

---

#### 3. 方法论总结  
- **实证递进价值**：本题与 Bob/Ray（私人物品扭曲）、Bonnie/Clyde（公共“坏”最优）形成**三重验证**：  
  - $\sum |\text{MRS}_i| = \text{MC}_G$ **普适于**  
    (i) 私人物品（成本分担模糊场景），  
    (ii) 公共物品（本题），  
    (iii) 公共“坏”（Bonnie/Clyde），  
    **且不依赖效用函数线性/非线性**。  
- **对机制设计的启示**：  
  - 公共物品配置效率取决于 **是否显性化 $\sum |\text{MRS}_i|$ 与 $\text{MC}_G$ 的匹配**（如本题通过透明计价实现），直接支持上文 **“机制透明性支撑帕累托最优”** 的核心论断。  
  - 任何分配方案必须内嵌此条件，否则如 (g) 所示，公平调剂可能**隐性导致 $G$ 低于最优水平**，重演上文滑冰场补贴的效率损失。

---
### Page/Slide 6



### 提取内容：当前图片文字与公式

#### 文字内容（完整提取）
```
428 PUBLIC GOODS (Ch. 35)

35.7 (0) This problem is set in a fanciful location, but it deals with a very practical issue that concerns residents of this earth. The question is, “In a Democracy, when can we expect that a majority of citizens will favor having the government supply pure private goods publicly?” This problem also deals with the efficiency issues raised by public provision of private goods. We leave it to you to see whether you can think of important examples of publicly supplied private goods in modern Western economies.

On the planet Jumpo there are two goods, aerobics lessons and bread. The citizens all have Cobb-Douglas utility functions of the form \( U_i(A_i, B_i) = A_i^{1/2} B_i^{1/2} \), where \( A_i \) and \( B_i \) are i’s consumptions of aerobics lessons and bread. Although tastes are all the same, there are two different income groups, the rich and the poor. Each rich creature on Jumpo has an income of 100 fondas and every poor creature has an income of 50 fondas (the currency unit on Jumpo). There are two million poor creatures and one million rich creatures on Jumpo. Bread is sold in the usual way, but aerobics lessons are provided by the state despite the fact that they are private goods. The state gives the same amount of aerobics lessons to every creature on Jumpo. The price of bread is 1 fonda per loaf. The cost to the state of aerobics lessons is 2 fondas per lesson. This cost of the state-provided lessons is paid for by taxes collected from the citizens of Jumpo. The government has no other expenses than providing aerobics lessons and collects no more or less taxes than the amount needed to pay for them. Jumpo is a democracy, and the amount of aerobics to be supplied will be determined by majority vote.

(a) Suppose that the cost of the aerobics lessons provided by the state is paid for by making every creature on Jumpo pay an equal amount of taxes. On planets, such as Jumpo, where every creature has exactly one head, such a tax is known as a “head tax.” If every citizen of Jumpo gets 20 lessons, how much will be total government expenditures on lessons? 120 million fondas. How much taxes will every citizen have to pay? 40 fondas. If 20 lessons are given, how much will a rich creature have left to spend on bread after it has paid its taxes? 60 fondas. How much will a poor creature have left to spend on bread after it has paid its taxes? 10 fondas.

(b) More generally, when everybody pays the same amount of taxes, if x lessons are provided by the government to each creature, the total cost to the government is 6 million times x and the taxes that one creature has to pay is 2 times x.
```

#### 公式内容
- 效用函数：  
  \( U_i(A_i, B_i) = A_i^{1/2} B_i^{1/2} \)
- 部分 (a) 数值：  
  Total government expenditures = \( 120 \times 10^6 \) fondas,  
  Tax per citizen = \( 40 \) fondas,  
  Rich remaining for bread = \( 60 \) fondas,  
  Poor remaining for bread = \( 10 \) fondas
- 部分 (b) 一般关系：  
  Total government cost = \( 6 \times 10^6 \times x \),  
  Tax per creature = \( 2 \times x \)

---

### 结合上文知识点的解析  
本图无图表，但文本内容与上文知识点形成直接验证，揭示 **公共决策机制对私人物品集体供给的效率影响**。以下基于上文核心结论进行递进分析：

#### 1. **机制设计缺陷导致效率损失的实证验证**  
上文方法论指出，\(\sum |\text{MRS}_i| = \text{MC}_G\) 普适于私人物品场景（如 Bob/Ray 案例中的成本分担扭曲）。本题中：  
- Aerobics lessons 本质是私人物品（具竞争性），但政府强制提供相同数量 \(x\)，且通过 **“head tax”** 均摊成本（即 \( \text{tax per citizen} = 2x \)）。  
- 贫富收入差异（rich: 100 fondas, poor: 50 fondas）导致：  
  - 当 \(x = 20\) 时，poor 剩余 bread 购买力仅 10 fondas（原收入 50），而 rich 有 60 fondas。  
  - 此分配 **内生抑制需求表达**：poor 的收入约束使其无法通过税收机制反映真实 MRS（因预算约束骤减），而 rich 的 MRS 未被充分加权。  
- 与上文 (g) 部分深度呼应：  
  > “分配公平性与供给数量负相关”  
  本题中，若多数投票倾向于增加 \(x\)（如 rich 更偏好），poor 的面包消费将被挤压（剩余收入不足），**隐性降低整体 \(\sum |\text{MRS}_i|\)**，从而破坏 \(\sum |\text{MRS}_i| = \text{MC}_G\) 的效率条件。结果必然是 **供给偏离最优水平**（类似上文滑冰场补贴案例的效率损失）。

#### 2. **效用函数形式的普适性与支付能力差异的放大效应**  
上文强调 “效用函数形式无关紧要”，本题以 Cobb-Douglas 形式复现关键逻辑：  
- 与上文 Lucy (线性) 和 Melvin (拟线性) 案例不同，此处全体消费者效用函数同构（\(U_i = A_i^{1/2} B_i^{1/2}\)），但 **收入差异扭曲了实际需求**：  
  - MRS 计算：\(\text{MRS}_i = \frac{\partial U / \partial A_i}{\partial U / \partial B_i} = \frac{B_i}{A_i}\)，与收入正相关（因 \(B_i\) 取决于剩余收入）。  
  - Head tax 使 poor 的 \(B_i\) 被强制压缩（如 \(x=20\) 时仅剩 10 fondas），导致其 MRS 被人为抬高（但投票中未被加权），而 rich 的 MRS 未充分体现。  
- 直接验证上文 **“支付能力差异设定帕累托改进阈值”**：  
  > 如上文 Bonnie/Clyde 案例中 $75 阈值源于收入差，  
  本题 poor 剩余收入仅 10 fondas（富者 60 fondas），差距扩大至 6 倍，**加剧多数投票对 low-MRS 个体的忽视**。若无机制调整（如收入相关补贴），必重演上文 “\(\sum \text{MRS}_i < \text{MC}\)” 的供给不足。

#### 3. **对民主决策中公共供给边界的启示**  
- 上文核心论断 “机制透明性支撑帕累托最优” 在此场景被证伪：  
  Head tax 机制 **掩盖了 \(\sum \text{MRS}_i\) 与 \(\text{MC}_G\) 的匹配**：  
  - 政府成本 \( \text{MC}_G = 6 \times 10^6 \) fondas/lesson（固定），  
  - 但纳税人投票仅基于自身净效用，无视其他人 MRS（因税收均摊导致 **成本分担模糊**）。  
- 例：多数投票可能支持 \(x>0\)（如 poor 占优时倾向于低成本），但均无法实现 \(\sum |\text{MRS}_i| = \text{MC}_G\)。这直接呼应上文 **“公共物品配置效率取决于匹配显性化”**，且强化了本题问题的实践意义——  
  > “In a Democracy, when can we expect a majority to favor public supply of private goods?”  
  答案隐含于上文：**仅当机制内嵌 \(\sum \text{MRS}_i\) 加总规则时**（如 Lindahl 税），否则民主决策必偏离效率边界。

综上，本题以 Cobb-Douglas 模型为载体，三重验证上文结论：  
1. 私人物品公共供给 **必引致成本分担扭曲**（类比 Bob/Ray）；  
2. 收入差异 **系统性放大分配与效率的负相关**（延伸上文 (g)）；  
3. 民主机制若未显性化 \(\sum \text{MRS}_i\)，**帕累托最优集无法达成**（呼应方法论总结）。  
此分析为上文 “三重验证” 提供了公理化实证支撑。

---
### Page/Slide 7



# 解析：公共提供私人物品的投票机制与效率损失

## 文字与公式提取

### 文字内容
- **(c)** 有氧课程将被公共提供，每人获得相同数量且无法从其他来源获取更多课程。消费者面临选择问题：最大化Cobb-Douglas效用函数，预算约束为 $2A + B = I$（$I$ 为收入）。若提供 $A$ 节课程，税收为 $2A$ fondas；纳税后剩余 $I-2A$ fondas 用于购买面包 $B$。
- **(d)** 若通过"人头税"(head tax)支付，政府向每人提供等量课程：富人偏好数量为 25，穷人偏好数量为 12.5（需基于合适预算求解Cobb-Douglas需求）。
- **(e)** 若由多数投票决定：提供 12.5 节课程。富人获得 75 单位面包，穷人获得 25 单位面包。
- **(f)** 若课程私有化（无人提供公共课程且不征税）：价格为面包 1 fonda/单位、课程 2 fondas/单位。富人消费 25 节课程和 50 单位面包；穷人消费 12.5 节课程和 25 单位面包。
- **(g)** 若维持公共提供但改用比例所得税：富人税单 $3A$ fondas，穷人税单 $1.5A$ fondas。总税收 = $2,000,000 \times 1.5A + 1,000,000 \times 3A = 6,000,000A$。

### 公式
- 消费者预算约束：$2A + B = I$
- 税收机制：$\text{tax} = 2A$（人头税）
- 纳税后剩余：$I - 2A$（用于购买面包 $B$）
- 比例税总收入：$2,000,000 \times 1.5A + 1,000,000 \times 3A = 6,000,000A$

---

## 知识点关联解析

### 1. **预算约束的公共提供扭曲**
- 问题(c)的 $2A + B = I$ 直接验证上文"**head tax 均摊成本**"机制：  
  每人强制承担 $2A$ 的税收（即 $\text{tax per citizen} = 2x$），导致预算约束从私有化的 $P_A A + P_B B = I$ 被扭曲为 $2A + B = I$。  
  - **关键机制**：当 $A$ 增加，$B$ 的购买力被刚性压缩（如 $x=12.5$ 时，穷人 $B_i = 50 - 2 \times 12.5 = 25$），与上文 $x=20$ 时"poor 剩余 bread 仅 10 fondas"逻辑一致。

### 2. **收入差异对需求表达的系统性扭曲**
- 问题(d)中富人偏好数量(25)是穷人(12.5)的2倍，精准体现上文"**支付能力差异设定帕累托改进阈值**"：  
  - 富人收入 100 fondas → 可负担 $A^* = 25$（因 $2 \times 25 = 50$，占收入 50%）  
  - 穷人收入 50 fondas → 仅负担 $A^* = 12.5$（$2 \times 12.5 = 25$，占收入 50%）  
  - **与上文呼应**：Cobb-Douglas 效用函数 $U_i = A_i^{1/2}B_i^{1/2}$ 使需求比例固定（收入平分原则），但 **收入差异被 head tax 放大**：当 $A$ 从 0 增至 25，穷人总面包消费从 50 骤降至 0，而富人降至 50，差距从 2 倍扩大为无穷大。

### 3. **多数投票机制的效率损失**
- 问题(e)中多数投票结果(12.5)与穷人偏好一致，验证上文"**分配公平性与供给数量负相关**"：  
  - 穷人数目(2,000,000) > 富人(1,000,000) → 少数富人的高 MRS 被完全忽视  
  - 此时 $\sum |\text{MRS}_i| < \text{MC}_G$：  
    - 穷人 MRS = $B_i/A_i = 25/12.5 = 2$  
    - 富人 MRS = $75/12.5 = 6$  
    - $\sum \text{MRS}_i = 2,000,000 \times 2 + 1,000,000 \times 6 = 10,000,000$  
    - 而 $\text{MC}_G = 6 \times 10^6$（见上文）  
  - **核心结论**：当机制未显性化 $\sum \text{MRS}_i$ 时，投票结果必然 $\sum \text{MRS}_i > \text{MC}_G$（此处 $10^7 > 6 \times 10^6$），导致 **供给过度**（与上文 Bob/Ray 案例扭曲方向一致）。

### 4. **私有化 vs. 比例税机制的效率对比**
- 问题(f)私有化结果（富人 25 节/50 面包、穷人 12.5 节/25 面包）形成**有效率配置**：  
  - 每人自选最优 $A$ 使 $\text{MRS}_i = P_A/P_B = 2$  
  - 印证上文"私人物品应私有化"原则——**无交叉补贴时，个体预算约束反映真实 MRS**。
- 问题(g)比例税设计直指上文**Lindahl 税核心**：  
  - 富人税 $3A$ ≈ 其 MRS（$B_i/A_i = 6$ 需 3 倍权重），穷人税 $1.5A$ ≈ 其 MRS（MRS=2 需 1.5 倍权重）  
  - 总税收 $6,000,000A$ 恰等于政府成本（$6 \times 10^6$ fondas/lesson），**首次显性化 $\sum \text{MRS}_i$ 与 $\text{MC}_G$ 的匹配**——这是唯一能实现帕累托最优的机制。

### 5. **对公共物品供给边界的实践启示**
- 本题从 **"私人物品公共提供"** 视角，强化上文核心论断：  
  > "民主决策中，仅当机制内嵌 $\sum \text{MRS}_i$ 加总规则时，才能达成帕累托最优"  
  - Head tax 场景(e)：供给 12.5 节 → 穷人面包刚性约束使 $\sum \text{MRS}_i$ 被高估，触发过度供给  
  - 比例税场景(g)：税收权重与 MRS 正相关 → 恢复 $\sum \text{MRS}_i = \text{MC}_G$  
- **结论延伸**：问题(e)与(f)对比证明——  
  公共提供私人物品时，**人头税必然扭曲需求表达**（类比上文滑冰场补贴案例），而**收入相关税制是效率解唯一的制度选择**。

---
### Page/Slide 8



### 3.9 比例税机制、效用比较与帕累托最优验证  
#### 1. 图片文字与公式提取  
- **情境设定**：  
  Total population: $3,000,000$ | Cost per lesson: $2$ fondas | Total cost: $6,000,000A$  
- **问题(h)**：  
  - Rich budget constraint: $\boxed{3A + B = 100}$  
  - Poor budget constraint: $\boxed{1.5A + B = 50}$  
  - Rich preferred lessons: $\boxed{\dfrac{50}{3}}$  
  - Poor preferred lessons: $\boxed{\dfrac{50}{3}}$  
  - Majority rule quantity: $\boxed{\dfrac{50}{3}}$  
  - Rich bread consumption: $\boxed{50}$  
  - Poor bread consumption: $\boxed{25}$  
- **问题(i)**（效用函数 $U_i = A_i^{1/2} B_i^{1/2}$，表达为平方根形式）：  
  | Scenario          | Rich Utility       | Poor Utility       |
  |-------------------|-------------------|-------------------|
  | Head tax         | $\sqrt{937.5}$   | $\sqrt{312.5}$   |
  | Privatization    | $\sqrt{1,250}$   | $\sqrt{312.5}$   |
  | Proportional tax | $\sqrt{833.3}$   | $\sqrt{416.67}$  |  
- **问题(j)**：  
  - Privatization vs head tax: $\boxed{\text{Yes}}$  
  - Proportional tax vs head tax: $\boxed{\text{No}}$  
  - Privatization vs proportional tax: $\boxed{\text{No}}$  
  - Explanation: $\boxed{\text{Rich prefer privatization, poor prefer proportional income tax}}$  

#### 2. 关键机制解析（结合上文知识点）  
##### (h) 比例税机制的效率实现  
- **预算约束的构造逻辑**：  
  效率税设计（Lindahl 税）将税收权重与个体 **MRS 直接挂钩**：  
  - 富人税收权重 $3$ ≈ 其 $B/A$（MRS，见上文知识点4），推导出预算约束 $3A + B = 100$。  
  - 穷人税收权重 $1.5$ ≈ 其 $B/A$（MRS=2），约束 $1.5A + B = 50$。  
  - **核心机制**：税收权重内嵌 $\sum \text{MRS}_i$ 的显性化，使个体决策时 $\text{MRS}_i = \text{tax rate}_i$，满足 $\sum \text{MRS}_i = \text{MC}_G = 6 \times 10^6$（上文知识点4）。  
- **均衡结果**：  
  - 双方偏好一致（均选 $\frac{50}{3}$），故多数投票结果无冲突（$\frac{50}{3}$）。  
  - 面包分配反映效率：  
    - 富人消费 $B = 50$（因 $3 \times \frac{50}{3} + B = 100 \Rightarrow B = 50$），  
    - 穷人消费 $B = 25$（因 $1.5 \times \frac{50}{3} + B = 50 \Rightarrow B = 25$）。  
  - **与上文呼应**：此为唯一实现帕累托最优的机制（上文知识点4），因 $\sum \text{MRS}_i$ 与 $\text{MC}_G$ 精准匹配。  

##### (i) 效用比较的深层含义  
- **效用值计算依据**（基于 $U_i = \sqrt{A_i B_i}$）：  
  - **Head tax**：延续问题(e)扭曲均衡（$A = 12.5$），富人刚性消费 $B = 75$（$U = \sqrt{12.5 \times 75} = \sqrt{937.5}$），穷人 $B = 25$（$U = \sqrt{312.5}$）。  
  - **Privatization**：对应问题(f)效率配置，富人自选 $A = 25, B = 50$（$U = \sqrt{1250}$），穷人 $A = 12.5, B = 25$（$U = \sqrt{312.5}$）。  
  - **Proportional tax**：Lindahl 均衡下 $A = \frac{50}{3}$，富人 $B = 50$（$U = \sqrt{\frac{50}{3} \times 50} = \sqrt{833.3}$），穷人 $B = 25$（$U = \sqrt{\frac{50}{3} \times 25} = \sqrt{416.67}$）。  
- **效率视角**：  
  - Privatization 中富人效用 $\sqrt{1250} > \sqrt{937.5}$（head tax），证实 **人头税扭曲需求**（上文知识点3），私有化还原真实 MRS。  
  - Proportional tax 中穷人效用 $\sqrt{416.67} > \sqrt{312.5}$（head tax），认证 **收入相关税制纠正分配失衡**（上文知识点5）。  

##### (j) 帕累托比较的制度启示  
- **Privatization vs head tax = Yes**：  
  - 富人效用提升（$\sqrt{1250} > \sqrt{937.5}$），穷人效用不变（$\sqrt{312.5} = \sqrt{312.5}$），直接验证 **私人物品私有化零效率损失**（上文知识点4）。  
- **Proportional tax vs head tax = No**：  
  - 因富人效用下降（$\sqrt{833.3} < \sqrt{937.5}$），虽穷人改善但违背 "无人受损" 原则。  
  - **关键矛盾**：head tax 下富人被迫消费低 $A$ 但高 $B$（扭曲剩余），而比例税需富人承担高权重税收（MRS=6），导致 $B$ 显著减少（$50 \to 75$），效用反降。  
- **Privatization vs proportional tax = No**：  
  - 富人偏好私有化（$\sqrt{1250} > \sqrt{833.3}$），穷人偏好比例税（$\sqrt416.67 > \sqrt{312.5}$），双方 **偏好分歧源于税制本质**：  
    - 私有化无交叉补贴，个体完全控制 MRS。  
    - 比例税隐含收入再分配，虽效率却牺牲富人福利（上文知识点5："收入相关税制是效率解，但未必帕累托占优"）。  
  - 此对比强化结论：**民主决策需机制内嵌 $\sum \text{MRS}_i$**（上文知识点5），但效率实现可能引致分配冲突。  

#### 3. 延伸结论  
本部分实证了上文核心命题：  
- 比例税（h）成功显性化 $\sum \text{MRS}_i$，实现 **技术效率**，但帕累托最优的达成需权衡 **效率与公平**（i/j 部分）。  
- 与 head tax 对比揭示：**人头税扭曲需求刚性**，而 **比例税虽效率却非普适最优**（富人反对），佐证上文"公共提供私人物品必须匹配收入相关税制"（上文知识点5）。  
- 结合问题(f)私有化结果，重申 **私人品属性决定最优制度选择**：当物品具私人性，私有化无效率损失；仅当公共提供时需精密税制设计。
