# PDF_Chapter_27

### Page/Slide 1



### 文字内容提取  
**Chapter 27**  
**Oligopoly**  

**Introduction.** In this chapter you will solve problems for firm and industry outcomes when the firms engage in Cournot competition, Stackelberg competition, and other sorts of oligopoly behavior. In Cournot competition, each firm chooses its own output to maximize its profits given the output that it expects the other firm to produce. The industry price depends on the industry output, say, $ q_A + q_B $, where A and B are the firms. To maximize profits, firm A sets its marginal revenue (which depends on the output of firm A and the expected output of firm B since the expected industry price depends on the sum of these outputs) equal to its marginal cost. Solving this equation for firm A’s output as a function of firm B’s expected output gives you one reaction function; analogous steps give you firm B’s reaction function. Solve these two equations simultaneously to get the Cournot equilibrium outputs of the two firms.  

**Example:** In Heifer’s Breath, Wisconsin, there are two bakers, Anderson and Carlson. Anderson’s bread tastes just like Carlson’s—nobody can tell the difference. Anderson has constant marginal costs of \$1 per loaf of bread. Carlson has constant marginal costs of \$2 per loaf. Fixed costs are zero for both of them. The inverse demand function for bread in Heifer’s Breath is $ p(q) = 6 - .01q $, where $ q $ is the total number of loaves sold per day.  

Let us find Anderson’s Cournot reaction function. If Carlson bakes $ q_C $ loaves, then if Anderson bakes $ q_A $ loaves, total output will be $ q_A + q_C $ and price will be $ 6 - .01(q_A + q_C) $. For Anderson, the total cost of producing $ q_A $ units of bread is just $ q_A $, so his profits are  

$$ pq_A - q_A = (6 - .01q_A - .01q_C)q_A - q_A $$  
$$ = 6q_A - .01q_A^2 - .01q_C q_A - q_A. $$  

Therefore if Carlson is going to bake $ q_C $ units, then Anderson will choose $ q_A $ to maximize $ 6q_A - .01q_A^2 - .01q_C q_A - q_A $. This expression is maximized when $ 6 - .02q_A - .01q_C = 1 $. (You can find this out either by setting A’s marginal revenue equal to his marginal cost or directly by setting the derivative of profits with respect to $ q_A $ equal to zero.) Anderson’s reaction function, $ R_A(q_C) $ tells us Anderson’s best output if he knows that Carlson is going to bake $ q_C $. We solve from the previous equation to find $ R_A(q_C) = (5 - .01q_C)/.02 = 250 - .5q_C $.  

We can find Carlson’s reaction function in the same way. If Carlson knows that Anderson is going to produce $ q_A $ units, then Carlson’s profits will be $ p(q_A + q_C) - 2q_C = (6 - .01q_A - .01q_C)q_C - 2q_C = 6q_C - .01q_A q_C - .01q_C^2 - 2q_C $. Carlson’s profits will be maximized if he chooses $ q_C $ to satisfy the equation $ 6 - .01q_A - .02q_C = 2 $. Therefore Carlson’s reaction function is $ R_C(q_A) = (4 - .01q_A)/.02 = 200 - .5q_A $.  

---

### 公式提取  
1. **Anderson的利润函数**  
   $$
   \pi_A = (6 - 0.01q_A - 0.01q_C)q_A - q_A = 5q_A - 0.01q_A^2 - 0.01q_C q_A
   $$  
2. **Anderson的反应函数条件**  
   $$
   6 - 0.02q_A - 0.01q_C = 1 \implies R_A(q_C) = 250 - 0.5q_C
   $$  
3. **Carlson的利润函数**  
   $$
   \pi_C = (6 - 0.01q_A - 0.01q_C)q_C - 2q_C = 4q_C - 0.01q_A q_C - 0.01q_C^2
   $$  
4. **Carlson的反应函数条件**  
   $$
   6 - 0.01q_A - 0.02q_C = 2 \implies R_C(q_A) = 200 - 0.5q_A
   $$  

---

### 经济学解析  
- **成本不对称性对反应函数的影响**：  
  Anderson的边际成本（\$1）低于Carlson（\$2），导致其反应函数截距更高（250 vs 200）。例如，当$ q_C = 0 $时，Anderson的最优产量为250单位，而Carlson仅能维持200单位，体现成本优势对供给能力的直接影响。  

- **策略替代效应的量化体现**：  
  两反应函数斜率均为$-0.5$，表明一厂商增产1单位将导致另一厂商减产0.5单位。这种对称斜率源于需求函数的线性结构，但截距差异揭示了成本差异如何打破均衡对称性。  

- **利润最大化机制**：  
  通过将边际收益（MR）等于边际成本（MC）推导反应函数。例如：  
  - Anderson的MR = $ 6 - 0.02q_A - 0.01q_C $，令其等于MC=1，解得最优产量条件。  
  - 此步骤验证了上文所述“**边际收益-边际成本均衡逻辑**”在异质成本场景下的具体应用。  

- **模型延续性意义**：  
  本例为联立反应函数求解Cournot均衡（如$ q_A^* = 200, q_C^* = 100 $）提供直接依据，深化了上文对“**反应函数联立确定均衡产出**”的理论阐述，凸显了成本结构对市场分配的核心作用。

---
### Page/Slide 2



### 公式提取  
1. **Cournot均衡条件**  
   $$
   \tilde{q}_A = R_A(\tilde{q}_C), \quad \tilde{q}_C = R_C(\tilde{q}_A)
   $$  
   均衡解：  
   $$
   \tilde{q}_A = 200, \quad \tilde{q}_C = 100
   $$  
2. **Cournot均衡价格与利润**  
   $$
   p = 6 - 0.01(200 + 100) = 3
   $$  
   Anderson利润：$\$2 \times 200$，Carlson利润：$\$1 \times 100$  
3. **Stackelberg模型基础**  
   行业总价：$q_L + R_F(q_L)$  
4. **Stackelberg例子（Carlson为领导者）**  
   - Anderson反应函数：$R_A(q_C) = 250 - 0.5q_C$  
   - 总产出：$q_C + R_A(q_C) = 250 + 0.5q_C$  
   - 价格函数：$p = 6 - 0.01(250 + 0.5q_C) = 3.5 - 0.005q_C$  
   - Carlson利润函数：$\pi_C = 1.5q_C - 0.005q_C^2$  
   - 均衡产出：$q_C = 150$，$q_A = 250 - 0.5 \times 150 = 175$  
   - Stackelberg价格：$p = 6 - 0.01(175 + 150) = 2.75$  
   - 利润分配：Carlson $\$0.75 \times 150$，Anderson $\$1.75 \times 175$  
5. **附录问题需求函数**  
   $$
   q = 3,200 - 1,600p, \quad q = q_C + q_S
   $$  

---

### 经济学解析  
基于上文推导的异质成本反应函数（$R_A(q_C) = 250 - 0.5q_C$, $R_C(q_A) = 200 - 0.5q_A$），当前内容通过**均衡求解**和**Stackelberg扩展**深化了寡头竞争的动态机制：  

1. **Cournot均衡的实证化验证**：  
   - 上文已建立反应函数，当前通过联立方程求解具体均衡值（$\tilde{q}_A = 200$, $\tilde{q}_C = 100$），验证了**成本不对称性对产出分配的量化影响**：Anderson以更低边际成本（\$1 vs \$2）获得更高市场份额（200 vs 100单位），但沉浸于静态均衡中，双方均无法单方面改变策略（纳什均衡特性）。  
   - 均衡价格 \$3 的推导直接应用需求函数 $p = 6 - 0.01(q_A + q_C)$，凸显**总产出决定价格**的市场机制。利润差异（Anderson \$400 vs Carlson \$100）源于成本与产量的耦合，呼应上文“**成本结构是利润分配的核心变量**”。

2. **Stackelberg竞争的动态优势**：  
   - 模型突破Cournot的同步假设，引入**领导-跟随序列**：领导者（Carlson）将跟随者（Anderson）的反应函数 $R_A(q_C)$ 内生化，优化自身决策。关键公式 $q_C + R_A(q_C)$ 将行业总价压缩为单变量 $q_C$，使领导者能直接构建利润最大化条件（$\pi_C = 1.5q_C - 0.005q_C^2$）。  
   - 领导者优势体现为**战略先动权**：Carlson 产量增至 150（vs Cournot 100），迫使 Anderson 增产至 175（vs 200），总产出 325 > 300。但价格 (\$2.75) 低于 Cournot (\$3)，反映**产量扩张对价格的压制效应**。  
   - 利润再分配揭示结构性洞见：Carlson 利润提升至 \$112.5 （vs \$100），证明**高成本厂商可通过先动优势弥补成本劣势**；Anderson 利润降至 \$306.25，说明跟随者因被动调整而受损。这验证了序列博弈中“**先动者攫取超额剩余**”的普遍规律，与上文成本不对称逻辑形成互补。

3. **模型延续性的实践意义**：  
   - Boxed 例题将理论映射至现实（如烘焙时间差异塑造领导地位），强调**技术或时间优势可内生化为博弈顺序**。  
   - 附录引入新需求函数 $q = 3,200 - 1,600p$，为后续分析**规模报酬或市场容量**提供接口，延续上文“**需求结构决定均衡特性**”的核心论点。  
   - 综合而言，当前内容从静态均衡（Cournot）走向动态均衡（Stackelberg），阐明**市场力量不仅取决于成本，还依赖策略时序**，为理解现实寡头行为（如产能预披露、技术领先者定价）奠定理论台阶。

---
### Page/Slide 3



### 1. 提取当前图片中的所有文字、公式

#### 文字内容：
- and $q_S$ is the number that Simon sells. The cost of producing pumpkins for either farmer is $\$0.50$ per pumpkin no matter how many pumpkins he produces.
- (a) The inverse demand function for pumpkins at the Farmers’ Market is $p = a - b(q_C + q_S)$, where $a = 2$ and $b = 1/1,600$. The marginal cost of producing a pumpkin for either farmer is $\$0.50$.
- (b) Every spring, each of the farmers decides how many pumpkins to grow. They both know the local demand function and they each know how many pumpkins were sold by the other farmer last year. In fact, each farmer assumes that the other farmer will sell the same number this year as he sold last year. So, for example, if Simon sold 400 pumpkins last year, Carl believes that Simon will sell 400 pumpkins again this year. If Simon sold 400 pumpkins last year, what does Carl think the price of pumpkins will be if Carl sells 1,200 pumpkins this year? If Simon sold $q_S^{t-1}$ pumpkins in year $t-1$, then in the spring of year $t$, Carl thinks that if he, Carl, sells $q_C^t$ pumpkins this year, the price of pumpkins this year will be $2 - (q_S^{t-1} + q_C^t)/1,600$.
- (c) If Simon sold 400 pumpkins last year, Carl believes that if he sells $q_C^t$ pumpkins this year then the inverse demand function that he faces is $p = 2 - 400/1,600 - q_C^t/1,600 = 1.75 - q_C^t/1,600$. Therefore if Simon sold 400 pumpkins last year, Carl’s marginal revenue this year will be $1.75 - q_C^t/800$. More generally, if Simon sold $q_S^{t-1}$ pumpkins last year, then Carl believes that if he, himself, sells $q_C^t$ pumpkins this year, his marginal revenue this year will be $2 - q_S^{t-1}/1,600 - q_C^t/800$.
- (d) Carl believes that Simon will never change the amount of pumpkins that he produces from the amount $q_S^{t-1}$ that he sold last year. Therefore Carl plants enough pumpkins this year so that he can sell the amount that maximizes his profits this year. To maximize this profit, he chooses the output this year that sets his marginal revenue this year equal to his marginal cost. This means that to find Carl’s output this year when Simon’s output last year was $q_S^{t-1}$, Carl solves the following equation: $2 - q_S^{t-1}/1,600 - q_C^t/800 = 0.5$.
- (e) Carl’s Cournot reaction function, $R_C^t(q_S^{t-1})$, is a function that tells us what Carl’s profit-maximizing output this year would be as a function of Simon’s output last year. Use the equation you wrote in the last answer to find Carl’s reaction function, $R_C^t(q_S^{t-1}) = 1,200 - q_S^{t-1}/2$. (Hint: This is a linear expression of the form $a - b q_S^{t-1}$. You have to find the constants $a$ and $b$.)

#### 公式内容：
- 需求函数： $p = a - b(q_C + q_S)$  
  参数： $a = 2$, $b = \frac{1}{1,600}$  
  边际成本： $\text{MC} = 0.5$
- 价格预测： $p = 2 - \frac{q_S^{t-1} + q_C^t}{1,600}$
- 特定情形（Simon去年销量 400）：  
  需求： $p = 1.75 - \frac{q_C^t}{1,600}$  
  边际收益： $\text{MR} = 1.75 - \frac{q_C^t}{800}$
- 一般边际收益： $\text{MR} = 2 - \frac{q_S^{t-1}}{1,600} - \frac{q_C^t}{800}$
- 利润最大化条件： $2 - \frac{q_S^{t-1}}{1,600} - \frac{q_C^t}{800} = 0.5$
- 反应函数： $R_C^t(q_S^{t-1}) = 1,200 - \frac{q_S^{t-1}}{2}$

---

### 2. 经济学解析
当前内容直接应用**上文附录需求函数**（$q = 3,200 - 1,600p$），推导同质成本下的Cournot反应函数，与上文知识点形成关键衔接：  

#### 需求函数与模型设定的连续性
- 上文附录明确给出需求结构 $q = 3,200 - 1,600p$，当前内容将其转化为逆需求函数 $p = 2 - \frac{q}{1,600}$（其中 $q = q_C + q_S$），**验证了需求参数如何内生化反应函数**。此处 $a=2$ 和 $b=1/1,600$ 源于上文设定，避免了对需求机制的重复解释。  
- 与上文异质成本案例（Anderson MC=$1$, Carlson MC=$2$）形成对照：**本案例中边际成本同质（$\text{MC}=0.5$）**，凸显成本对称性对策略互动的影响——反应函数呈对称形式（后续可推导 $R_S^t(q_C^{t-1}) = 1,200 - \frac{q_C^{t-1}}{2}$），而上文异质成本导致反应函数截距差异（$250$ vs $200$），体现**成本差异是扭曲产量分配的结构性根源**。

#### 反应函数推导的机制深化
- **策略时序假设的显性化**：厂商基于历史产量预测对手行为（如 $q_S^{t-1}$ 固定），继承上文"**先动优势依赖假设准确性**"逻辑。但此处无Stackelberg序贯结构，而是强化Cournot均衡的静态本质——双方同时调整，但需通过时间维度 $t$ 模拟迭代收敛至均衡。  
- **反应函数系数的经济含义**：  
  - 从利润最大化条件 $2 - \frac{q_S^{t-1}}{1,600} - \frac{q_C^t}{800} = 0.5$ 解出 $R_C^t(q_S^{t-1}) = 1,200 - \frac{q_S^{t-1}}{2}$。  
  - 截距 $1,200$ 由需求参数和成本共同决定（$ \frac{a - \text{MC}}{2b} = \frac{2 - 0.5}{2 \times \frac{1}{1,600}} = 1,200 $），**延续上文“需求规模参数主导初始产能”** 的论点。  
  - 斜率 $-0.5$ 源于 $b$ 值（$\text{斜率} = -\frac{1}{2}$），印证上文反应函数的通用形式 $R_i(q_j) = \frac{a - \text{MC}_i}{2b} - \frac{1}{2} q_j$，**显示市场集中度（$b$ 值）对策略敏感性的量化作用**。

#### 对上文均衡分析的延伸
- 若求解均衡，联立反应函数得 $q_C^* = q_S^* = 800$（因同质成本），总产出 $q^* = 1,600$，价格 $p^* = 1.0$。此结果呼应上文Cournot均衡的核心规律：**总产出随厂商数增加而逼近完全竞争水平**（上文 $q_A + q_C = 300$，此处 $q_C + q_S = 1,600$），但关键差异在于**同质成本消除利润分化**（双方利润相等），反至上文成本不对称导致利润分配高度倾斜（Anderson $\$400$ vs Carlson $\$100$）。  
- 本例为后续Stackelberg分析埋下伏笔：若引入领导-跟随序列（如习题中一方提前决策），厂商将利用反应函数内生化对手行为（如上文Carlson的 $q_C + R_A(q_C)$），**动态优势与成本劣势的博弈关系将重新激活上文"先动者攫取超额剩余"的结论**。  

综上，本内容以**同质成本案例**衔接上文，将抽象需求函数落地为可操作的反应函数推导，强化"**策略互动本质是需求参数与成本结构的耦合均衡**"这一主线，为寡头竞争动态分析提供标准化框架。

---
### Page/Slide 4



# Cournot 模型动态收敛与均衡验证分析

## 图片文字与公式提取

### 文字内容
- (f) 假设 Simon 的决策方式与 Carl 相同，问题完全对称。因此无需计算即可推断 Simon 的反应函数为 $R_S^t(q_C^{t-1}) = 1,200 - q_C^{t-1}/2$。
- (g) 假设第 1 年 Carl 生产 200 个南瓜、Simon 生产 1,000 个。第 2 年 Carl 产量：700；Simon 产量：1,100。第 3 年 Carl 产量：650；Simon 产量：850。Carl 产量收敛至 800；Simon 产量收敛至 800。
- (h) 平衡条件方程组：若 Carl 生产 $q_C$、Simon 生产 $q_S$，则下期均希望维持产量，方程为 $q_S = 1,200 - q_C/2$ 和 $q_C = 1,200 - q_S/2$。
- (i) 均衡解：每个厂商生产 800 单位，总产量 1,600，市场价格 $1，每个厂商利润 $400。
- 27.2 (0) 模型新增细节：Carl 比 Simon 早一周种植，Simon 可观察 Carl 实际种植量，因此不再假设 Carl 沿用去年产量。

### 公式列表
1. Simon 反应函数：$R_S^t(q_C^{t-1}) = 1,200 - q_C^{t-1}/2$
2. Cournot 均衡条件方程组：
   $$
   \begin{cases}
   q_S = 1,200 - \dfrac{q_C}{2} \\
   q_C = 1,200 - \dfrac{q_S}{2}
   \end{cases}
   $$

## 经济学解析

### 1. 对称反应函数与均衡收敛机制
- **同质成本的直接应用**：图片(f)中 Simon 反应函数 $R_S^t(q_C^{t-1}) = 1,200 - q_C^{t-1}/2$ 严格呼应上文反应函数通式 $R_i(q_j) = \frac{a - \text{MC}_i}{2b} - \frac{1}{2}q_j$。当 $a=2$、$\text{MC}=0.5$、$b=1/1,600$ 时，截距 $\frac{2-0.5}{2 \times (1/1,600)} = 1,200$，验证了上文"需求规模参数主导初始产能"的结论。
- **动态调整过程**：图片(g)的迭代序列（年1: [200,1000] → 年2: [700,1100] → 年3: [650,850]）揭示了Cournot模型的收敛路径：
  - 通过反应函数递推 $q_C^t = 1,200 - q_S^{t-1}/2$ 和 $q_S^t = 1,200 - q_C^{t-1}/2$
  - 序列逼近均衡点 (800,800)，体现寡头厂商在有限理性下通过历史产量调整趋向均衡
  - 此过程强化上文"时间维度 $t$ 模拟迭代收敛至均衡"的关键机制

### 2. 均衡结果与上文模型验证
- **均衡解的实现**：图片(i)求解方程组得 $q_C^* = q_S^* = 800$，与上文推导完全一致。印证同质成本下：
  - 总产量 $q^* = 1,600$ 使市场价格 $p^* = 2 - 1,600/1,600 = 1$
  - 单厂商利润 $ \pi = (p^* - \text{MC})q^* = (1 - 0.5) \times 800 = 400 $
- **与上文异质成本案例的对比延伸**：
  | 模型类型 | 厂商产能 | 价格 | 单厂商利润 | 关键差异 |
  |---|---|---|---|---|
  | 本例同质成本 | 800 | $1 | $400 | 利润平等分配 |
  | 上文异质成本 | Anderson 250 / Carlson 200 | $1.5 | $400 / $100 | 成本差异导致利润分化 |
  - 再次验证上文结论：**成本对称性使策略互动简化为对称均衡，消除利润分配扭曲**

### 3. Stackelberg模型的逻辑铺垫
- **先动优势的实证化**：27.2(0)引入的时序细节（Carl 早于 Simon 种植）将上文抽象的"先动优势依赖假设准确性"转化为明确博弈结构：
  - Carl 作为价格先行者，其决策不再是历史产量 $q_S^{t-1}$，而是直接影响 Simon 的当期反应
  - Simon 的反应函数内生化为 $q_S = R_S(q_C^t)$（$\text{而非 } q_S^{t-1}$），延续上文"动态优势与成本劣势的博弈"逻辑
- **均衡框架延伸**：此设定使反应函数从静态 $R_C^t(q_S^{t-1})$ 升级为动态预测工具，为后续推导 Stackelberg 均衡（如 Simon 会将 $q_C$ 代入其利润函数）奠定基础，直接呼应上文"先动者攫取超额剩余"的结论。

图片内容通过对称案例完整验证了上文理论框架，动态调整序列展示了均衡的收敛过程，而新增的时序细节则自然衔接到非对称决策的Stackelberg模型，保持了寡头竞争分析逻辑的严密递进。

---
### Page/Slide 5



# Stackelberg 寡头模型解析

## 1. 文字与公式提取

### 所有文字内容
- (a) If Carl plants enough pumpkins to yield $q_C^t$ this year, then Simon knows that the profit-maximizing amount to produce this year is $q_S^t = 1,200 - q_C^t/2$.
- (b) When Carl plants his pumpkins, he understands how Simon will make his decision. Therefore Carl knows that the amount that Simon will produce this year will be determined by the amount that Carl produces. In particular, if Carl's output is $q_C^t$, then Simon will produce and sell $1,200 - q_C^t/2$ and the total output of the two producers will be $1,200 + q_C^t/2$. Therefore Carl knows that if his own output is $q_C$, the price of pumpkins in the market will be $1.25 - q_C^t/3,200$.
- (c) In the last part of the problem, you found how the price of pumpkins this year in the Farmers' Market is related to the number of pumpkins that Carl produces this year. Now write an expression for Carl's total revenue in year $t$ as a function of his own output, $q_C^t$. $1.25q_C^t - (q_C^t)^2/3,200$. Write an expression for Carl's marginal revenue in year $t$ as a function of $q_C^t$. $1.25 - q_C^t/1,600$.
- (d) Find the profit-maximizing output for Carl. $1,200$. Find the profit-maximizing output for Simon. $600$. Find the equilibrium price of pumpkins in the Lake Witchisit Farmers' Market. $\$7/8$. How much profit does Carl make? $\$450$. How much profit does Simon make? $\$225$. An equilibrium of the type we discuss here is known as a Stackleberg equilibrium.
- (e) If he wanted to, it would be possible for Carl to delay his planting until the same time that Simon planted so that neither of them would know the other's plans for this year when he planted. Would it be in Carl's interest to do this? Explain. No. Carl's profits in Stackleberg equilibrium are larger than in Cournot equilibrium. So if the output

### 所有公式内容
1. Simon的反应函数：$q_S^t = 1,200 - q_C^t/2$
2. 总产量：$1,200 + q_C^t/2$
3. 市场价格：$p = 1.25 - q_C^t/3,200$
4. Carl的总收入：$TR_C = 1.25q_C^t - (q_C^t)^2/3,200$
5. Carl的边际收入：$MR_C = 1.25 - q_C^t/1,600$

## 2. 模型解析

### 2.1 Stackelberg模型与上文Cournot模型的对比

#### 模型结构差异
- **上文Cournot模型**：双寡头**同时行动**，各自基于对方上期产量的预测决定本期产量
  - 均衡条件：$q_S = 1,200 - q_C/2$ 和 $q_C = 1,200 - q_S/2$
  - 均衡结果：$q_C^* = q_S^* = 800$，$p^* = \$1$，$π_C = π_S = \$400$
- **当前Stackelberg模型**： Carl作为**领导者先行动**，Simon作为**跟随者后行动**
  - Simon反应函数内生化：$q_S = 1,200 - q_C^t/2$（直接依赖Carl当期产量）
  - Carl预先知道Simon反应并据此选择最优产量

### 2.2 模型推导验证

#### 需求函数重构
由市场价格函数 $p = 1.25 - q_C^t/3,200$ 与总产量 $q = 1,200 + q_C^t/2$ 可推导：
$$ p = 2 - \frac{q}{1,600} $$
- 当 $q = 1,600$ 时，$p = \$1$（与上文Cournot均衡价格一致）
- 当 $q = 1,800$（Stackelberg总产量）时，$p = 2 - 1,800/1,600 = \$7/8$

#### 利润最大化验证
- **Carl（领导者）利润最大化**：
  $$ MR = MC \Rightarrow 1.25 - \frac{q_C}{1,600} = 0.5 \Rightarrow q_C^* = 1,200 $$
- **Simon（跟随者）产量**：
  $$ q_S^* = 1,200 - \frac{q_C^*}{2} = 1,200 - 600 = 600 $$
- **利润计算**：
  - Carl：$π_C = (\frac{7}{8} - 0.5) \times 1,200 = \$450$
  - Simon：$π_S = (\frac{7}{8} - 0.5) \times 600 = \$225$

### 2.3 Stackelberg均衡的经济学含义

#### 先动优势量化验证
| 均衡类型 | Carl产量 | Simon产量 | 市场价格 | Carl利润 | Simon利润 | 总产量 |
|---|---|---|---|---|---|---|
| Cournot | 800 | 800 | \$1.00 | \$400 | \$400 | 1,600 |
| Stackelberg | **1,200** | 600 | \$0.875 | **\$450** | \$225 | 1,800 |

- **先动者超额利润**：Carl通过先行动策略，产量增加50%，利润提升12.5%（\$450 > \$400）
- **跟随者劣势**：Simon被迫减产25%，利润下降43.75%（\$225 < \$400）
- **市场效率差异**：Stackelberg总产量更高（1,800 > 1,600），价格更低，但利润分配更为不均

#### 与上文理论的连续性
- **验证27.2(0)新增细节**：Carl早种植的设定使模型从"抽象的先动优势假设"转化为**可计算的Stackelberg均衡**
- **强化反应函数作用**：Simon反应函数 $R_S(q_C) = 1,200 - q_C/2$ 从Cournot的**静态修正工具**转变为Stackelberg中的**内生决策依据**
- **利润对比解释(e)问**：Carl拒绝返回Cournot模式（不延迟种植），直接证明上文"先动者攫取超额剩余"的核心结论

### 2.4 与上文案例的对比延伸

**策略结构差异的经济本质**：
- **Cournot**：两厂商在**时间对称**下进行产量博弈，均衡解呈对称分布
- **Stackelberg**：引入**时间非对称性**，领导者通过**产量承诺**影响跟随者决策空间
- **均衡结果差异**：Stackelberg中先动方利用信息优势构建**自我约束的承诺机制**，使其边际收益曲线与Cournot模型存在本质差异（$1.25 - q_C/1,600$ vs Cournot下的不同MR曲线）

此模型完整展示了寡头竞争中**时间维度对均衡结果的决定性影响**，为理解企业战略行为中的"先行者优势"提供了微观基础。

---
### Page/Slide 6



# 寡头垄断模型的延伸解析

## 1. 当前图片内容提取

### 文字内容
- 页面标题：`326 OLIGOPOLY (Ch. 27)`
- 正文段落：`when neither knows the other's output this year until after planting time is a Cournot equilibrium, Carl will want Simon to know his output.`
- 习题 27.3 (0)：`Suppose that Carl and Simon sign a marketing agreement. They decide to determine their total output jointly and to each produce the same number of pumpkins. To maximize their joint profits, how many pumpkins should they produce in toto?  1,200. How much does each one of them produce?  600. How much profit does each one of them make?  450.`
- 习题 27.4 (0)：`The inverse market demand curve for bean sprouts is given by P(Y) = 100 - 2Y, and the total cost function for any firm in the industry is given by TC(y) = 4y.`
  - `(a)`：`The marginal cost for any firm in the industry is equal to $4. The change in price for a one-unit increase in output is equal to $-2.`
  - `(b)`：`If the bean-sprout industry were perfectly competitive, the industry output would be 48, and the industry price would be $4.`
  - `(c)`：`Suppose that two Cournot firms operated in the market. The reaction function for Firm 1 would be y₁ = 24 - y₂/2. (Reminder: Unlike the example in your textbook, the marginal cost is not zero here.) The reaction function of Firm 2 would be y₂ = 24 - y₁/2. If the firms were operating at the Cournot equilibrium point, industry output would be 32, each firm would produce 16, and the market price would be $36.`
  - `(d)`：`For the Cournot case, draw the two reaction curves and indicate the equilibrium point on the graph below.`

### 公式内容
- 反需求函数：$P(Y) = 100 - 2Y$
- 成本函数：$TC(y) = 4y$
- 企业1反应函数：$y_1 = 24 - y_2/2$
- 企业2反应函数：$y_2 = 24 - y_1/2$

## 2. 模型解析与上文知识的连续性

### 2.1 卡特尔均衡 vs. Cournot/Stackelberg均衡 (关联27.3习题)

当前图片中27.3习题展示的**卡特尔合谋**情景与上文知识点形成关键对比：

| 均衡类型 | 总产量 | 单厂商产量 | 单厂商利润 | 定价机制 |
|---------|--------|------------|------------|----------|
| 卡特尔 | 1,200 | 600 | $450 | 联合利润最大化 |
| Cournot | 1,600 | 800 | $400 | 同时决策的纳什均衡 |
| Stackelberg | 1,800 | Carl:1,200<br>Simon:600 | Carl:$450<br>Simon:$225 | 领导者-跟随者动态均衡 |

**经济学含义连续性：**
- 卡特尔产出(1,200)小于Cournot(1,600)和Stackelberg(1,800)，验证了**合谋会减少总产量**、提高价格
- 卡特尔下单厂商利润($450)与Stackelberg中Carl利润相等，但**稳定性差异**：
  - Stackelberg中Carl的$450来自**先动优势**（上文2.3节验证）
  - 卡特尔中$450来自**合作约束**，需解决搭便车问题
- 正文句"Carl will want Simon to know his output"呼应上文Stackelberg核心：**领导者需要被跟随者观测到产量承诺**

### 2.2 豆芽市场Cournot模型的普适性 (关联27.4习题)

27.4习题中豆芽市场的数学结构与上文南瓜模型保持完全一致的**理论框架**：

- **反应函数同构性**：
  - 南瓜模型：$q_S = 1,200 - q_C/2$（上文知识点）
  - 豆芽模型：$y_1 = 24 - y_2/2$
  - 系数差异源于具体参数（南瓜案例有特定市场需求函数，豆芽案例给定$P(Y)=100-2Y$）

- **利润最大化条件一致**：
  ```math
  \begin{align*}
  \text{上文南瓜模型:} & \quad MR = 1.25 - q_C/1,600 = MC = 0.5 \\
  \text{豆芽模型(Cournot):} & \quad MR = 100 - 4y_1 - 2y_2 = MC = 4
  \end{align*}
  ```
  代入对称均衡解$y_1 = y_2$可得$y_i = 16$，验证了27.4(c)中结果

- **关键参数对比**：
  | 模型 | 边际成本 | 需求斜率 | 均衡产量/厂商 | 均衡价格 |
  |------|----------|----------|----------------|-----------|
  | 南瓜 | $0.50 | -1/1,600 | 800 (Cournot) | $1.00 |
  | 豆芽 | $4.00 | -2 | 16 (Cournot) | $36.00 |
  | 边际成本差异直接导致均衡产量和价格水平不同，但产业结构特征保持一致 |

### 2.3 市场结构比较的深层含义

当前图片内容强化了上文2.4节所述**策略结构差异的经济本质**：

- **完全竞争基准 (27.4(b))**：
  - 豆芽市场$P = MC \Rightarrow 100-2Y = 4 \Rightarrow Y=48$
  - 对比南瓜市场Cournot均衡(1,600)，验证**寡头竞争下的产出介于垄断与完全竞争之间**

- **垄断势力量化**：
  - 南瓜卡特尔总产1,200 vs. Cournot 1,600 → 减产25%
  - 豆芽卡特尔总产：垄断产量$MR=MC \Rightarrow 100-4Y=4 \Rightarrow Y=24$ vs. Cournot 32 → 减产25%
  - **相同减产比例**证明不同寡头模型具有普适性规律

- **反应函数几何意义 (27.4(d))**：
  - 斜率为-1/2的反应曲线交点即Cournot均衡(16,16)
  - 与上文南瓜模型对比可见：**无论边际成本是否为零**，只要需求形式相似，反应函数就保持相同斜率结构

> **知识连续性总结**：图片内容将上文Stackelberg-Cournot对比框架拓展至**合谋行为**，并通过新案例验证了寡头理论的核心规律——不同市场结构（合谋、同时行动、序列行动）产生系统性产量与利润差异，且数学结构具有普适性。特别是卡特尔利润($450)与Stackelberg领导者利润相等，解释了上文"Carl拒绝返回Cournot模式"的行为动机：**先动优势与合谋利润水平相当，但无需合作约束**。

---
### Page/Slide 7



# 微观经济学解析：豆芽市场策略互动模型

## 1. 图片内容提取

### 图表信息
- **坐标轴**：
  - 横轴：$y_1$（ Firm 1 产量），刻度 0-24
  - 纵轴：$y_2$（ Firm 2 产量），刻度 0-24
- **反应函数**：
  - Firm 1's reaction function（从左上向右下倾斜的直线）
  - Firm 2's reaction function（从左上向右下倾斜的直线）
- **交点**：标记为 $e$（表示Cournot均衡点）

### 文本内容
- **(e)** If the two firms decided to collude, industry output would be **24** and the market price would equal **$52**.
- **(f)** Suppose both of the colluding firms are producing equal amounts of output. If one of the colluding firms assumes that the other firm would not react to a change in industry output, what would happen to a firm's own profits if it increased its output by one unit? **Profits would increase by $22**.
- **(g)** Suppose one firm acts as a Stackleberg leader and the other firm behaves as a follower. The maximization problem for the leader can be written as:
  ```
  max_y1 [100 - 2(y1 + 24 - y1/2)]y1 - 4y1
  ```
  Solving this problem results in the leader producing an output of **24** and the follower producing **12**. This implies an industry output of **36** and price of **$28**.
- **27.5 (0)** Grinch is the sole owner of a mineral water spring that costlessly bubbles forth as much mineral water as Grinch cares to bottle. It costs Grinch $2 per gallon to bottle this water. The inverse demand curve for Grinch's mineral water is $p = \$20 - .20q$, where $p$ is the price per gallon and $q$ is the number of gallons sold.

## 2. 图表解析与经济学含义

### 2.1 反应函数与Cournot均衡
- 图中两条反应函数显示了豆芽市场双寡头的**策略依赖关系**：
  - 所有反应函数斜率为 $-1/2$，与上文"反应函数同构性"完全一致（对比南瓜模型 $q_S = 1,200 - q_C/2$，此处为 $y_1 = 24 - y_2/2$）
- **交点 $e$** 对应Cournot均衡，其坐标为 $(16,16)$，总产量 $Y = 32$
  - 验证上文知识点：完全竞争产量48 > Cournot 32 > 卡特尔24，清晰展现**寡头产出介于垄断与完全竞争之间**的规律

### 2.2 卡特尔合谋的稳定性问题
- 文本(e)显示卡特尔总产出为24（各厂商产12），对比Cournot均衡32，**减产25%**，与上文知识点总结一致
- 文本(f)揭示关键经济学含义：
  - 利润增加$22的单方偏离收益表明：**每个厂商都有激励背叛合谋**
  - 定量验证上文"卡特尔需解决搭便车问题"的论断，解释为何合谋是**不稳定的纳什均衡**

### 2.3 Stackelberg动态均衡
- 文本(g)的max问题公式展示**领导者决策机制**：
  - $24 - y_1/2$ 是跟随者的反应函数
  - 领导者将跟随者反应内生化，将其代入自身利润函数：$[100 - 2(y_1 + y_2)]y_1 - 4y_1$
- 结果验证上文"先动优势"理论：
  - 领导者产量(24) > 均衡产量(16) → 获取先动租金
  - 与上文Simon/Carl案例对比：本例总产量(36) > Cournot(32)，再次确认**序列行动增加市场总产出**

### 2.4 模型理论框架对比

| 市场结构 | 总产量 | 单厂商产量 | 市场价格 | 关键经济含义 |
|----------|--------|------------|----------|--------------|
| 卡特尔 | 24 | 12 | $52 | 通过合谋减产25%获取垄断租金（但存在$22的背叛激励） |
| Cournot | 32 | 16 | $36^*$ | 同时决策的纳什均衡（交点$e$) |
| Stackelberg | 36 | 领导者:24<br>跟随者:12 | $28 | 反应函数曲线交点移动，证明**领导者承诺效应** |

> *注：Cournot价格未直接给出，但可由需求曲线$P=100-2Y$计算：$P=100-2×32=\$36$*

## 3. 与上文知识体系的连续性

- **反应函数几何意义强化**：图表直观展示$-1/2$斜率的反应曲线交点即均衡，与上文"无论边际成本是否为零，只要需求形式相似，反应函数就保持相同斜率结构"完全吻合
- **合谋-领导力比较**：卡特尔利润$450（上文）与本例中领导者利润部分同源，但：
  - 卡特尔利润来自脆弱的合作约束
  - Stackelberg利润来自可置信的先动承诺（呼应"Carl will want Simon to know his output"）
- **量化搭便车问题**：本例$f$部分$22的背叛收益为上文"合谋稳定性差异"提供精确度量，解释为何**承诺机制比单纯合谋更可靠**的深层原因

> 图表与文本共同验证了寡头理论核心规律：**三种市场结构产生系统性差异**，其数学本质（反应函数结构→均衡结果）具有跨行业普适性。当厂商具有观测能力（如Stackelberg领导者），策略替代完全合谋，这正是上文"Carl拒绝返回Cournot模式"的行为逻辑基础：与其冒险合谋，不如凭借先动优势实现同样可观但更稳定的利润水平。

---
### Page/Slide 8



# 提取的文字与公式

## 文字内容
- `328 OLIGOPOLY (Ch. 27)`
- `(a) Write down an expression for profits as a function of q: Π(q) = (20 − .20q)q − 2q. Find the profit-maximizing choice of q for Grinch. 45.`
- `(b) What price does Grinch get per gallon of mineral water if he produces the profit-maximizing quantity? $11. How much profit does he make? $405.`
- `(c) Suppose, now, that Grinch’s neighbor, Grubb finds a mineral spring that produces mineral water that is just as good as Grinch’s water, but that it costs Grubb $6 a bottle to get his water out of the ground and bottle it. Total market demand for mineral water remains as before. Suppose that Grinch and Grubb each believe that the other’s quantity decision is independent of his own. What is the Cournot equilibrium output for Grubb? 50/3. What is the price in the Cournot equilibrium? $9.33.`
- `27.6 (1) Albatross Airlines has a monopoly on air travel between Peoria and Dubuque. If Albatross makes one trip in each direction per day, the demand schedule for round trips is q = 160 − 2p, where q is the number of passengers per day. (Assume that nobody makes one-way trips.) There is an “overhead” fixed cost of $2,000 per day that is necessary to fly the airplane regardless of the number of passengers. In addition, there is a marginal cost of $10 per passenger. Thus, total daily costs are $2,000+10q if the plane flies at all.`
- `(a) On the graph below, sketch and label the marginal revenue curve, and the average and marginal cost curves.`

## 公式与参数
- Grinch 利润函数：`Π(q) = (20 - 0.20q)q - 2q`
- Grinch 利润最大化产量：`q = 45`
- Grinch 定价：`p = $11`，利润：`$405`
- Grubb 边际成本：`$6`
- 市场需求函数（Albatross）：`q = 160 - 2p`
- Albatross 成本结构：  
  - 总成本 `TC = $2,000 + 10q`  
  - 边际成本 `MC = 10`  
  - 平均成本 `AC = 2000/q + 10`
- Cournot 均衡结果（Grubb）：`q_B = 50/3`，价格 `$9.33`

## 图表标注
- 坐标轴：  
  - X轴（Quantity, Q）：刻度 `0, 20, 40, 60, 80`  
  - Y轴（MR, MC）：刻度 `20, 40, 60, 80`  
- 曲线标记：  
  - `mr`：指向向下倾斜的边际收益曲线  
  - `mc`：指向水平直线（边际成本）  
  - `ac`：指向递减的平均成本曲线  

---

# 图表解析与经济学含义

## 图表核心特征
1. **MR 曲线**  
   由需求函数 `$q = 160 - 2p$` 推导得反需求 `$p = 80 - 0.5q$`，故 `$MR = 80 - q$`。  
   - 表现为截距 80、斜率 -1 的直线（当 `$q=0$` 时 `$MR=80$`；`$q=80$` 时 `$MR=0$`）。  
   - 体现垄断厂商的**边际收益递减特性**：为扩大销量需降价，导致 `$MR < p$`。

2. **MC 曲线**  
   - 恒定于 10 的水平线，反映 Albatross 的常数边际成本（`$10/乘客$`），与上文寡头模型中 "优先阶段确定的边际成本" 分析逻辑一致。

3. **AC 曲线**  
   - `$AC = 2000/q + 10$`，表现为递减曲线（随产量增加向 MC 逼近）。  
   - 体现**固定成本摊薄效应**：初始高成本因规模扩大逐步降低，符合上文 "规模经济影响平均成本" 的底层原理。

## 与上文知识点的连续性解读
- **垄断作为合谋基准**：  
  图表完整展示 **MR=MC 时的垄断均衡点**（`$q_M=70$`, `$p_M=45$`），直接对应上文知识点中 **卡特尔的理想目标**。当 Grinch 单独经营时（问题 a-b），其产量 45 与价格 11 即为该垄断模型的实例化，验证 "卡特尔试图复制垄断产出" 的理论基础。

- **寡头竞争对均衡的扰动**：  
  问题 (c) 中引入 Grubb 后，形成**非对称成本 Cournot 模型**（`$c_G=2$`, `$c_B=6$`）：  
  - Grinch 反应函数：`$q_G = 45 - 0.5q_B$`  
  - Grubb 反应函数：`$q_B = 35 - 0.5q_G$`（截距差异源于成本不对称）  
  两反应函数斜率一致（`$-1/2$`），**严格延续上文 "反应函数同构性" 规律**：需求结构决定斜率，成本差异仅影响截距。均衡总产量 `$160/3 \approx 53.3$` 高于垄断产量 45，价格 `$9.33$` 低于垄断价格 `$11$`，动态重申 "Cournot 产量 > 卡特尔产量" 的层级关系。

- **搭便车问题的微观起源**：  
  图表中 **AC 递减特性**（固定成本占比高）加剧合谋脆弱性。与上文计算的 `$22$` 背叛收益同理，高固定成本市场中，任何厂商减产都会显著推高其他厂商的 **AC**，形成强烈单方增产激励。这为上文 "卡特尔需解决容量过剩导致的不稳定性" 提供直接图解逻辑。

> 本图表与 Grinch 案例共同构成**市场结构演进的完整链条**：从垄断（a-b）检验合谋可行性，到 Cournot 竞争（c）揭示均衡偏移，最后通过垄断图形化模型锚定所有寡头理论的参照系。其 MR-MC 交点动态为上文 "先动优势"（Stackelberg）与 "合谋维持"（Cartel）的定量分析奠定基础。

---
### Page/Slide 9



## 当前图片文字与公式提取

### 文字内容
- **(b)** Calculate the profit-maximizing price and quantity and total daily profits for Albatross Airlines. $ p = 45 $, $ q = 70 $, $ \pi = \$450 $ per day.
- **(c)** If the interest rate is 10% per year, how much would someone be willing to pay to own Albatross Airlines’s monopoly on the Dubuque-Peoria route. (Assuming that demand and cost conditions remain unchanged forever.) About \$1.6 million.
- **(d)** If another firm with the same costs as Albatross Airlines were to enter the Dubuque-Peoria market and if the industry then became a Cournot duopoly, would the new entrant make a profit? No; losses would be about \$900 per day.
- **(e)** Suppose that the throbbing night life in Peoria and Dubuque becomes widely known and in consequence the population of both places doubles. As a result, the demand for airplane trips between the two places doubles to become $ q = 320 - 4p $. Suppose that the original airplane had a capacity of 80 passengers. If AA must stick with this single plane and if no other airline enters the market, what price should it charge to maximize its output and how much profit would it make? $ p = \$60 $, $ \pi = \$2,000 $.
- **(f)** Let us assume that the overhead costs per plane are constant regardless of the number of planes. If AA added a second plane with the same costs and capacity as the first plane, what price would it charge? \$45. How many tickets would it sell? 140. How much would its profits be? \$900. If AA could prevent entry by another competitor, would it choose to add a second plane? No.
- **(g)** Suppose that AA stuck with one plane and another firm entered the market with a plane of its own. If the second firm has the same cost function as the first and if the two firms act as Cournot oligopolists, what will be the price, \$40, quantities, 80, and profits? \$400.
- **27.7 (0)** Alex and Anna are the only sellers of kangaroos in Sydney, Australia. Anna chooses her profit-maximizing number of kangaroos to sell, $ q_1 $, based on the number of kangaroos that she expects Alex to sell. Alex knows how Anna will react and chooses the number of kangaroos that  

### 公式与关键参数
- **需求函数（问题 e）**: $ q = 320 - 4p $
- **价格与产量（问题 b）**: $ p = 45 $, $ q = 70 $, $ \pi = 450 $
- **价格与利润（问题 e）**: $ p = 60 $, $ \pi = 2,000 $
- **价格与利润（问题 f）**: $ p = 45 $, quantity = 140, $ \pi = 900 $
- **Cournot 结果（问题 g）**: $ p = 40 $, total quantity = 80, $ \pi = 400 $ (per firm)

---

## 经济学解析与知识连续性

### 垄断均衡的验证（对应问题 b）
- 问题 (b) 中 $ q = 70 $, $ p = 45 $, $ \pi = 450 $ **直接量化了上文垄断模型**：  
  由上文需求函数 $ q = 160 - 2p $ 推导反需求 $ p = 80 - 0.5q $，MR 曲线为 $ MR = 80 - q $，与 MC = 10 的交点 $ q_M = 70 $ 严格匹配。  
  - 利润 $ \pi = (45 \times 70) - (2,000 + 10 \times 70) = 450 $ 验证了 **固定成本分摊效应**：当产量增至 70 时，AC 从初始 $ \infty $ 降至 $ 2,000/70 + 10 \approx 38.57 $，使价格 $ p > AC $ 形成正利润。
  - 此结果锚定 **卡特尔的合谋基准**：上文指出合谋理想状态即复制此垄断产出，但寡头竞争会偏离此点（见问题 d/g）。

### 垄断价值的动态延伸（对应问题 c）
- $1.6$ million 的 monopoly value 计算 **强化了市场结构对资本估值的约束**：  
  年利润 $ 450 \times 365 = 164,250 $ 除以 10% 利率得永续价值 $ 1,642,500 \approx 1.6 $ million，体现 **静态垄断效率与长期资本回报的权衡**。  
  - 与上文 "Cournot 均衡削弱垄断势力" 逻辑一致：若竞争使利润趋零（如问题 d），垄断价值将归零，重申 "市场结构稳定性是资本估值前提"。

### 寡头竞争的实证扰动（对应问题 d 与 g）
- **Cournot 损失（问题 d）**：新 entrant 亏损 $ 900 $/day **实证了上文 "寡头竞争降低产业吸引力" 的推论**。  
  - 双寡头 Cournot 模型中，对称成本下反应函数 $ q_i = 35 - 0.5q_j $（推导自需求 $ q = 160 - 2p $ 和 MC=10），均衡 $ q_1 = q_2 = 160/3 \approx 53.3 $，总产出 $ 106.6 > 70 $，价格 $ p = (160 - 106.6)/2 = 26.7 $，但单家企业产量 $ 53.3 > $ 垄断分产量（70/2=35），导致 AC $ = 2,000/53.3 + 10 \approx 47.5 $ 高于价格，利润为负——**印证 "合谋需抑制过度产出" 的脆弱性**。
- **对称 Cournot 结果（问题 g）**：$ p = 40 $, total $ q = 80 $, $ \pi = 400 $ **呼应上文 Cournot 均衡层级**：  
  - 需求未变时，问题 (g) 等同于问题 (d)，但答案中 $ \pi = 400 $ 暗示回本条件（如固定成本调整），直接关联上文 "非协作下价格 $ \approx \$9.33 $" 的逻辑链条：产量上升压低价格，利润空间被侵蚀。

### 需求扩张与产能约束（对应问题 e 与 f）
- **需求翻倍（问题 e）**：新需求 $ q = 320 - 4p $（原 $ q = 160 - 2p $ 的同比例放大）**验证了上文 "规模经济对均衡的影响机制"**。  
  - 虽产能限 80 人，但反需求 $ p = 80 - 0.25q $ 使 MR = 80 - 0.5q，MC=10 下理论 $ q_M = 140 $。因产能约束，AA 选择 $ q = 80 $, $ p = 60 $，利润 $ \pi = (60 \times 80) - (2,000 + 800) = 2,000 $——**凸显 "产能刚性迫使偏离理论 MR=MC 点"**，与上文 "固定成本占比高加剧合谋不稳定性" 一致。
- **多飞机决策（问题 f）**：  
  - 添加第二飞机后 $ q = 140 $, $ p = 45 $, $ \pi = 900 $ 说明 **产能扩展无法完全规避固定成本陷阱**：总成本 $ TC = 2 \times 2,000 + 10 \times 140 = 5,400 $，AC = 38.57仍高于价格（45），但利润增量 $ 900 - 450 = 450 $ 低于固定成本 $ 2,000 $，故理性拒扩——**量化了上文 "高固定成本市场合谋失败" 的微观根源**。

### 知识连续性总结
当前图片零散的数值解 **系统化串联了上文市场结构演进框架**：  
- (b) 确立垄断参照系 → (c) 量化垄断价值 → (d/g) 验证 Cournot 偏移 → (e/f) 展示需求与产能扰动。  
- 所有结果均植根于 **相同技术参数**（MC=10, FC=2,000, $ q = 160 - 2p $），但 **需求扩张 (e) 和对称寡头 (g) 拓展了分析维度**，为上文 "先动优势"（Stackelberg）或 "容量限制战略" 提供实证铺垫，同时强调 **合谋可行性高度依赖产业基本面**（如需求弹性和成本结构），避免脱离上文理论的孤立解读。

---
### Page/Slide 10



# 当前图片解析

## 1. 文字与公式提取

### 全文内容  
330 OLIGOPOLY (Ch. 27)  
she herself will sell, $q_2$, after taking this information into account. The inverse demand function for kangaroos is $P(q_1 + q_2) = 2,000 - 2(q_1 + q_2)$. It costs $400$ to raise a kangaroo to sell.  

$(a)$ Alex and Anna are Stackelberg competitors. **Alex** is the leader and **Anna** is the follower.  

$(b)$ If Anna expects Alex to sell $q_2$ kangaroos, what will her own marginal revenue be if she herself sells $q_1$ kangaroos?  
$MR(q_1 + q_2) = 2,000 - 4q_1 - 2q_2$.  

$(c)$ What is Anna’s reaction function, $R(q_2)$?  
$R(q_2) = 400 - \frac{1}{2}q_2$.  

$(d)$ Now if Alex sells $q_2$ kangaroos, what is the total number of kangaroos that will be sold?  
$400 + \frac{1}{2}q_2$.  
What will be the market price as a function of $q_2$ only?  
$P(q_2) = 1,200 - q_2$.  

$(e)$ What is Alex’s marginal revenue as a function of $q_2$ only?  
$MR(q_2) = 1,200 - 2q_2$.  
How many kangaroos will Alex sell?  
$400$.  
How many kangaroos will Anna sell?  
$200$.  
What will the industry price be?  
$\$800$.  

27.8 (0)  
Consider an industry with the following structure. There are 50 firms that behave in a competitive manner and have identical cost functions given by $c(y) = y^2 / 2$. There is one monopolist that has 0 marginal costs. The demand curve for the product is given by  
$D(p) = 1,000 - 50p$.  

$(a)$ What is the supply curve of one of the competitive firms?  
$y = p$.  
The total supply from the competitive sector at price $p$ is  
$S(p) = 50p$.  

$(b)$ If the monopolist sets a price $p$, the amount that it can sell is  
$D_m(p) = 1,000 - 100p$.  

---

## 2. 内容解析

### 核心机制与上文知识连续性
当前图片系统呈现 **Stackelberg领导者-追随者模型** 及 **混合市场结构（垄断者+竞争性边缘）** 的实证案例，直接延续上文对寡头动态的竞争性演化的讨论：
- **Stackelberg模型的动态验证**：  
  需求 $P = 2,000 - 2Q$ 与 $MC = 400$ 的设定，推导出均衡结果（Alex产400，Anna产200，$P = 800$）。这实证了上文知识点总结中预设的 **“先动优势”（Stackelberg动态）**：  
  - 上文指出Cournot均衡（问题d）导致过度产出（总产出106.6 > 垄断产出70），侵蚀利润；此案例中，Stackelberg总产出600 > 垄断产出400（计算：$MR = 2,000 - 4Q = 400 \implies Q = 400$），但**低于双寡头Cournot均衡的533.3**（计算：$q_i = (2,000 - 400)/(2 \times 3) \approx 266.7$）。这印证了“先动者通过产能承诺抑制追随者产出”的机制——Alex作为领导者将产量推至400，迫使Anna仅产200，强化了 **“合谋需控制产能扩张以维持价格”的脆弱性**（呼应上文“固定成本占比高加剧合谋不稳定性”）。
  - 产业吸引力变化：Stackelberg价格（\$800）低于Cournot价格（\$933.3），但高于垄断价格（\$1,200），体现 **竞争层级对利润的梯度侵蚀**，直接延续问题d中“寡头竞争降低产业吸引力”的推论。例如，若固定成本类似上文（\$2,000），Stackelberg下单家利润将受制于更高总产出，压缩AC优势。

- **混合市场结构与残余需求逻辑**：  
  27.8 (0) 部分中，垄断者面对竞争性边缘的残余需求 $D_m(p) = 1,000 - 100p$，与上文问题e **需求扩张与产能约束** 的机制高度一致：  
  - 竞争性部门的总供给 $S(p) = 50p$ 相当于一个“弹性产能池”，垄断者必须在其之上优化产出，类似上文需求翻倍后AA面临产能刚性（80人限制）。  
  - 残余需求的推导 $D_m = D - S$ 量化了 **外部竞争对垄断租金的挤压**，与上文“产能扩展无法完全规避固定成本陷阱”形成逻辑闭环：即便需求扩大（$D(p) = 1,000 - 50p$），垄断者仍受制于边缘企业供给，无法实现理论最大利润，**重申“市场结构稳定性是资本估值前提”**（上文问题c的垄断价值计算基础）。

### 关键延伸与理论衔接
- 此内容填补了上文知识点总结中“**为Stackelberg先动优势提供实证铺垫**”的缺口，展示时序竞争如何加剧产出偏离垄断最优（Stackelberg总产出>Cournot），但其均衡仍受成本结构约束（$MC = 400$ 超过上文$MC = 10$，放大价格波动敏感性）。
- **需求弹性与合谋可行性的实证**：  
  图片中需求弹性隐含在 $b = 2$ 参数中，若弹性较低（如上文需求 $q = 160 - 2p$），Stackelberg产出扩张会更显著压低价格，导致类似问题d的亏损；此处 $b = 2$ 但规模更大，避免了负利润，**直接验证“合谋可行性高度依赖产业基本面”**——需求规模需覆盖固定成本分摊（对比上文问题f的二飞机决策失败）。
- 避免孤立解读：所有公式（如Anna的反应函数 $R(q_2) = 400 - 0.5q_2$）均基于相同微观逻辑：企业行为由 $MR = MC$ 驱动，延续上文“资本估值-产量-价格”的动态链条，无需重复固定成本分摊等基础机制。

---
### Page/Slide 11



### 提取内容  
所有文字与公式提取自当前图片：  

- **(c)** The monopolist’s profit-maximizing output is \( y_m = 500 \). What is the monopolist’s profit-maximizing price? \( p = 5 \).  
- **(d)** How much output will the competitive sector provide at this price? \( 50 \times 5 = 250 \). What will be the total amount of output sold in this industry? \( y_m + y_c = 750 \).  
- **27.9 (0)** Consider a market with one large firm and many small firms. The supply curve of the small firms taken together is  
  \[ S(p) = 100 + p. \]  
  The demand curve for the product is  
  \[ D(p) = 200 - p. \]  
  The cost function for the one large firm is  
  \[ c(y) = 25y. \]  
  **(a)** Suppose that the large firm is forced to operate at a zero level of output. What will be the equilibrium price? \( 50 \). What will be the equilibrium quantity? \( 150 \).  
  **(b)** Suppose now that the large firm attempts to exploit its market power and set a profit-maximizing price. In order to model this we assume that customers always go first to the competitive firms and buy as much as they are able to and then go to the large firm. In this situation, the equilibrium price will be \( \$37.50 \). The quantity supplied by the large firm will be \( 25 \), and the equilibrium quantity supplied by the competitive firms will be \( 137.5 \).  
  **(c)** What will be the large firm’s profits? \( \$312.50 \).  
  **(d)** Finally suppose that the large firm could force the competitive firms out of the business and behave as a real monopolist. What will be the equilibrium price? \( \frac{225}{2} \). What will be the equilibrium quantity? \( \frac{175}{2} \). What will be the large firm’s profits? \( \left( \frac{175}{2} \right)^2 \).  

---

### 内容解析  

#### 知识连续性与机制验证  
当前图片内容直接延续【上文知识点总结】中的 **残余需求（residual demand）逻辑** 和 **混合市场结构分析框架**，但通过新参数深化对“**边缘竞争对主导企业定价权的约束**”的理解，避免重复已述机制（如残余需求公式 \( D_m(p) = D(p) - S(p) \)），聚焦数值实现与动态推演：  

1. **图片前半部分（(c)-(d)）作为上文知识点的实证延伸**：  
   - 上文知识点给出需求 \( D(p) = 1,000 - 50p \) 和竞争性总供给 \( S(p) = 50p \)，导出残余需求 \( D_m(p) = 1,000 - 100p \)。图片 (c)-(d) 以 \( y_m = 500 \)、\( p = 5 \) 量化此关系：  
     - 当 \( p = 5 \)，竞争性供给 \( S(5) = 50 \times 5 = 250 \)（与上文一致），总产出 \( y_m + y_c = 750 \)。  
     - **关键连续性**：此结果验证上文强调的 **“垄断者利润受竞争性边缘挤压”**——上文指出 \( D_m(p) \) 可被视作“有效垄断需求”，而图片数据显性化了垄断租金的损耗：若无竞争性部门，垄断者将按 \( D(p) \) 定价（如 \( p=10 \) 时 \( y=500 \)），但竞争性部门迫使价格降至 5，总产出扩大至 750，印证上文“**市场结构稳定性直接影响资本估值**”（问题 c 的垄断价值计算基础）。  

2. **问题 27.9 深化混合市场结构的动态演化**：  
   - **模型设定差异与逻辑一致性**：  
     - 上文知识点中竞争性供给 \( S(p) = 50p \) 为纯边际成本导向（隐含 0 固定成本），而 27.9 中 \( S(p) = 100 + p \) 引入 **固定供应阈值**（小企业供给始终至少 100 单位），模拟现实中边缘企业的刚性产能，**直接呼应上文“固定成本占比高加剧合谋不稳定性”**（【上文知识点总结】第 2 部分）。  
     - 大企业成本 \( c(y) = 25y \)（MC=25）替代上文 MC=0 的设定，使分析聚焦 **成本结构对价格-产出权衡的影响**。  
   - **子问题解析与理论衔接**：  
     - **(b) 部分**：大企业设定 \( p = \$37.50 \) 时，残余需求 \( D_m(p) = D(p) - S(p) = (200 - p) - (100 + p) = 100 - 2p \)。  
       - 垂直整合上文机制：顾客优先购买竞争性产品（先满足 \( S(p) \)）等同于 **“产能承诺”**（Stackelberg 模型核心），使大企业面临向下倾斜的残余需求，但 **产出（25）显著低于纯垄断水平（(d) 中 87.5）**——这**实证了上文结论**：“边缘竞争迫使主导企业产出低于理论垄断最优，但高于竞争均衡”（27.9(a) 竞争价格 50 vs (b) 价格 37.5 vs (d) 垄断价格 112.5）。  
     - **(c) 与 (d) 部分对比**：  
       | 场景                | 价格       | 产量        | 利润               | 损失来源               |  
       |---------------------|------------|-------------|--------------------|------------------------|  
       | 主导企业定价 (b)    | \( 37.5 \) | \( 25 \)    | \( 312.5 \)        | 竞争性边缘分流需求     |  
       | 纯垄断 (d)          | \( 112.5 \) | \( 87.5 \) | \( (175/2)^2 \)    | 无竞争性边缘           |  
       - **关键推论**：利润差值 \( (175/2)^2 - 312.5 \approx 7,656.25 - 312.5 = 7,343.75 \) 量化了上文提出的 **“竞争性边缘对垄断租金的侵蚀强度”**。若产业固定成本较高（如上文问题 f 中二飞机决策），此损失可能将企业推向亏损临界点，**强化“市场结构性变量（如边缘企业占比）是资本估值先决条件”的论断**。  

#### 核心延伸价值  
- **混合结构演化路径的实证闭环**：27.9(b) 中价格 \( 37.50 \) 介于 (a) 竞争价格 (50) 和 (d) 垄断价格 (112.5) 之间，**动态展示产业吸引力梯度**，呼应上文“寡头竞争降低产业吸引力”的推论（【上文知识点总结】第 2 部分）。  
- **政策含义隐含**：(d) 部分假设主导企业排除竞争者，但现实中边缘企业难以强制退出（因 \( S(p) = 100 + p \) 表明其具备生存阈值），**凸显上文“合谋可行性依赖基本面”**——需求规模（\( D(p) = 200 - p \) 较上文更小）与成本结构（MC=25 > 上文 MC=10）共同导致纯垄断利润倍增，但需满足退出壁垒假设。  
- **避免冗余**：未重复供给/需求曲线推导（上文已阐明），而是聚焦新参数下 **“残余需求弹性”对定价空间的约束**：27.9 中 \( D_m(p) = 100 - 2p \) 的弹性低于上文 \( D_m(p) = 1,000 - 100p \)（因 \( b \) 从 100 降至 2），导致 (b) 价格降幅（vs 垄断）更平缓，**验证“需求弹性是市场力量强度的核心调节器”**（上文 Stackelberg 部分隐含逻辑）。

---
### Page/Slide 12



### 27.10 问题解析  

#### 1. 文字与公式提取  
- **问题描述**：  
  - Ben Kinmore 为 Bouncing Springs 唯一炉灶经销商。  
  - 购入成本：$20/个（ delivered to store）  
  - 道路布局：单一路线贯穿城镇，每英里一个农场，运输成本 $1/英里。  
  - 每个农场预留价格：$120（最多愿付此价，且仅需一个炉灶）。  
  - 定价策略：基础价 $p + 按距离加收运输费（$1/英里）。  

- **子问题 (a)**：  
  > If Ben set a base price of $p for cookstoves where $p < 120$, and if he charged $1 a mile for delivering them, what would be the total number of cookstoves he could sell? $2(120 - p)$. (Remember to count the ones he could sell to his east as well as to his west.) Assume that Ben has no other costs than buying the stoves and delivering them. Then Ben would make a profit of $p - 20$ per stove. Write Ben’s total profit as a function of the base price, $p$, that he charges: $2(120 - p)(p - 20) = 2(140p - p^2 - 2,400)$.  

- **子问题 (b)**：  
  > Ben’s profit-maximizing base price is $\$70$. (Hint: You just wrote profits as a function of prices. Now differentiate this expression for profits with respect to $p$.) Ben’s most distant customer would be located at a distance of $50$ miles from him. Ben would sell $100$ cookstoves and make a total profit of $\$5,000$.  

- **子问题 (c)**：  
  > Suppose that instead of setting a single base price and making all buyers pay for the cost of transportation, Ben offers free delivery of cookstoves. He sets a price $p$ and promises to deliver for free to any farmer who lives within $p - 20$ miles of him. (He won’t deliver to anyone who lives...  

#### 2. 经济学解析：市场结构与定价动态的延伸  
27.10 虽无直接竞争性部门，但通过**空间分散需求**（spatial dispersion）暗含类似上文 27.9 的混合市场结构逻辑，强化“资本估值依赖市场约束内生性”这一核心。关键衔接如下：  

- **需求约束的显性化与残余需求弹性**：  
  - (a) 中销量公式 $2(120 - p)$ 对应**空间维度的残余需求**：  
    - 预留价格 $120$ 和单位运输成本 $1$ 隐含需求曲线 $D(p) = 240 - 2p$（每侧 $120 - p$ 个农场，总 $240 - 2p$）。  
    - 与上文 27.9 的 $D_m(p) = 100 - 2p$ 类比，此处需求弹性 $| \epsilon | = \frac{p}{120 - p}$，**证实“需求弹性直接约束垄断定价空间”**。  
  - 利润函数 $2(120 - p)(p - 20)$ 体现**边际成本 $c = 20$ 对最优价格的压制**（上文 27.9 中 MC=25），解释为何最优价 $70$ 低于预留价 $120$——呼应上文“成本结构决定价格-产出权衡边界”。  

- **结构稳定性对资本估值的实证**：  
  - (b) 中利润 $\$5,000$ 量化**垄断租金规模**：  
    - 最优销量 $100$（而非 (a) 中 $2(120 - p)$ 的理论最大值 $240$）反映**空间摩擦内生的市场边界**，等同于“边缘竞争性部门”对垄断势力的侵蚀（类似上文 27.9(b) 中 $25 < 87.5$ 的产出缺口）。  
    - 利润 $\$5,000$ 直接关联资本估值：若固定成本（如囤积成本）加剧，此租金可能归零，**验证上文“固定成本占比升高削弱垄断可持续性”**（问题 f 中二飞机决策的逻辑延伸）。  

- **政策与动态演化的隐含逻辑**：  
  - (c) 引入免费配送，等价于**价格歧视策略**（覆盖 $p - 20$ 英里范围）。  
    - 与 27.9 中“主导企业应对边缘产能刚性”对比：此处 Ben 主动压缩有效市场半径，**实证“寡头竞争下市场操控需适配基本面”**（上文合谋可行性结论）；若物资短缺（如历史中铁路前中西部），此策略维持垄断稳定性，否则加速结构瓦解。  
  - 地理约束（$p - 20$ 英里）作为**外生边缘门槛**，替代上文 $S(p) = 100 + p$ 的固定阈值，**统一说明“市场完整性依赖结构性变量”**——无此约束时，Ben 可实现纯垄断（类似 27.9(d)），但配送成本导致租金损耗，呼应“寡头竞争降低产业吸引力”推论。  

> 注：延续 27.9 的分析路径，27.10 通过**空间异质性**将市场竞争机制内嵌于单垄断者模型，避免重复固定成本定义，但深化“结构参数（如预留价格、运输成本）作为资本估值先决条件”的框架连续性。

---
### Page/Slide 13



### 1. 文字与公式提取  
- **数值结果**：  
  - 设定价格：**\$120**  
  - 交付数量：**200**  
  - 总收入：**\$24,000**  
  - 总成本（含采购与配送）：**\$14,000**  
  - 利润：**\$10,000**  

- **关键公式**：  
  - 无差异点定价逻辑：  
    - 从 Ben 购买成本：$ p_B + x $  
    - 从 Huey 购买成本：$ p_H + (40 - x) $  
  - 利润计算隐含结构：  
    - 总成本 = 采购成本（$ 20 \times 200 = \$4,000 $） + 配送成本（\$10,000，基于平均运输距离）  

---

### 2. 经济学解析  

#### **(a) 免费配送策略与利润跃升的内在逻辑**  
- **利润对比的结构性原因**：  
  - 子问题 (b) 中消费者承担运输成本时，Ben 的最优基价 \$70 仅覆盖 **50 英里**范围（销量 100），利润 \$5,000。  
  - 免费配送允许 **边际成本内生化**：Ben 将运输成本（单位 \$1/英里）纳入定价，**消除了消费者对运输成本的敏感度**，使市场边界扩展至 **100 英里**（$ p - 20 = 100 $），销量翻倍至 200。  
  - 利润从 \$5,000 升至 \$10,000 的关键在于 **两阶段价值捕获**：  
    1. **高基价覆盖近端高支付意愿群体**：近端农民实际支付的“净价”（\$120）略低于预留价 \$120，但仍高于子问题 (b) 的 \$70；  
    2. **远端市场渗透**：通过承担运输成本，Ben 以 \$120 基价覆盖远端农民（原因是这些农民的运费已被隐性补贴），扩大销量。  

- **上文理论的实证延伸**：  
  - 此结果验证了 [上文解析] 中“**地理价格歧视可转化运输成本为垄断租金**”的论断。免费配送相当于 **三阶价格歧视**，利用空间异质性分割市场：  
    - 近端农民：支付高基价（扣除运输成本后仍高于边际成本）；  
    - 远端农民：通过运费补贴降低实际净价门槛，但基价已包含对运输成本的补偿。  
  - 利润翻倍 **直接支持“结构参数决定资本估值上限”**：当企业能内化市场边界约束（此处为配送成本）， monopolist 的租金提取能力显著增强（对比子问题 (b) 中空间摩擦导致的产出缺口）。  

---

#### **(b) 双头垄断竞争的逻辑衔接（Calculus 27.11）**  
- **竞争模型与空间均衡**：  
  - Ben 和 Huey 的竞争结构 **延续上文空间分散需求框架**，但引入 **双头垄断**（duopoly）替代单一垄断者，市场边界由两者的基价 $ p_B, p_H $ 和距离 $ x $ 共同决定。  
  - 无差异点 $ x^* $ 的方程 $ p_B + x = p_H + (40 - x) $ 直接对应 **霍特林模型（Hotelling Model）** 的均衡条件，表明：  
    - 消费者在临界距离 $ x^* $ 处对两者的净成本无差异；  
    - 企业通过调整基价争夺市场半径，最终形成 **纳什均衡价格**。  

- **对资本估值的动态影响**：  
  - 与上文 [27.10(c)] 逻辑一致，**外生竞争（Huey 的进入）压缩了 Ben 的垄断租金**：  
    - 无竞争时，Ben 可通过免费配送实现 \$10,000 利润；  
    - 双头竞争下，两企业将通过价格战（如降低基价）收缩有效市场半径，导致 **产业利润率向竞争性部门收敛**。  
  - 验证 [上文知识点] 中“**边缘竞争者侵蚀垄断势力**”的论断：铁路机会成本的内生性（运输成本 \$1/英里）将制约企业定价权，最终均衡价格接近边际成本 + 运输成本调整项。  

> 注：当前图片通过 **利润量化（\$10,000）** 和 **竞争模型引出**，强化了“市场结构动态性”对资本估值的核心作用。与上文 27.9/27.10 一脉相承，但将分析单元从单一垄断者扩展至空间竞争框架，揭示 **外生冲击（铁路）对定价策略的根本性重构**。

---
### Page/Slide 14



### 1. 文字与公式提取  
- **文本内容**：  
  334 OLIGOPOLY (Ch. 27)  
  Ben’s market extends. \( p_B + x^* = p_H + (40 - x^*) \). If Ben’s base price is \( p_B \) and Huey’s is \( p_H \), then Ben will sell \( 20 + (p_H - p_B)/2 \) cookstoves and Huey will sell \( 20 + (p_B - p_H)/2 \) cookstoves.  
  (b) Recalling that Ben makes a profit of \( p_B - 20 \) on every cookstove that he sells, Ben’s profits can be expressed as the following function of \( p_B \) and \( p_H \). \( (20 + (p_H - p_B)/2)(p_B - 20) \).  
  (c) If Ben thinks that Huey’s price will stay at \( p_H \), no matter what price Ben chooses, what choice of \( p_B \) will maximize Ben’s profits? \( p_B = 30 + p_H/2 \). (Hint: Set the derivative of Ben’s profits with respect to his price equal to zero.) Suppose that Huey thinks that Ben’s price will stay at \( p_B \), no matter what price Huey chooses, what choice of \( p_H \) will maximize Huey’s profits? \( p_H = 30 + p_B/2 \). (Hint: Use the symmetry of the problem and the answer to the last question.)  
  (d) Can you find a base price for Ben and a base price for Huey such that each is a profit-maximizing choice given what the other guy is doing? (Hint: Find prices \( p_B \) and \( p_H \) that simultaneously solve the last two equations.) \( p_B = p_H = 60 \). How many cookstoves does Ben sell to farmers living west of him? 20. How much profit does he make on these sales? $800.  
  (e) Suppose that Ben and Huey decided to compete for the customers who live between them by price discriminating. Suppose that Ben offers to deliver a stove to a farmer who lives x miles west of him for a price equal to the maximum of Ben’s total cost of delivering a stove to that farmer and Huey’s total cost of delivering to the same farmer less 1 penny. Suppose that Huey offers to deliver a stove to a farmer who lives x miles west of Ben for a price equal to the maximum of Huey’s own total cost of delivering to this farmer and Ben’s total cost of delivering to him less a penny. For example, if a farmer lives 10 miles west of Ben, Ben’s total cost of delivering to him is $30, $20 to get the stove and $10 for hauling it 10 miles west. Huey’s total cost of delivering it to him is $50, $20 to get the stove and $30 to haul it 30 miles east. Ben will charge the maximum of his own cost, which is $30, and Huey’s cost less a penny, which is $49.99. The maximum of these two numbers is $49.99. Huey will charge the maximum of his own total cost of delivering to this farmer, which is $50, and Ben’s cost less a penny, which is $29.99. Therefore Huey will charge $50.00 to deliver to this farmer. This farmer will buy from Ben.  

- **关键公式**：  
  - 市场边界决定：\( p_B + x^* = p_H + (40 - x^*) \)  
  - 销售量：  
    - Ben: \( 20 + \frac{p_H - p_B}{2} \)  
    - Huey: \( 20 + \frac{p_B - p_H}{2} \)  
  - Ben 利润函数：\( \left(20 + \frac{p_H - p_B}{2}\right)(p_B - 20) \)  
  - 反应函数：  
    - \( p_B = 30 + \frac{p_H}{2} \)  
    - \( p_H = 30 + \frac{p_B}{2} \)  
  - 纳什均衡：\( p_B = p_H = 60 \)  
  - 利润计算示例（x=10 英里）：  
    - Ben 收费 = \( \max(30, 49.99) = 49.99 \)  
    - Huey 收费 = \( \max(50, 29.99) = 50.00 \)  

---

### 2. 经济学解析  

#### **(a) 双头垄断均衡与利润侵蚀的机制**  
- **纳什均衡的形成逻辑**：  
  - 市场边界方程 \( p_B + x^* = p_H + (40 - x^*) \) 源于空间异质性框架（延续上文 27.10），界定临界距离 \( x^* \) 处消费者的成本无差异点。  
  - 企业通过调整基价争夺市场半径，形成 **反应函数**（\( p_B = 30 + p_H/2 \), \( p_H = 30 + p_B/2 \)），直接体现 **霍特林模型中的价格竞争**：  
    - 边际成本 \( c = 20 \)（隐含于利润公式 \( p_B - 20 \)）与运输成本（\$1/英里）共同内生化定价权。  
    - 对称均衡 \( p_B = p_H = 60 \) 导致 **有效市场半径收缩**：Ben 仅售 20 台（vs. 单垄断 200 台），利润 \$800（vs. 单垄断 \$10,000）。  
  - **利润跃缩的结构性原因**：  
    - 竞争通过 **价格弹性的空间扭曲** 消解垄断租金：单垄断时企业内化运输成本实现空间价格歧视（如上文免费配送策略），而双头竞争下企业被迫降低基价至 \( p^* = 60 \)（仅比边际成本高 40），导致单位利润 \( p_B - 20 = 40 \) 较单垄断时 \$100（上文 \$120 基价隐含）减少 60%。  
    - 销量从 200 台降至 20 台，验证了上文“**边缘竞争者侵蚀垄断势力**”推论——Huey 的进入将 Ben 的租金捕获能力压缩至原水平的 8%（\$800/\$10,000），直接削弱产业吸引力。  

- **上文理论的实证强化**：  
  - 均衡价格 \( p^* = 60 \) 高于纯竞争均衡（\( p = c + \text{平均运输成本} \approx 20 \)），但远低于单垄断最优价（\$120），印证上文“结构参数决定资本估值上限”的动态性：  
    - 外生竞争（Huey 存在）使市场边界约束从单边垄断（0-100 英里）转变为双边分割（0-20 英里），运输成本从租金提取工具转为 **竞争性损耗项**。  
    - 利润 \$800 量化了“**寡头竞争降低产业吸引力**”——产业总利润现为 \$1,600（Ben+Huey），较单垄断 \$10,000 下降 84%。  

#### **(b) 价格歧视竞争对市场结构的再重构**  
- **激烈竞争的微观逻辑**：  
  - 部分 (e) 的价格歧视策略（如向近端农民提供“成本价减 1 美分”）将竞争从价格层面升级为 **边际客户掠夺**：  
    - 当农民居于 x=10 英里时，Ben 以 \$49.99（接近 Huey 的边际成本 \$50）截断需求，Huey 以 \$50 被动退出。  
    - 此机制本质是 **Bertrand 竞争的空间变体**，利用对手成本信息压缩利润空间，导致 **均衡价格趋近对手边际成本**（如 Ben 收费 ≈ Huey’s cost）。  
  - **对产业动态的核心影响**：  
    - 此类竞争消除价格粘性，使生产企业利润进一步逼近 **零经济利润**（当前均衡 \$800 偏高因假设固定成本忽略）。  
    - 与上文 27.10 形成鲜明对比：单垄断时免费配送策略通过“隐性运费补贴”扩大需求边界；双头竞争下，企业被迫将运费显性化为竞争武器，**空间异质性从垄断工具转为竞争约束**，证实“市场结构动态性是资本估值的核心变量”。  

> 注：当前图片通过 **纳什均衡量化（\$60 均衡价，\$800 利润）** 和 **价格歧视机制**，系统性延伸上文分析——将 27.10 的单垄断空间模型扩展至动态竞争框架，揭示“铁路成本内生性”如何在寡头中重构定价权，最终趋近竞争性均衡。此过程直接支持上文“结构参数作为资本估值先决条件”的连续性结论。

---
### Page/Slide 15



# 霍特林模型中的空间价格歧视与均衡分析

## 1. 图片内容提取

### 文字与公式：
- **核心定价规则**：`59.99 - x`（Ben向西x英里农民的送货价格；Huey向东x英里农民的送货价格）
- **市场边界**：农民居住在Ben西20英里内从Ben购买，居住在Huey东20英里内从Huey购买
- **问题(f)关键数据**：  
  - 最便宜配送区域：*Those who live midway between them*（居中位置农民）  
  - **每家企业利润**：`$400`  
  - 均衡稳定性：`No`（无法通过调价增加利润）

### 图表元素：
- **坐标轴**：  
  - X轴：`Miles west of Ben`（Ben西侧距离，0-40英里）  
  - Y轴：`Dollars`（价格，20-80美元）  
- **三条关键曲线**：  
  - `Blue line`（Ben的送货成本曲线）  
  - `Red line`（Huey向Ben西侧交付的总成本曲线）  
  - `Pencil line`（消费者最低可获价格，取两线中较小值）  
- **利润区域**：  
  - `Ben's profit`（Ben的利润阴影区，X=0-20英里）  
  - `Huey's profit`（Huey的利润阴影区，X=20-40英里）  

---

## 2. 图表解析与上文连续性分析

### **(a) 完全价格歧视下的市场分割机制**
- **定价策略的本质**：  
  `59.99 - x` 价格公式是**完全空间价格歧视**的体现，直接修正了上文纳什均衡（$p_B=p_H=60$）的基价竞争模型——企业不再设定统一基价，而是根据消费者地理位置连续调整价格。  
  - *与上文连续性*：此策略升级了上文(e)部分"成本价减1美分"机制，将边缘竞争固化为全市场连续定价，使价格随距离直线下降（斜率=-1），体现运输成本（\$1/英里）完全内生化。

- **市场边界动态**：  
  图中`Pencil line`在X=20处形成V型最低点，印证了"在居中位置消费者获最优惠价格"。这是因：  
  - Ben在X<20区域价格更低（`59.99-x < 60-(40-x)`）  
  - Huey在X>20区域价格更低（`59.99-(40-x) < 60-x`）  
  - *与上文关联*：验证了上文"运输成本从垄断租金工具转为竞争损耗项"——此处企业主动将运输成本转嫁给定价，使价格梯度匹配运输成本，消解价格粘性。

### **(b) 均衡利润与竞争强度的图像化验证**
- **利润区域解读**：  
  - 两家企业各占20英里市场，利润区呈三角形，顶点在X=20处（利润为零的边界点）  
  - 面积量化显示**单位英里利润仅\$20**（总利润\$400/20英里），较上文基价竞争模型（单位利润\$40，见`p_B-20=40`）下降50%，体现**完全价格歧视加剧利润侵蚀**。

- **纳什均衡的几何证明**：  
  - `Pencil line`的V型结构表明：任何单边提价将使该企业损失边缘消费者；任何单边降价至V型线下方将导致负利润（因成本约束）。  
  - 与上文结论直接呼应："无法通过调价增加利润"（answer: *No*）证实此状态为**严格纳什均衡**，是Bertrand竞争空间变体的解。

### **(c) 对上文理论的实证延伸**
- **利润跃缩的新维度**：  
  - 此图中总利润\$800（\$400×2）较上文基价模型（\$800×2）再降50%，揭示：  
    > *完全价格歧视虽能扩大市场覆盖（如上文"有效市场半径收缩"的反向操作），但通过消除剩余攫取空间，将竞争强度推向极致，使利润向竞争性均衡（*p*→*c*）趋近。*  
  - *与上文连续性*：呼应"价格弹性空间扭曲"机制——此处V型最低价格（X=20处）比上文纳什均衡价\$60更低，验证了上文"竞争越激烈，价格越趋近边际成本"的推论。

- **结构参数的动态重构**：  
  图中蓝/红线斜率（-1）严格等于运输成本，表明**外生竞争结构（Huey存在）使运输成本从垄断定价工具转为竞争约束基准**。  
  - *与上文对应*：延续"空间异质性从垄断工具转为竞争约束"的核心结论，量化显示运输成本率如何内生决定价格曲线斜率。

---

## 3. 与上文理论的函数映射

| 上文核心概念          | 图中实证体现                          | 经济意义                                                                 |
|-----------------------|---------------------------------------|--------------------------------------------------------------------------|
| 纳什均衡              | `Pencil line`V型结构 + 利润区顶点    | 价格曲线交点(X=20)为不可单边改进的均衡点                                |
| 利润侵蚀机制          | 三角形利润区 → \$400/企业             | 比基价模型再降50%，验证价格歧视对租金捕获能力的彻底消解                  |
| 边际竞争效应          | X=20边界点消费者获最低价             | "边缘消费者"成为竞争焦点，单位利润归零                                   |
| 运输成本内生化        | 价格曲线斜率= -1（匹配\$1/英里运输成本） | 企业被迫将外生运输成本嵌入定价，放弃垄断租金提取能力                     |

> 图像通过完全价格歧视的几何呈现，系统强化了上文"结构参数作为资本估值先决条件"的核心命题：当竞争者将价格调整粒度提升至空间连续级别（`59.99-x`），产业利润被压缩至基价模型的一半，直接证明"市场结构动态性"通过定价精度迭代持续削弱资本估值潜力。

---
### Page/Slide 16



# 当前图片解析

## 1. 文字与公式提取  
- **文字内容**：  
  `336 OLIGOPOLY (Ch. 27)`  
- **公式**：  
  无  

## 2. 图表分析  
当前图片仅包含章节标题页，**无任何图表、价格曲线或利润区域**。因此：  
- 无法验证上文所述的 `Pencil line` V型结构、市场边界动态（X=20处）或三角形利润区。  
- 无斜率（-1）、价格梯度或单位利润（\$20/英里）等参数可量化。  

## 3. 与上文知识的连续性  
- 该图片标识了微观经济学教材中寡头垄断部分的页码（336页，第27章），与上文讨论的空间竞争模型、运输成本内生化及利润侵蚀机制同属理论框架。  
- **隐含衔接点**：页码指向的章节必然包含上文所述的基价竞争模型，但本图片未提供新实证数据，故不修正或延伸上文结论（如V型最低点的纳什均衡证明、利润再降50%的量化验证）。  
- **知识连续性**：确认本图片为上文模型的文献来源页，逻辑上承续“空间竞争固化→价格梯度匹配运输成本”的核心路径，但无增量信息。
