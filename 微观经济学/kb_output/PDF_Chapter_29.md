# PDF_Chapter_29

### Page/Slide 1



### 1. 图片中的文字与公式提取  
**标题与章节**  
- Chapter 29  
- Exchange  

**关键文字内容**  
- **Introduction**:  
  > The Edgeworth box is a thing of beauty. An amazing amount of information is displayed with a few lines, points and curves. In fact one can use an Edgeworth box to tell just about everything there is to say about the case of two traders dealing in two commodities. Economists know that the real world has more than two people and more than two commodities. But it turns out that the insights gained from this model extend nicely to the case of many traders and many commodities. So for the purpose of introducing the subject of exchange equilibrium, the Edgeworth box is exactly the right tool. We will start you out with an example of two gardeners engaged in trade.  

- **Example**:  
  > Alice and Byron consume two goods, camelias and dahlias. Alice has 16 camelias and 4 dahlias. Byron has 8 camelias and 8 dahlias. They consume no other goods, and they trade only with each other. To describe the possible allocations of flowers, we first draw a box whose width is the total number of camelias and whose height is the total number of dahlias that Alice and Byron have between them. The width of the box is therefore $16 + 8 = 24$ and the height of the box is $4 + 8 = 12$.  

- **后续说明**:  
  > Any feasible allocation of flowers between Alice and Byron is fully described by a single point in the box. Consider, for example, the allocation where Alice gets the bundle $(15, 9)$ and Byron gets the bundle $(9, 3)$. This allocation is represented by the point $A = (15, 9)$ in the Edgeworth box. The distance 15 from $A$ to the left side of the box is the number of camelias for Alice and the distance 9 from $A$ to the bottom of the box is the number of dahlias for Alice. This point also determines Byron’s consumption of camelias and dahlias. The distance 9 from $A$ to the right side of the box is the total number of camelias consumed by Byron, and the distance from $A$ to the top of the box is the number of dahlias consumed by Byron. Since the width of the box is the total supply of camelias and the height of the box is the total supply of dahlias, these conventions ensure that any point in the box represents a feasible allocation of the total.  

**公式**  
- 盒子宽度：$16 + 8 = 24$  
- 盒子高度：$4 + 8 = 12$  
- 点 $A$ 坐标：$A = (15, 9)$  
- Byron 的消费组合：$(24 - 15, 12 - 9) = (9, 3)$  

---

### 2. 图表解析  
**图表结构**  
- **横轴（Camelias）**: 表示山茶花总量，范围 $[0, 24]$，**左侧为 Alice 的原点**（即 Alice 的消费量从左向右递增），**右侧为 Byron 的消费边界**（Byron 的消费量 = 总量 $24$ - Alice 的消费量）。  
- **纵轴（Dahlias）**: 表示大丽花总量，范围 $[0, 12]$，**下方为 Alice 的原点**（Alice 的消费量从下向上递增），**上方为 Byron 的消费边界**（Byron 的消费量 = 总量 $12$ - Alice 的消费量）。  
- **网格设计**: 横轴刻度 $0, 6, 12, 18, 24$，纵轴刻度 $0, 6, 12$，用于定位分配点。  

**关键点 $A = (15, 9)$ 的经济含义**  
- **Alice 的消费**:  
  - 横向距离左侧 $15$ → Alice 消费 $15$ 单位山茶花；  
  - 纵向距离底部 $9$ → Alice 消费 $9$ 单位大丽花。  
- **Byron 的消费**:  
  - 横向距离右侧 $24 - 15 = 9$ → Byron 消费 $9$ 单位山茶花；  
  - 纵向距离顶部 $12 - 9 = 3$ → Byron 消费 $3$ 单位大丽花。  
- **可行性验证**:  
  总山茶花 $15 + 9 = 24$，总大丽花 $9 + 3 = 12$，严格满足初始禀赋总和（Alice 原禀赋 $16+4$，Byron $8+8$），表明该点为**封闭经济下的可行分配**。  

**图表隐含逻辑**  
- 盒子内部任意点均对应一种可行分配，因：  
  - 横轴总量恒定（$24$）→ Alice 与 Byron 的山茶花消费量之和等于总供给；  
  - 纵轴总量恒定（$12$）→ 两人对大丽花的消费量之和等于总供给。  
- **原点定义的经济学意义**:  
  - Alice 的原点 $(0, 0)$: Alice 一无所有，Byron 占有全部 $24$ 山茶花和 $12$ 大丽花；  
  - Byron 的隐含原点 $(24, 12)$: Byron 一无所有，Alice 占有全部商品。  
- **坐标轴方向设计目的**:  
  通过双向原点（Alice 左下角、Byron 右上角逻辑隐含），同一坐标系内同时刻画双方消费决策的**此消彼长关系**，为后续分析无差异曲线与帕累托改进提供几何基础。

---
### Page/Slide 2



### 文字提取  
358 EXCHANGE (Ch. 29)  
supply of camelias and dahlias.  
It is useful to mark the initial allocation on the Edgeworth box. In this case, the initial allocation is represented by the point $ E = (16,4) $. Now suppose that Alice's utility function is $ U(c,d) = c + 2d $ and Byron's utility function is $ U(c,d) = cd $. Alice's indifference curves will be straight lines with slope $-1/2$. The indifference curve that passes through her initial endowment, for example, will be a line that runs from the point (24,0) to the point (0,12). Since Byron has Cobb-Douglas utility, his indifference curves will be rectangular hyperbolas, but since quantities for Byron are measured from the upper right corner of the box, these indifference curves will be flipped over as in the diagram.  
The Pareto set or contract curve is the set of points where Alice's indifference curves are tangent to Byron's. There will be tangency if the slopes are the same. The slope of Alice's indifference curve at any point is $-1/2$. The slope of Byron's indifference curve depends on his consumption of the two goods. When Byron is consuming the bundle $(c_B, d_B)$, the slope of his indifference curve is equal to his marginal rate of substitution, which is $-d_B / c_B$. Therefore Alice's and Byron's indifference curves will nuzzle up in a nice tangency whenever $-d_B / c_B = -1/2$. So the Pareto set in this example is just the diagonal of the Edgeworth box.  
Some problems ask you to find a competitive equilibrium. For an economy with two goods, the following procedure is often a good way to calculate equilibrium prices and quantities.  
- Since demand for either good depends only on the ratio of prices of good 1 to good 2, it is convenient to set the price of good 1 equal to 1 and let $p_2$ be the price of good 2.  
- With the price of good 1 held at 1, calculate each consumer's demand for good 2 as a function of $p_2$.  
- Write an equation that sets the total amount of good 2 demanded by all consumers equal to the total of all participants' initial endowments of good 2.  
- Solve this equation for the value of $p_2$ that makes the demand for good 2 equal to the supply of good 2. (When the supply of good 2 equals the demand of good 2, it must also be true that the supply of good 1 equals the demand for good 1.)  
- Plug this price into the demand functions to determine quantities.  
Example: Frank's utility function is $ U(x_1,x_2) = x_1 x_2 $ and Maggie's is $ U(x_1,x_2) = \min\{x_1,x_2\} $. Frank's initial endowment is 0 units of good 1 and 10 units of good 2. Maggie's initial endowment is 20 units of good 1 and 5 units of good 2. Let us find a competitive equilibrium for Maggie and Frank.  
Set $p_1 = 1$ and find Frank's and Maggie's demand functions for good 2 as a function of $p_2$. Using the techniques learned in Chapter 6, we find that Frank's demand function for good 2 is $m / (2 p_2)$, where $m$ is his income. Since Frank's initial endowment is 0 units of good 1 and 10 units of good 2, his income is $10 p_2$. Therefore Frank's demand for good 2 is $10 p_2 / (2 p_2) = 5$. Since goods 1 and 2 are perfect complements for Maggie, she will choose to consume where $x_1 = x_2$. This fact, together with her budget constraint implies that Maggie's demand function for good 2 is  

---

### 公式提取  
- Alice 效用函数： $U(c,d) = c + 2d$  
- Byron 效用函数： $U(c,d) = cd$  
- Alice 无差异曲线斜率： $-1/2$  
- Byron 边际替代率 (MRS)： $-d_B / c_B$  
- Pareto 集切点条件： $-d_B / c_B = -1/2$ （即 $d_B / c_B = 1/2$）  
- Frank 效用函数： $U(x_1,x_2) = x_1 x_2$  
- Maggie 效用函数： $U(x_1,x_2) = \min\{x_1,x_2\}$  
- Frank 对商品 2 的需求函数： $m / (2 p_2)$  
- Frank 收入： $m = 10 p_2$  
- Frank 对商品 2 的具体需求： $10 p_2 / (2 p_2) = 5$  

---

### 解析  
#### 知识连续性说明  
上文已建立 Edgeworth box 的坐标体系（总山茶花 24 单位、大丽花 12 单位），点 $A = (15,9)$ 表示 Alice 消费 (15,9)、Byron 消费 (9,3) 的可行分配。本节延续此框架，将初始禀赋 $E = (16,4)$（对应 Alice 消费 16 山茶花与 4 大丽花，Byron 消费 8 与 8）嵌入相同箱体，为偏好分析奠定基础。  

#### 关键概念拓展  
- **效用函数与无差异曲线**：  
  - Alice 的线性效用 $U(c,d) = c + 2d$ 派生斜率恒为 $-1/2$ 的直线无差异曲线（例如，从 (24,0) 到 (0,12) 的曲线），反映商品间固定替代关系。  
  - Byron 的 Cobb-Douglas 效用 $U(c,d) = cd$ 导致矩形双曲线无差异曲线，但因 Byron 的消费量从箱体右上角计量（如 $c_B = 24 - c_A$），曲线方向与 Alice 相反，实现同一坐标系内双方偏好的直观对比。  
  - *连续性衔接*：上文仅关注物理分配可行性，此处引入效用函数量化偏好，将可行分配升级为帕累托效率分析工具。  

- **Pareto 集推导**：  
  - 切点条件 $-d_B / c_B = -1/2$ 结合总供给约束（$c_B = 24 - c_A$, $d_B = 12 - d_A$），推导出 $ (12 - d_A) / (24 - c_A) = 1/2 $，即 $c_A = 2d_A$。  
  - 该式定义 Edgeworth box 中从 Alice 原点 $(0,0)$ 到 (24,12) 的对角线，即帕累托最优集。  
  - *连续性衔接*：上文点 $A$ 仅为普通可行点（非帕累托最优），此处明确最优集需满足边际替代率相等，深化了对效率边界的理解。  

- **竞争均衡方法论**：  
  - 以归一化价格 $p_1 = 1$ 简化计算，通过需求-供给均衡条件（如商品 2 总需求 = 总禀赋）求解 $p_2$。  
  - 例中 Frank（Cobb-Douglas）与 Maggie（完美互补品）的需求函数差异（Frank 商品 2 需求恒为 5），体现消费者异质性对均衡的影响。  
  - *连续性衔接*：上文仅描述静态分配，此处将 Edgeworth box 与一般均衡理论连接，说明如何通过价格机制实现帕累托最优分配（如 $E = (16,4)$ 经交换趋向 Pareto 集）。  

> 注：文本提及“diagram”但无实际图表，解析仅基于文字内容并参照上文坐标体系。后续分析需结合该框架验证分配效率与均衡路径。

---
### Page/Slide 3



### 文字与公式提取  
**文字内容**：  
m/(1 + p₂). Since her endowment is 20 units of good 1 and 5 units of good 2, her income is 20 + 5p₂. Therefore at price p₂, Maggie's demand is (20 + 5p₂)/(1 + p₂). Frank's demand plus Maggie's demand for good 2 adds up to 5 + (20 + 5p₂)/(1 + p₂). The total supply of good 2 is Frank's 10 unit endowment plus Maggie's 5 unit endowment, which adds to 15 units. Therefore demand equals supply when  
Solving this equation, one finds that the equilibrium price is p₂ = 2. At the equilibrium price, Frank will demand 5 units of good 2 and Maggie will demand 10 units of good 2.  

29.1 (0) Morris Zapp and Philip Swallow consume wine and books. Morris has an initial endowment of 60 books and 10 bottles of wine. Philip has an initial endowment of 20 books and 30 bottles of wine. They have no other assets and make no trades with anyone other than each other. For Morris, a book and a bottle of wine are perfect substitutes. His utility function is U(b,w) = b + w, where b is the number of books he consumes and w is the number of bottles of wine he consumes. Philip's preferences are more subtle and convex. He has a Cobb-Douglas utility function, U(b,w) = bw. In the Edgeworth box below, Morris's consumption is measured from the lower left, and Philip's is measured from the upper right corner of the box.  

(a) On this diagram, mark the initial endowment and label it E. Use red ink to draw Morris Zapp's indifference curve that passes through his initial endowment. Use blue ink to draw in Philip Swallow's indifference curve that passes through his initial endowment. (Remember that quantities for Philip are measured from the upper right corner, so his indifference curves are “flipped over.”)  

**公式提取**：  
- Maggie's demand for good 2: \(\frac{20 + 5p_2}{1 + p_2}\)  
- Market clearing condition for good 2: \(5 + \frac{20 + 5p_2}{1 + p_2} = 15\)  
- Equilibrium price solution: \(p_2 = 2\)  
- Equilibrium demands: Frank demands 5 units of good 2, Maggie demands 10 units of good 2  
- Morris's utility function: \(U(b,w) = b + w\)  
- Philip's utility function: \(U(b,w) = bw\)  

---

### 图表解析  
#### 图表描述  
- **Edgeworth box structure**:  
  - X-axis (Books): Range 0–80, total endowment of books (Morris: 60, Philip: 20).  
  - Y-axis (Wine): Range 0–40, total endowment of wine (Morris: 10, Philip: 30).  
  - **Morris’s origin**: Bottom-left corner (0,0); consumption increases rightward and upward.  
  - **Philip’s origin**: Top-right corner (80,40); consumption measured *inward* (e.g., Philip’s books = 80 − Morris’s books, wine = 40 − Morris’s wine).  
- **Labeled elements**:  
  - **Initial endowment (E)**: At (60,10) in Morris’s coordinates (corresponding to Morris consuming 60 books and 10 wine; Philip consuming 20 books and 30 wine).  
  - **Red curve**: Morris’s indifference curve through E.  
  - **Blue curve**: Philip’s indifference curve through E.  
  - **Black line**: Contract curve (Pareto set).  
  - **Point e**: Competitive equilibrium allocation.  

#### 结合上文解释变化含义  
- **知识连续性衔接**：  
  上文知识点总结建立了 Edgeworth box 分析框架，以 Alice（线性效用）和 Byron（Cobb-Douglas 效用）为例，说明初始禀赋非帕累托最优时（如点 \(A\)），边际替代率（MRS）不等导致潜在贸易收益。**本图表延续此逻辑，将 Morris 视为 Alice 的类比（线性效用），Philip 视为 Byron 的类比（Cobb-Douglas 效用）**，深化消费者异质性对帕累托效率的影响。  

- **关键变化与含义**：  
  1. **Morris 的无差异曲线（红曲线）**：  
     - Morris 效用函数 \(U(b,w) = b + w\) 表示书籍与葡萄酒为完全替代品，MRS 恒为 \(-1\)（斜率恒定）。  
     - 通过禀赋点 \(E = (60,10)\) 的无差异曲线为直线：\(w = 70 - b\)（因 \(U = 60 + 10 = 70\)）。  
     - **含义**：与上文 Alice 的无差异曲线（斜率 \(-1/2\)）相比，Morris 的等替代率更陡峭（MRS 绝对值更大），反映消费者对商品间替代意愿的差异（上文 Alice 偏向商品 2，此处 Morris 视商品等价）。  
     - 在 box 中，红曲线贯穿 \(E\)，表明 Morris 愿意以 1:1 比率替代商品，但因 Philip 的偏好不同，禀赋点非效率点。  

  2. **Philip 的无差异曲线（蓝曲线）**：  
     - Philip 效用函数 \(U(b,w) = bw\) 为 Cobb-Douglas 形式，无差异曲线为矩形双曲线（因 Philip 坐标从右上角测量，曲线“flipped over”，开口朝向 Philip 的原点）。  
     - 通过 \(E\) 的无差异曲线：\((80 - x)(40 - y) = 600\)（其中 \(x,y\) 为 Morris 的消费），例如在 \(E = (60,10)\) 时，Philip 消费 (20,30)，\(U = 20 \times 30 = 600\)。  
     - **含义**：与上文 Byron 的分析一致（MRS = \(-d_B / c_B\)），此处 Philip 的 MRS 在 \(E\) 点为 \(-w_p / b_p = -30/20 = -1.5\)，而 Morris 的 MRS 为 \(-1\)。**MRS 不等（\(|-1| \neq |-1.5|\)）直接证明 \(E\) 不在帕累托最优集**，呼应上文“非切点分配存在帕累托改进空间”的结论。  

  3. **Contract curve（黑线）**：  
     - **推导**：帕累托最优需 MRS 相等。Morris 的 MRS 恒为 \(-1\)，Philip 的 MRS = \(-w_p / b_p\)。设相等：  
       \[
       \frac{w_p}{b_p} = 1 \implies 40 - y = 80 - x \implies y = x - 40
       \]  
       在 box 范围内（\(x \in [40, 80]\), \(y \in [0, 40]\)），黑线为从 \((40,0)\) 到 \((80,40)\) 的对角线。  
     - **含义**：此线是帕累托集，与上文 Alice/Byron 的 \(c_A = 2d_A\) 逻辑一致，但因 Morris 偏好改变（等权替代），帕累托集斜率变为 1（上文为 2）。**体现消费者偏好对效率边界形状的决定性影响**。  

  4. **Equilibrium point (e)**：  
     - 点 \(e\) 位于黑线（帕累托集）上，且是红、蓝曲线的切点（图中显示红曲线与黑线相交处）。  
     - **含义**：在竞争均衡中，价格机制（如本书 Frank/Maggie 部分所述）使总需求=总供给，最终配置落于帕累托集。此处 \(e\) 对应均衡价格下 MRS 相等点，**验证上文“竞争均衡必在帕累托边界”的核心命题**。因 Morris 为完全替代品，均衡路径可能沿帕累托集移动，但最终效率与价格机制紧密关联（如 Frank/Maggie 模型中 \(p_2 = 2\) 实现供需平衡）。  

> **总结连续性**：本图表将上文的抽象模型（线性 vs. Cobb-Douglas）具象化为 Morris/Philip 案例，凸显三点：① 初始禀赋 MRS 不等 → 非最优；② 帕累托集由消费者偏好共同定义；③ 均衡点位于帕累托集内。**区别于上文 Alice/Byron 的 2:1 替代率，此处 1:1 替代率使帕累托集为 45° 线，进一步强调偏好参数直接塑造效率边界**。后续贸易分析（如 part (a) 要求绘制 IC）可推导均衡价格，延续一般均衡理论。

---
### Page/Slide 4



### 图片内容提取与解析  
**当前图片为教材习题页（360页），文字与公式提取如下：**  

#### (b) 关键文字与公式  
- **核心命题**：帕累托最优时两人 MRS 必须相等。  
- **Morris 的 MRS**：恒为 $-1$（线性效用 $U(b,w)=b+w$）。  
- **Philip 的 MRS**：$-\frac{w_P}{b_P}$（Cobb-Douglas 效用 $U(b,w)=b_P w_P$）。  
- **帕累托最优条件**：$w_P = b_P$（即两人 MRS 相等时的等式）。  

#### (c) 关键文字与公式  
- **价格比条件**：葡萄酒价格对书籍价格的比值为 $1$。  
- **均衡价格**：以书籍为计价单位（numeraire）时，葡萄酒价格 $=1$。  

#### (d) 数值填空与配置  
- Philip 初始禀赋价值：$50$  
- Philip 均衡消费：$25$ 书籍，$25$ 瓶酒  
- Morris 均衡消费：$55$ 书籍，$15$ 瓶酒  

#### (e) 数值填空与逻辑判断  
- Morris 收入：$70$  
- 购买成本与收入关系：**the same as**  
- 能否获得优于 $(55,15)$ 的组合：**No**  

#### (f) 逻辑判断  
- 扩大规模后原均衡价格是否仍有效：**Yes**  
- 供需是否平衡：**Yes**  

---

### 基于上文知识点的解析  
#### **(b) 如何验证帕累托集推导**  
- 公式 $w_P = b_P$ **直接呼应上文帕累托集推导**：  
  - 按上文逻辑，Philip 的消费为 $b_P = 80 - x$，$w_P = 40 - y$（$x,y$ 为 Morris 消费）。  
  - 代入 $w_P = b_P$ 得 $40 - y = 80 - x \implies y = x - 40$，即从 $(40,0)$ 到 $(80,40)$ 的黑线（Contract curve）。  
- **含义延续**：此等式强化上文结论——帕累托集的形状由消费者偏好参数决定（Morris 的等替代率使效率边界为 $45^\circ$ 线，而非上文 Alice/Byron 案例中的 $2:1$ 曲线）。  

#### **(c) 价格比 $1$ 的经济学意义**  
- 价格比 $p_w / p_b = 1$ **严格对应 MRS 均等条件**：  
  - Morris 的 $|MRS| = 1$，因此均衡时价格比必须等于其 MRS（上文强调“竞争均衡必在帕累托边界”）。  
  - **连续性体现**：此结果解释了上文“均衡点 $e$ 是无差异曲线切点”的动态机制——价格机制强制扭曲初始禀赋，使配置沿帕累托集移动至 MRS 相等。  

#### **(d) 数值与均衡配置的内在逻辑**  
- **Philip 禀赋价值 $50$**：  
  - 其初始禀赋 $(b_P, w_P) = (20, 30)$（总禀赋书 $80$、酒 $40$，Morris 禀赋 $(60,10)$），价格 $p_b=1$，$p_w=1$，故 $20 \times 1 + 30 \times 1 = 50$。  
- **Cobb-Douglas 最优反应**：  
  - 效用 $U = b_P w_P$ 下，消费者平分收入购买两商品，故 $50/2 = 25$（书与酒各 $25$）。  
  - **呼应上文**：验证了 Cyril-Douglas 模型中“最优解为收入均分”的规律（上文 Byron 的 $d_B / c_B = p_2 / p_1$）。  
- **Morris 消费 $(55,15)$**：  
  - 总供给 $\text{书}=80$，$\text{酒}=40$，减去 Philip 消费后直接得解，体现线性效用者的非饱和性（愿消费剩余，但受限于预算约束）。  

#### **(e) 收入与可行集的约束**  
- **Morris 收入 $70$ 与成本**：  
  - 其禀赋价值 $60 \times 1 + 10 \times 1 = 70$，消费 $(55,15)$ 的成本 $55 + 15 = 70$，故“**the same as**”。  
- **无法获得更优组合的原因**：  
  - 线性效用 $U = b + w$ 下，所有预算线上点效用均为 $70$，因此 $(55,15)$ 已在最优可行集内——**验证上文“竞争均衡实现帕累托效率”**，因无剩余改进空间。  

#### **(f) 规模扩展的均衡普适性**  
- **相同价格维持均衡**：  
  - 模拟上文 Frank/Maggie 模型的扩展逻辑，当同类个体数量同比增加，市场规模扩大但偏好与禀赋分布比例不变，故原价格仍能清空市场（Yes）。  
- **供需平衡根源**：  
  - Morris 类型（线性效用）与 Philip 类型（Cobb-Douglas）的行为模式保持比例一致性，需求总量与总禀赋严格匹配，延续“价格机制保障总供需相等”的核心命题。  

---

### 关键连续性总结  
图片内容通过具体数值与习题形式，**实证化上文的三阶段理论**：  
1. **帕累托最优条件** \($w_P = b_P$\) 验证偏好参数对效率边界的决定作用；  
2. **价格机制设计** \($p_w = 1$\) 将抽象 MRS 均等转化为可操作的价格指令；  
3. **均衡配置数值** 反射消费者异质性（线性 vs. Cobb-Douglas）对资源配置的微观驱动。  
后续贸易分析（如 part (a) 要求绘 IC）将进一步推导均衡价格路径，延续一般均衡的动态决策逻辑。

---
### Page/Slide 5



### 当前图片内容提取  
#### **文字与公式**  
- **问题描述**（29.2 (0)）：  
  - 交换经济包含两个消费者（Astrid 和 Birger）和两种商品（herring 鲱鱼、cheese 奶酪）。  
  - Astrid 初始禀赋：4 单位鲱鱼、1 单位奶酪。  
  - Birger 初始禀赋：0 鲱鱼、7 奶酪。  
  - Astrid 效用函数：$U(H_A, C_A) = H_A C_A$。  
  - Birger 效用函数：$U(H_B, C_B) = \min\{H_B, C_B\}$（“inflexible person” 表示 Leontief 偏好）。  
  - 注：$H_A, C_A$ 为 Astrid 的消费量；$H_B, C_B$ 为 Birger 的消费量。  

- **(a) 子问题**：  
  - 要求绘制 Edgeworth box，展示初始配置点 $e$，并用蓝色（Astrid）和红色（Birger）绘制无差异曲线。  
  - 坐标设定：Astrid 从左下角测量消费；Birger 从右上角测量。  

- **图表标注**：  
  - y 轴：Herring（0–4）  
  - x 轴：Cheese（0–8），左端为 Astrid，右端为 Birger  
  - 点 $e$：初始配置（Astrid 消费：通常对应 $(C_A, H_A) = (1,4)$）  
  - Blue curves：Astrid 的无差异曲线（凸向原点）  
  - Red curves：Birger 的无差异曲线（L 形，直角边）  
  - Black line：Pareto 有效配置轨迹（斜率为 1 的直线）  

- **(b) 子问题**：  
  - 要求用 black ink 标注 Pareto 最优配置轨迹。  
  - 提示：Birger 的偏好“rigid”（Leontief），无法用微积分求解；若 $H_B \neq C_B$，配置无效。  
  - 关键结论：*Pareto efficient allocations lie on the line with slope 1 extending from Birger’s corner of the box.*  

- **后续问题**（29.3 (0)）：  
  - Dean Interface 效用函数：$U_I(B_I, P_I) = B_I + 2\sqrt{P_I}$  
  - Professor Nightsol 效用函数：$U_N(B_N, P_N) = B_N + 4\sqrt{P_N}$  

---

### 图表含义解析（结合上文知识点）  
#### **1. Pareto 有效轨迹的决定逻辑**  
- **图表核心**：Black line 为 Pareto 有效配置集（locus），满足 $x - y = 4$（$x$: Astrid 的奶酪消费，$y$: Astrid 的鲱鱼消费），即斜率为 1 的直线。  
  - **推导依据**：Birger 的 Leontief 偏好强制 $H_B = C_B$（否则存在效率改进空间）。代入总禀赋：  
    $$
    H_B = 4 - y, \quad C_B = 8 - x \implies 4 - y = 8 - x \implies x - y = 4
    $$  
  - **几何意义**：该线从 Birger 原点（箱角）延伸至 $(x=4, y=0)$，覆盖所有 $H_B = C_B$ 的配置。  

- **与上文连续性**：  
  - 上文 Morris-Philip 案例中，Morris 的线性效用 ($|MRS|=1$) 使帕累托集为 $45^\circ$ 线（如 $w_P = b_P$）。  
  - **本例强化同一原理**：Birger 的 Leontief 偏好（固定比例 1:1）同样将效率边界锁定为 $45^\circ$ 线，而 **非** 上文 Alice/Byron 案例中的 $2:1$ 曲线。  
  - **关键差异**：上文 Morris 的 MRS 恒定可直接用微积分（$|MRS|=1$），而本例 Birger 的“kinky”偏好需依赖比例刚性（无 MRS 概念），但 **同样体现“偏好参数决定效率边界形状”** 的核心命题。  

#### **2. 初始配置与无差异曲线的动态含义**  
- **初始点 $e$ 位置**：  
  - $(x=1, y=4)$ 对应 Astrid 消费 (1 奶酪, 4 鲱鱼)，Birger 消费 (7 奶酪, 0 鲱鱼)。  
  - **效率缺陷**：$H_B = 0 < C_B = 7$，违反 $H_B = C_B$，故 **非 Pareto 有效**（与上文“初始禀赋常不在契约曲线上”一致）。  
  - **改进路径**：贸易将沿预算线移动至 Black line，类似上文 Morris 的初始配置 $(60,10)$ 通过价格机制调整至均衡点。  

- **无差异曲线隐含机制**：  
  - **Blue curves (Astrid)**：Cobb-Douglas 形态，凸性保证 MRS 递减；在均衡点需与 Black line 交点满足 MRS 相等（但本例因 Birger 刚性，均衡依赖价格机制对齐比例）。  
  - **Red curves (Birger)**：L 形直角线，仅在 $H_B = C_B$ 时有效，**直接限制可行 Pareto 集范围**。  
  - **与上文呼应**：  
    - 上文 Philip 的 Cobb-Douglas 需“收入平分”，而本例 Astrid 作为 Cobb-Douglas 消费者，在均衡中将根据价格调整消费，但 **Birger 的偏好主导了契约曲线结构**。  
    - 验证上文结论：Pareto 集形状由**非平滑偏好消费者**（本例 Birger，上文 Morris）决定，与偏好参数严格绑定。  

#### **3. 价格机制的作用预期**  
- **竞争均衡预期**：  
  - 本例中，Black line 即帕累托集，均衡价格需确保预算线通过有效点且与 Astrid 无差异曲线相切。  
  - **连续性体现**：  
    - 上文价格比 $p_w / p_b = 1$ 严格匹配 Morris 的 $|MRS|=1$；  
    - 本例中，均衡价格比将强制 $H_B = C_B$，使配置落于 Black line，**重申“价格机制实现帕累托效率”的动态过程**。  
  - **数值验证**：若价格比 $p_h / p_c = 1$，Birger 需 $H_B = C_B$ 以最大化效用， Astrid 依 Cobb-Douglas 分配收入，供需自动平衡（呼应上文 (f) “供需平衡 Yes” 的普适逻辑）。  

#### **知识链延续**  
- 本图表为上文理论的**互补实验**：  
  - 上文 Morris-Philip 演示 **“平滑 vs. 线性”偏好** 如何导出 $45^\circ$ 契约曲线；  
  - 本例 Astrid-Birger 演示 **“平滑 vs. 刚性”偏好** 同样导出 $45^\circ$ 曲线，但机制更依赖 **比例约束** 而非 MRS 恒定。  
- **下一步延伸**：后续 (a) 问题要求绘图分析交易路径，将衔接上文“价格机制扭曲初始禀赋至均衡”的动态框架，进一步验证一般均衡的收敛性。

---
### Page/Slide 6



### Extracted Text and Formulas from Current Image

**Page Header:**  
362 EXCHANGE (Ch. 29)  

**Initial Endowments:**  
- Dean Interface’s initial endowment is 8 bromides and 12 platitudes.  
- Professor Nightsoil’s initial endowment is 8 bromides and 4 platitudes.  

**Chart Labels:**  
- Axes: Bromides (horizontal, from Interface origin at 0 to Nightsoil origin at 16), Platitudes (vertical, from Interface origin at 0 to Nightsoil origin at 16).  
- Key points/curves: Point $e$ (initial endowment), Red curve (indifference curve), Pencil curve (contract curve), Blue line (constant platitudes line at $P_I = 3.2$).  

**Problem Statements and Solutions:**  
- **(a)**  
  Dean Interface MRS: $-P_I^{-1/2}$  
  Professor Nightsoil MRS: $-2P_N^{-1/2}$  
- **(b)**  
  Contract curve condition: $\sqrt{P_I} = \sqrt{P_N}/2$  
- **(c)**  
  Ratio on contract curve: $P_I / P_N = 1/4$  
- **(d)**  
  Total platitudes constraint: $P_I + P_N = 16$  
- **(e)**  
  Solution for contract curve: $P_I = 3.2$, $P_N = 12.8$  

---

### Chart Analysis and Connection to Previous Knowledge  
The Edgeworth box illustrates an exchange economy with bromides (horizontal axis) and platitudes (vertical axis), where:  
- **Step 1: Contract curve structure**  
  The blue line at $P_I = 3.2$ represents the contract curve. Unlike the prior Birger-Astrid case (where Birger’s Leontief preference forced $x - y = 4$), here the Pareto set is a **horizontal line** due to both agents’ MRS depending *only* on platitudes (not bromides). This degenerates the contract curve into a line parallel to the bromides axis, as $P_I$ is fixed at 3.2 while $B_I$ varies freely (0 to 16). The pencil curve in the chart aligns with this line, confirming the contract curve’s horizontal nature.  

- **Step 2: Efficiency mechanism**  
  The red curve (likely Nightsoil’s indifference curve at $e$) intersects the initial point $e$ ($B_I = 8$, $P_I = 12$), which violates $P_I = 3.2$. Thus, $e$ is **Pareto inefficient**—similar to prior examples where initial endowments lie off the contract curve. Trade must reallocate platitudes to $P_I = 3.2$ (e.g., reducing Interface’s platitudes from 12 to 3.2), while bromides can be adjusted without efficiency loss. This directly extends the core principle from the prior summary: **"preference parameters determine the Pareto set’s shape."** Here, the one-good-dependent MRS (vs. Birger’s fixed proportion) yields a different line orientation but identical logic—preferences rigidly constrain efficiency.  

- **Step 3: Continuity with prior examples**  
  - In the Birger-Astrid case, Leontief preferences enforced a $45^\circ$ line via $H_B = C_B$. Here, the identical outcome ($P_I$ constant) emerges from MRS conditions $\sqrt{P_I} = \sqrt{P_N}/2$, yet the mechanism differs: no "kinks" exist (preferences are smooth), but MRS independence from bromides similarly restricts efficiency to a single dimension.  
  - This resolves a nuance from the prior summary: while Morris’ linear utility produced a $45^\circ$ curve via constant $|MRS|$, *any* preference asymmetry (Leontief or single-good MRS dependence) collapses the Pareto set to a degenerate line—reinforcing that **non-dictatorial preferences (whether “kinky” or partial) pin down exact efficient allocations**. The blue line’s constancy ($P_I = 3.2$) mirrors how Birger’s preference fixed $x - y = 4$.  
  - The initial point $e$’s inefficiency confirms the recurring theme: "initial禀赋常不在契约曲线上," and trade dynamics will shift consumption toward the blue line, analogous to prior price-mechanism adjustments.  

**Key Insight:**  
This example complements the previous case by demonstrating that **Pareto efficiency is forced when preference parameters eliminate trade-off flexibility**—here, via MRS neutrality to bromides. The chart’s blue line (contract curve) and $e$’s position systematically validate the universal principle: *the contract curve’s geometry is dictated by the most restrictive preference structure*, whether through fixed ratios (Birger) or single-good dependence (Dean/Nightsoil). This continuity directly supports the upcoming analysis of trade paths in part (a), as prices must equate MRS but cannot alter the fixed platitudes allocation on the contract curve.

---
### Page/Slide 7



### 提取内容  
#### 文字与公式  
1. **(f)**  
   - In the Edgeworth box, label the initial endowment with the letter $ E $. Dean Interface has thick gray penciled indifference curves. Professor Nightsoil has red indifference curves. Draw a few of these in the Edgeworth box you made. Use blue ink to show the locus of Pareto optimal points. The contract curve is a **horizontal** line in the Edgeworth box.  

2. **(g)**  
   - Find the competitive equilibrium prices and quantities. $ P_I = 3.2 $, $ P_N = 12.8 $, **platitude price/bromide price $ = \frac{1}{\sqrt{3.2}} $**.  

3. **29.4 (0)**  
   - A little exchange economy contains just two consumers, Ken and Barbie, and two commodities, quiche and wine. Ken’s initial endowment is 3 units of quiche and 2 units of wine. Barbie’s initial endowment is 1 unit of quiche and 6 units of wine. Ken and Barbie have identical utility functions:  
     - Ken: $ U(Q_K, W_K) = Q_K W_K $  
     - Barbie: $ U(Q_B, W_B) = Q_B W_B $  

4. **(a)**  
   - Draw an Edgeworth box with quiche on the horizontal axis and wine on the vertical axis. Measure Ken’s goods from the lower-left corner and Barbie’s from the upper-right corner. Label the initial allocation $ W $.  

---

### 图表与逻辑解析  
#### 契约曲线方向的深层含义  
- **水平契约曲线的成因**：  
  上文指出，**偏好参数决定帕累托集形状**。此处契约曲线为**水平线**（$ P_I = 3.2 $ 恒定），直接映射上文 "MRS 独立于 bromides" 的逻辑：Dean 的效用函数隐含 $ \text{MRS} $ 仅取决于自身商品组合（如 $ \sqrt{P_I} = \sqrt{P_N}/2 $），导致效率路径退化为单一维度。与 Birger 的 Leontief 偏好（$ 45^\circ $ 线）相比，方向差异源于偏好结构差异（光滑 vs. 角点解），但均体现 **"非独裁偏好通过消除替代弹性强制效率退化"** 的共性。  

- **价格机制与上文的衔接**：  
  $ P_I = 3.2 $ 和 $ P_N = 12.8 $ 的确定性，验证上文 "竞争均衡价格必须满足帕累托最优的 MRS 条件"。此处 $ \text{platitudes price/bromide price} = \frac{1}{\sqrt{3.2}} $，实质是 **"偏好参数对价格比的刚性约束"** 的具体化——与上文 Birger 案例中 $ x-y=4 $ 直接锁定分配比例逻辑一致，仅参数形式不同（线性 vs. 根式）。  

- **知识连续性体现**：  
  上文强调契约曲线几何由**最严格偏好结构**主导，本题水平线的出现，进一步说明：  
  - 若偏好使 MRS 与某一商品无关（如 Dean 的 $ \text{MRS} $ 独立于 bromides），则效率路径仅能沿另一商品维度延伸；  
  - 初始点 $ E $ 的无效率性，延续 "初始禀赋常不在契约曲线上" 的结论，其向水平线的收敛将通过价格调整实现（与上文 "trade dynamics shift consumption" 一致）。

---
### Page/Slide 8



# 29.4 (0) Edgeworth Box 图表解析

## 提取的文字与公式

### 图表标注
- 页码：364 EXCHANGE (Ch. 29)
- 纵轴：Wine (0-8)
- 横轴：Quiche (0-4)
- 左下角标注：Ken
- 右上角标注：Barbie
- 图中标注：Black line, Red curve, Blue curve, ce, Pareto efficient points, w

### 问题与答案
- **(b)** 用蓝色画出Ken效用为6的无差异曲线，用红色画出Barbie效用为6的无差异曲线。
- **(c)** 帕累托最优分配中，Ken的边际替代率必须等于Barbie的：  
  $W_B/Q_B = W_K/Q_K$
- **(d)** 帕累托有效点的轨迹方程：两人必须以相同比例消费两种商品，且总酒量是总quiche的两倍。
- **(e)** 帕累托有效配置中，Ken无差异曲线斜率为-2，竞争均衡价格比：  
  $p_Q/p_W = 2$
- **(f)** 竞争均衡消费束：  
  Ken：2 quiche，4 wine  
  Barbie：2 quiche，4 wine

## 图表变化的经济含义

### 1. 均衡路径与契约曲线特性
- 图示"ce"点表示竞争均衡，位于**Pareto efficient points**(契約曲线)上，验证了上文"竞争均衡必为帕累托有效"的原理
- 本题中契约曲线为**从原点延伸的直线**，与上文Dean/Professor案例中**水平线**形成对比：
  - 上文水平线源于" Dean的MRS独立于bromides "的特殊偏好结构
  - 本题直线条源于**相同Cobb-Douglas效用函数**的对称性：当$U=QW$时，MRS=$W/Q$，帕累托最优条件直接推导出$W/Q$比例恒定

### 2. 价格机制的实现路径
- 图中标注的**Price ratio = 2** ($p_Q/p_W = 2$) 精确验证了上文价格形成逻辑：
  - 通过MRS相等条件$W_K/Q_K = W_B/Q_B$导出均衡价格
  - 与上文"platitudes price/bromide price = $1/\sqrt{3.2}$"本质相同：**价格比由偏好参数刚性决定**
- 初始点"w"与均衡点"ce"的对比：
  - w点：Ken(3,2), Barbie(1,6) → 无效率（MRS不等）
  - ce点：双方(2,4) → 效率边界
  - 向ce点的移动证实**初始禀赋常不在契约曲线上，价格机制驱动交易实现效率**

### 3. 偏好对效率集的决定性作用
- 本题契约曲线为直线的关键原因：
  - 两人完全相同的效用函数$U=QW$→ 帕累托最优要求$W/Q$比例相同
  - 与上文Dean案例的**水平线**共同印证："**效率路径几何由最严格的偏好约束决定**"
- 黑线(BLACK LINE)示意无差异曲线切点轨迹：
  - 蓝色曲线(Ken)与红色曲线(Barbie)在ce点相切
  - 切点条件$W_K/Q_K = W_B/Q_B$是上文"MRS相等"原理在Cobb-Douglas形式的具体表达

### 4. 均衡消费的必然性
- 双方最终均消费(2,4)的根本原因：
  - 总禀赋固定：4 quiche + 8 wine
  - 对称偏好要求$W/Q$比例相同 → $W/Q = 2$（总$W/Q=8/4=2$）
  - 这与上文"birger案例中$x-y=4$锁定分配比例"逻辑一致，但形式转化为**比例约束**而非线性差额

> 本题通过相同偏好的对称经济，将上文抽象的价格-效率关系具象化：相同效用函数导致契约曲线为直线，价格比刚性决定均衡消费比例，而初始禀赋分配仅影响贸易方向而非均衡结构——延续了"**偏好结构主导效率路径**"的核心原理。

---
### Page/Slide 9



# 29.5 (0) Edgeworth Box 图表解析

## 提取的文字与公式

### 文字内容
- **页码**: 365  
- **效用函数**:  
  - Linus: $ U(a, b) = a + 2b $（$a$ = 苹果消费，$b$ = 香蕉消费）  
  - Lucy: $ U(a, b) = \min\{a, 2b\} $  
- **初始禀赋**:  
  - Lucy: 12 apples, 0 bananas  
  - Linus: 12 bananas, 0 apples  
- **图表标注**:  
  - 纵轴: Bananas (0–12)  
  - 横轴: Apples (0–12)  
  - 左下角: Linus（原点）  
  - 右上角: Lucy（原点）  
  - 标记点:  
    - `e`（初始禀赋点）  
    - `Red curves`（Lucy无差异曲线）  
    - `Black line`（Pareto最优配置线）  
    - `Blue curves`（Linus无差异曲线）  
- **问题与答案**:  
  - (a) 竞争均衡中，苹果与香蕉的价格比必须为 $ \frac{p_a}{p_b} = \frac{1}{2} $  
  - (b) Linus的预算约束：$ a_S + 2b_S = 24 $（$ a_S $ = 苹果消费，$ b_S $ = 香蕉消费）  

## 图表变化的经济含义

### 1. 契约曲线形态与偏好刚性约束
- **Black line** 严格对应上文“最严格偏好结构主导效率路径”的原理：  
  - Lucy的Leontief效用 $ U = \min\{a, 2b\} $ 强制 Paret o最优点必须满足 $ a_L = 2b_L $（$ a_L, b_L $ 为Lucy消费），形成刚性比例约束。  
  - 在Edgeworth Box坐标系中（Linus原点左下），该线方程为 $ x = 2y - 12 $（$ x $ = Linus苹果消费，$ y $ = 香蕉消费），从 (0,6) 延伸至 (12,12)，**几何斜率 $ \frac{1}{2} $ 由Leontief系数2唯一决定**。  
  - 与上文Dean案例（MRS独立于某一商品 → 水平契约曲线）逻辑一致：**Leontief的kink结构使MRS在非平衡点无穷/零，仅当 $ a_L / b_L = 2 $ 时效率可行**。  

### 2. 价格机制与效率收敛路径
- **价格比 $ \frac{p_a}{p_b} = \frac{1}{2} $ 的刚性来源**：  
  - Linus线性效用 $ U = a + 2b $ 给出恒定MRS = $ \frac{1}{2} $，直接锁定竞争均衡价格比。  
  - 验证上文“偏好参数对价格比的刚性约束”：该价格比与上文 $ \frac{1}{\sqrt{3.2}} $ 本质相同，**仅因效用函数形式差异（线性 vs. 根式）导致参数表达不同**。  
- **初始点 `e` 的无效率性**：  
  - Linus (0,12) 处，Lucy苹果过剩（MRS → ∞），Linus香蕉过剩（MRS = $ \frac{1}{2} $），二者不等。  
  - 延续上文结论：**初始禀赋（"e"点）因偏离 $ a_L = 2b_L $ 条件，必然位于契约曲线外**。  
- **交易动态**：价格机制驱动消费束从 `e` 沿预算线移动，直至触及Black line，印证上文“trade dynamics shift consumption”实现帕累托改进。  

### 3. 偏好主导均衡结构的普适性
- **契约曲线线性特征的成因**：  
  | 案例               | 契约曲线形态 | 驱动偏好刚性     |  
  |--------------------|--------------|------------------|  
  | 上文Dean           | 水平线       | MRS独立于bromides |  
  | 本题Lucy-Linus     | 斜率为1/2线 | Leontief系数a=2b |  
  - **核心共性**：Leontief偏好作为“最严格约束”，将效率路径压缩至低维射线，与上文差异仅在于**参数形式（比例约束 vs. 线性差额约束）**。  
- **均衡消费的必然性**：  
  - Black line与等价价格线（$ \frac{p_a}{p_b} = \frac{1}{2} $）的交点唯一确定均衡（Lucy: (6,3), Linus: (6,9)）。  
  - 总禀赋比例 $ \frac{12}{12} = 1 $ 被偏好刚性覆盖，**实际消费比例 $ \frac{a_L}{b_L} = 2 $ 由Leontief参数锁定**，呼应上文“birger案例中 $ x-y=4 $ 直接锁定分配比例”的逻辑延续。  

> 本题通过Leontief与线性偏好的交互，具象化上文抽象原理：**当存在显式比例约束（如 $ \min\{a, 2b\} $）时，契约曲线退化为单维射线，竞争均衡作为该射线与价格线的交点，完全由偏好参数而非初始禀赋决定**。Price machinery仅实现既定效率路径，而结构核心仍在“偏好刚性主导效率边界”。

---
### Page/Slide 10



### 提取当前图片文字与公式

#### 文字内容
- 页码与章节：`366 EXCHANGE (Ch. 29)`
- 正文段落：  
  `consumption. In competitive equilibrium, total consumption of apples equals the total supply of apples and total consumption of bananas equals the total supply of bananas. Therefore Lucy will consume \( 12 - a_s \) apples and \( \mathbf{12} - b_s \) bananas. At a competitive equilibrium, Lucy will be consuming at one of her kink points. The kinks occur at bundles where Lucy consumes \( \mathbf{2} \) apples for every banana that she consumes. Therefore we know that \( \frac{12 - a_s}{12 - b_s} = \mathbf{2} \).`
- (c) 部分：  
  `(c) You can solve the two equations that you found above to find the quantities of apples and bananas consumed in competitive equilibrium by Linus and Lucy. Linus will consume \( \mathbf{6} \) units of apples and \( \mathbf{9} \) units of bananas. Lucy will consume \( \mathbf{6} \) units of apples and 3 units of bananas.`
- 问题 29.6：  
  `29.6 (0) Consider a pure exchange economy with two consumers and two goods. At some given Pareto efficient allocation it is known that both consumers are consuming both goods and that consumer A has a marginal rate of substitution between the two goods of 2. What is consumer B's marginal rate of substitution between these two goods? \( \mathbf{2} \).`
- 问题 29.7：  
  `29.7 (0) Charlotte loves apples and hates bananas. Her utility function is \( U(a, b) = a - \frac{1}{4}b^2 \), where \( a \) is the number of apples she consumes and \( b \) is the number of bananas she consumes. Wilbur likes both apples and bananas. His utility function is \( U(a, b) = a + 2\sqrt{b} \). Charlotte has an initial endowment of no apples and 8 bananas. Wilbur has an initial endowment of 16 apples and 8 bananas.`  
  `(a) On the graph below, mark the initial endowment and label it E. Use red ink to draw the indifference curve for Charlotte that passes through this point. Use blue ink to draw the indifference curve for Wilbur that passes through this point.`

#### 公式
- Lucy 的均衡条件：  
  \( \frac{12 - a_s}{12 - b_s} = 2 \)  
  （其中 \( a_s \) 为 Linus 的苹果消费量，\( b_s \) 为 Linus 的香蕉消费量）
- 均衡消费量：  
  - Linus: \( (a_s, b_s) = (6, 9) \)  
  - Lucy: \( (a_L, b_L) = (6, 3) \)
- 问题 29.6 的答案：  
  \( \text{MRS}_B = 2 \)
- 问题 29.7 的效用函数：  
  - Charlotte: \( U(a, b) = a - \frac{1}{4}b^2 \)  
  - Wilbur: \( U(a, b) = a + 2\sqrt{b} \)

---

### 关键内容解析（结合上文知识点总结）

#### 1. Lucy 的 Leontief 约束与契约曲线验证
- **公式 \( \frac{12 - a_s}{12 - b_s} = 2 \) 的经济含义**：  
  该式直接源于 Lucy 的 Leontief 效用 \( U_L = \min\{a_L, 2b_L\} \)。在 Pareto 最优配置中，Lucy 的消费必须满足刚性比例 \( a_L = 2b_L \)（即 \( \frac{a_L}{b_L} = 2 \)）。  
  - 此处 \( a_L = 12 - a_s \)，\( b_L = 12 - b_s \)，代入得 \( \frac{12 - a_s}{12 - b_s} = 2 \)。  
  - 这 **印证了上文“Black line 由 \( a_L = 2b_L \) 唯一决定”的核心原理**：契约曲线形态完全由偏好刚性主导，而非初始禀赋。均衡点必须落在此线上（如上文所述，Black line 方程为 \( x = 2y - 12 \)）。

#### 2. 均衡消费量的结构必然性
- **Linus (6,9) 与 Lucy (6,3) 的解析**：  
  - 该分配满足：
    - Lucy 的比例约束：\( \frac{a_L}{b_L} = \frac{6}{3} = 2 \)。  
    - 总禀赋守恒：苹果 \( 6 + 6 = 12 \)，香蕉 \( 9 + 3 = 12 \)。  
  - **与上文价格机制一致**：Linus 的线性效用 \( U_S = a_s + 2b_s \) 导出 MRS = \( \frac{1}{2} \)，锁定价格比 \( \frac{p_a}{p_b} = \frac{1}{2} \)。  
  - 代入 Linus 预算约束 \( a_s + 2b_s = 24 \)（初始禀赋 12 苹果 + 24 香蕉价值）：  
    \( 6 + 2 \times 9 = 24 \)，验证均衡唯一性。  
  - **关键延续**：消费分配由偏好参数（Leontief 系数 2）直接决定，总禀赋比例 \( \frac{12}{12} = 1 \) 被覆盖，呼应上文“实际消费比例由偏好刚性锁定”的结论。

#### 3. 问题 29.6 的帕累托最优条件强化
- **MRS 相等性 \( \text{MRS}_B = 2 \) 的逻辑延伸**：  
  - 在 Pareto 最优配置中，当双方均消费两种商品，必须满足 \( \text{MRS}_A = \text{MRS}_B \)。  
  - 此结果 **实证上文“Pareto 最优点要求 MRS 相等”的基础定理**：在 Lucy-Linus 例中，Lucy 的 kink 点 MRS 无定义，但仅当 \( a_L = 2b_L \) 时，Linus 的 MRS = \( \frac{1}{2} \) 与 Lucy 的有效 MRS 一致。  
  - 即使效用函数形式不同（如 Leontief vs. 线性），该条件仍成立，体现上文“偏好主导效率边界”的普适性。

#### 4. 问题 29.7 的关联启示（知识连续性）
- **Charlotte 与 Wilbur 的效用结构**：  
  - Charlotte 的效用 \( U = a - \frac{1}{4}b^2 \) 中，\( b \) 项为负二次型，导致其对香蕉的 MRS 非递减（随 \( b \) 增加，MRS 上升）。  
  - Wilbur 的效用 \( U = a + 2\sqrt{b} \) 的 MRS = \( \frac{1}{2\sqrt{b}} \)，随 \( b \) 递减。  
  - **与上文刚性约束对比**：若存在类似 Leontief 的显式比例限制（如 \( a = kb \)），契约曲线将退化为射线；但此处效用函数连续可微，契约曲线为连续曲线（MRS 相等的轨迹）。  
  - 延续上文逻辑：初始禀赋（E 点）偏离 MRS 相等点时，价格机制驱动交易至 Pareto 最优点，印证“trade dynamics shift consumption”的原理。

---
### Page/Slide 11



### Detailed Analysis of Current Image

#### 1. Extracted Text and Formulas from Image
**Graphic Elements (Edgeworth Box):**
- **Axes**: Horizontal axis (Bananas, 0–16), vertical axis (Apples, 0–16)
- **Origins**: 
  - "Charlotte" at bottom-left (0,0)
  - "Wilbur" at top-right (16,16)
- **Labeled Features**:
  - "Black line" (a vertical line at bananas = 0 for Charlotte)
  - "Blue line" (a curved line; initial endowment point "e" marked near (bananas ≈ 8, apples ≈ 0) for Charlotte)
  - "Red line" (a steep upward-sloping line through point "e")
- **Point**: "e" (initial endowment, coordinates approximately (8, 0) in Charlotte's consumption space)

**Text Content:**
- **(b)** If Charlotte hates bananas and Wilbur likes them, how many bananas can Charlotte be consuming at a Pareto optimal allocation? **0**. On the graph above, use black ink to mark the locus of Pareto optimal allocations of apples and bananas between Charlotte and Wilbur.
- **(c)** We know that a competitive equilibrium allocation must be Pareto optimal and the total consumption of each good must equal the total supply, so we know that at a competitive equilibrium, Wilbur must be consuming **16** bananas. If Wilbur is consuming this number of bananas, his marginal utility for bananas will be **1/4** and his marginal utility of apples will be **1**. If apples are the numeraire, then the only price of bananas at which he will want to consume exactly 16 bananas is **1/4**. In competitive equilibrium, for the Charlotte-Wilbur economy, Wilbur will consume **16** bananas and **14** apples and Charlotte will consume **0** bananas and **2** apples.
- **29.8 (0)** Mutt and Jeff have 8 cups of milk and 8 cups of juice to divide between themselves. Each has the same utility function given by $u(m,j) = \max\{m,j\}$, where $m$ is the amount of milk and $j$ is the amount of juice that each has. That is, each of them cares only about the larger of the two amounts of liquid that he has and is indifferent to the liquid of which he has the smaller amount.

**Explicit Formulas:**
- Marginal utility for Wilbur's bananas at equilibrium: $\text{MU}_b = \frac{1}{4}$
- Marginal utility for Wilbur's apples: $\text{MU}_a = 1$
- Banana price (with apples as numeraire): $p_b = \frac{1}{4}$
- Competitive equilibrium allocation:
  - Charlotte: $(a_c, b_c) = (2, 0)$
  - Wilbur: $(a_w, b_w) = (14, 16)$

---

#### 2. Chart Interpretation via Microeconomic Principles
The Edgeworth Box illustrates the Charlotte-Wilbur exchange economy with total endowment (16 apples, 16 bananas). It integrates the utility functions from **Problem 29.7** in the knowledge summary ($U_c = a_c - \frac{1}{4}b_c^2$ for Charlotte; $U_w = a_w + 2\sqrt{b_w}$ for Wilbur). Below, we interpret the lines in relation to Pareto optimality, equilibrium, and their economic implications, emphasizing continuity from prior concepts.

##### **Black Line: Locus of Pareto Optimal Allocations**
- **Economic Meaning**: Represents the contract curve where Pareto optimality holds. Charlotte's utility function $U_c = a_c - \frac{1}{4}b_c^2$ implies a negative marginal utility for bananas ($\text{MU}_b^c = -\frac{1}{2}b_c < 0$ for $b_c > 0$), meaning she *hates bananas*. Thus:
  - No Pareto optimal allocation has $b_c > 0$, as transferring bananas from Charlotte to Wilbur strictly benefits both parties (Charlotte gains utility by consuming fewer bananas; Wilbur gains from higher banana consumption).
  - All Pareto optimal points have $b_c = 0$ (Charlotte consumes zero bananas), with bananas fully allocated to Wilbur ($b_w = 16$). The Black line is the **left edge** of the box (where Charlotte's banana consumption is zero), and apples can be freely allocated (e.g., Charlotte $(0, a_c)$, Wilbur $(16, 16 - a_c)$ for $a_c \in [0,16]$).
- **Connection to Prior Knowledge**:  
  This contrasts with the Lucy-Linus example (**key point 1** in the summary), where preference rigidity (Leontief) generated a linear contract curve ($a_L = 2b_L$). Here, Charlotte’s *non-convex disutility* (quadratic in bananas) forces a **corner solution** contract curve (vertical line at $b_c = 0$), but it still embodies the core Pareto efficiency principle: when one agent has negative MRS, efficient allocations exclude that good from their consumption. This aligns with **Problem 29.6**’s insight that MRS equality is necessary for interior solutions; here, the "MRS" for Charlotte is undefined for $b_c > 0$, leading to a boundary rule.

##### **Blue Line and Point e: Initial Endowment and Inefficiency**
- **Economic Meaning**: The Blue line and point "e" (near $(b_c, a_c) \approx (8, 0)$) denote the initial endowment. Charlotte starts with 8 bananas and 0 apples; Wilbur with 8 bananas and 16 apples.
  - This allocation is **inefficient**: Charlotte holds bananas, which reduce her utility, while Wilbur’s higher marginal utility for bananas ($\text{MU}_b^w = \frac{1}{\sqrt{b_w}} = \frac{1}{\sqrt{8}} \approx 0.35$) could be increased via trade.
  - The curved Blue line suggests possible contract mechanisms, but the tangent to this line at "e" does not satisfy MRS equality (Charlotte’s MRS is undefined/volatile due to disutility; Wilbur’s MRS $\approx 0.35$), confirming inefficiency.
- **Connection to Prior Knowledge**:  
  This mirrors the **Lucy-Linus example** (section 2 of the summary), where initial endowments not on the Black line (e.g., initial $(a_s, b_s) \neq (6,9)$) were inefficient. The inefficiency here stems from preference asymmetry (Charlotte’s disutility), but the **principle of trade-driven efficiency** (**key point 4** in the summary) applies: price mechanisms will reallocate resources to the contract curve.

##### **Red Line: Competitive Equilibrium Budget Line**
- **Economic Meaning**: The Red line is the competitive equilibrium budget line with apples as the numeraire ($p_a = 1$). Its slope is $-p_b / p_a = -1/4$, derived from:
  - Wilbur’s MRS condition: At $b_w = 16$, $\text{MRS}_w = \text{MU}_b^w / \text{MU}_a^w = (1/\sqrt{16}) / 1 = 1/4$. Equality with $p_b / p_a$ implies $p_b = 1/4$.
  - Equilibrium allocations: Charlotte consumes $(a_c, b_c) = (2, 0)$ (using all income on apples); Wilbur consumes $(a_w, b_w) = (14, 16)$. Total supply: $0 + 16 = 16$ bananas, $2 + 14 = 16$ apples.
  - **Income verification**: 
    - Charlotte’s income: $m_c = p_a a_c^0 + p_b b_c^0 = 1 \cdot 0 + (1/4) \cdot 8 = 2$; she demands $a_c = m_c = 2$, $b_c = 0$ (consistent with disutility).
    - Wilbur’s income: $m_w = p_a a_w^0 + p_b b_w^0 = 1 \cdot 16 + (1/4) \cdot 8 = 18$; at $b_w = 16$, $a_w = m_w - p_b b_w = 18 - 4 = 14$.
- **Connection to Prior Knowledge**:  
  This demonstrates the **automatic efficiency of competitive markets** (section 3 of the summary). The equilibrium is Pareto optimal (on the Black line), as required by the **first welfare theorem**. It extends **Problem 29.6**’s $ \text{MRS}_B = 2 $ by showing how price ratios "mimic" MRS equality even in boundary cases: here, Charlotte’s corner solution is consistent with Wilbur’s MRS, just as $a_L = 2b_L$ in Lucy-Linus locked the MRS ratio. Crucially, the price $p_b = 1/4$ is **determined solely by preferences** (Wilbur’s MU at $b_w = 16$), not the initial endowment—reinforcing the summary’s assertion that "actual consumption proportions are set by preference rigidities."

##### **Key Dynamics and Continuity**
- **Trade Mechanism**: Starting from "e," Charlotte abandons bananas immediately (due to disutility), selling all 8 bananas for apples at $p_b = 1/4$. She gains 2 apples (net income effect), while Wilbur uses the bananas to raise utility via $\sqrt{b_w}$. This **gains-from-trade process** (section 4, summary) closes the gap between initial endowment and Pareto optimum.
- ** depart from Rigid Proportions**: Unlike Lucy’s Leontief constraint ($a_L = 2b_L$), Charlotte’s disutility eliminates banana consumption entirely. This shows how **preference type dictates the contract curve’s shape** (degenerating to a corner solution), while the MRS-equality logic remains valid for the other agent.
- **Link to Problem 29.8**: Mutt and Jeff’s $\max\{m,j\}$ utility (text section) also generates a corner-based contract curve, but as a pure linear trade-off (no disutility), highlighting how utility structure—not just initial endowments—shapes efficiency outcomes. This underscores the summary’s emphasis on "preference dominant" efficiency boundaries.

> **Summary of Chart Changes**: The Black line (contract curve) is vertical due to Charlotte’s disutility; the Red line (equilibrium) tangentially touches this curve at $(0, 2)$; and the Blue line (initial) lies off-curve, driving trade to the equilibrium point. This system confirms that **Pareto optimality is achievable only when preferences dictate consumption at boundaries or MRS equals prices**, extending the core tenets of the knowledge summary without redundancy.

---
### Page/Slide 12



### 1. 提取文字与图表元素  
**图片文字内容**：  
- 页眉：`368 EXCHANGE (Ch. 29)`  
- 问题描述：  
  > (a) Sketch an Edgeworth box for Mutt and Jeff. Use blue ink to show a couple of indifference curves for each. Use red ink to show the locus of Pareto optimal allocations. (Hint: Look for boundary solutions.)  
- 坐标轴标签：  
  - 左下角：`Mutt`（原点），`0`（Milk 横轴起点），`Juice`（纵轴标签）  
  - 右上角：`Jeff`，`8`（Milk 横轴终点）  
- 图表标注：  
  - `Red point`（Mutt 坐标系左上和 Jeff 坐标系右下各一个）  
  - `Blue curves (Mutt)`（Mutt 坐标系中左下角 L 形无差异曲线）  
  - `Blue curves (Jeff)`（Jeff 坐标系中右上角倒置 L 形无差异曲线）  
  - 对角线（从 Mutt 原点至 Jeff 坐标 (8,8) 的直线）  

**公式**：  
图片中无显式公式，但问题指向 **$ u = \max\{m, j\} $**（隐含于上文对 Problem 29.8 的引用）。  

---

### 2. 图表解析与知识连续性  
#### **核心结构与含义**  
- **坐标系设定**：  
  Edgeworth 框总禀赋为 **8 单位 Milk**（横轴）和 **8 单位 Juice**（纵轴）。Mutt 从左下角（0,0）消费，Jeff 从右上角（8,8）消费。  
  - *知识连续性*：延续上文 **Lucy-Linus 模型** 的禀赋标准化逻辑，但此处总禀赋为 **(8,8)**，而非上文的隐式比例。

- **蓝线（无差异曲线）**：  
  - Mutt 的 `Blue curves` 呈 **L 形**（角点在横轴/纵轴方向延伸），反映 $ u = \max\{m_m, j_m\} $ 的效用结构：  
    - 当 $ m_m = 2 $ 时，无差异曲线为 $ j_m \leq 2 $（水平段）和 $ m_m = 2 $（垂直段）；  
    - 效用仅由较大值决定，故边际替代率（MRS）在内部区域未定义，仅在边界为 0 或 ∞。  
  - Jeff 的 `Blue curves` 为倒置 L 形，逻辑相同但方向相反。  
  - *知识连续性*：与上文 **Charlotte 的边界解** 本质一致——**偏好刚性直接导致无差异曲线断裂**，此处因 $ \max $ 结构跳过内部切点，直接强制边界主导。

- **红线（Pareto 最优轨迹）**：  
  两类 `Red point` 位于边界：  
  - Mutt 的红点：**(0,8)**（Mutt 仅消费 Juice，Jeff 消费所有 Milk）；  
  - Jeff 的红点：**(8,0)**（Jeff 仅消费 Milk，Mutt 消费所有 Juice）。  
  - *解释*：  
    由于双方效用均依赖于 **单一商品的最大值**，任何内部分配均存在帕累托改进空间。例如：  
    - 若 Mutt 消费 (1,1)，其效用为 1；若将多余资源转移至 Jeff 的优势商品（如 Jeff 仅消费 Milk），双方效用均可提升。  
    - 唯有当至少一方垄断 **其中一种商品全部禀赋** 时，达到帕累托最优。  
  - *知识连续性*：  
    直接验证上文 **"preference dominant efficiency boundaries"** ——  
    - **Lucy-Linus** 的 Leontief 约束（$ a_L = 2b_L $）导致合同曲线退化为对角线；  
    - **Mutt-Jeff** 的 $ \max\{m,j\} $ 约束导致合同曲线退化为 **边界线**。  
    两者均表明 **效用结构而非禀赋** 决定效率边界形态。

- **对角线与贸易方向**：  
  对角线（总禀赋约束线）与红点分离，说明 **初始禀赋（未标注）必然位于无效率区域**。  
  - 例如：若初始点为 (4,4)，Mutt 和 Jeff 的效用均为 4；通过贸易，将 Milk 全部转移至 Jeff（(0,8)）可使 Jeff 效用升至 8，Mutt 损失可被 Juice 补偿（因 Mutt 更在乎 Juice 极值）。  
  - *知识连续性*：  
    延续上文 **"gains-from-trade process"** —— 贸易通过消除禀赋错配（非偏好最优）逼近边界解，验证 **价格机制仅在边界使 MRS "mimic" 价格比**（此处因 $ \max $ 结构，贸易本质是商品所有权转移，而非连续替代）。

#### **关键差异与深化**  
- **与 Charlotte 模型的对比**：  
  Charlotte 因 **香蕉负效用** 彻底退出香蕉消费（$ b_c = 0 $）；  
  Mutt-Jeff 因 **$ \max $ 效用** 被迫在两种商品间 **二选一**，而非单侧退出。  
  → 体现 **不同偏好类型**（厌恶、极值偏好）均导向边界解，但机制不同：  
  - Charlotte：效用函数存在 **负域**；  
  - Mutt-Jeff：效用函数存在 **不可微极值**。  

- **对 "Preference Rigidities" 的再强化**：  
  本图中，**合同曲线完全脱离内部区域**，说明当效用函数为 **分段常数或非凸** 时，孟格尔-埃奇沃思均衡必须位于边界——直接支持上文 **"actual consumption proportions are set by preference rigidities"**。  

> **图表动态总结**：  
> 蓝线（无差异曲线）断裂 → 红线（最优解）紧贴边界 → 初始禀赋必然驱动贸易至边界点。  
> 此一过程**完全由效用函数刚性主导**，与禀赋分布无关（因总禀赋固定，仅转移方向由偏好决定），是上文 **"price ratio mimics MRS at boundaries"** 的拓扑扩展。

---
### Page/Slide 13



### 图表解析：Tommy 与 Mrs. Twit 的偏好结构与帕累托最优边界

#### 1. 提取图片文字与公式
- **坐标轴**：
  - X 轴（横轴）：Cookies（取值 0–16）
  - Y 轴（纵轴）：Milk（取值 0–16）
- **曲线标签**：
  - "Blue curve"（蓝色曲线）
  - "Red curve"（红色曲线）
  - "Tommy's red curve"（Tommy 的红色曲线，与红曲线重合）
  - "Black line"（黑色线，图表中已存在）
- **阴影区域**：图表中部存在一个以蓝色斜线填充的扇形区域
- **问题文本**：
  - (a) 问题：*On the graph, shade in the area consisting of combinations of cookies and milk that both Tommy and his mother agree are better than 7 cookies and 8 glasses of milk, where “better” for Mrs. Twit means she thinks it is healthier, and where “better” for Tommy means he likes it better.*  
    （译：在图表上涂阴影，表示双方均认为比 7 块饼干和 8 杯牛奶更优的组合，“更优”对 Mrs. Twit 意味着她认为更健康，对 Tommy 意味着他更喜欢。）
  - (b) 问题：*Use black ink to sketch the locus of “Pareto optimal” bundles of cookies and milk for Tommy. In this situation, a bundle is Pareto optimal if any bundle that Tommy prefers to this bundle is a bundle that Mrs. Twit thinks is worse for him. The locus of Pareto optimal points that you just drew should consist of two line segments. These run from the point (8,4) to the point 5,7 and from that point to the point 2,7.*  
    （译：用黑色墨水绘制 Tommy 的“帕累托最优”组合轨迹。此处，若 Tommy 偏好的任意其他组合均被 Mrs. Twit 认为对他更不利，则该组合适为帕累托最优。所绘轨迹应由两段线段组成：从 (8,4) 到 (5,7)，再从 (5,7) 到 (2,7)。）
  - 29.10 (2) 附加说明：*This problem combines equilibrium analysis with some of the things you learned in the chapter on intertemporal choice. It concerns the economics of saving and the life cycle on an imaginary planet where life is short and simple. In advanced courses in macroeconomics, you would study more-complicated versions of this model that build in more earthly realism. For the present, this simple model gives you a good idea of how the analysis must go.*  
    （译：本题结合了均衡分析与跨期选择章节的知识，涉及一个假想星球上的储蓄与生命周期经济学。在宏观经济学高级课程中，将学习更复杂的模型；当前简化模型有助于理解分析框架。）
- **关键坐标点**：  
  $(8,4)$, $(5,7)$, $(2,7)$

#### 2. 图表含义解释（结合上文知识点）

##### 图表结构概述
- **蓝色曲线（Blue curve）**：代表 Mrs. Twit 的无差异曲线。其“健康偏好”隐含 **cookies 为厌恶品**（cookies 不健康，低消费更优），而 milk 为正常品（高消费更优）。这导致其无差异曲线斜率为正（需补偿牛奶增加以容忍更多 cookies），且更靠近左上象限的曲线表示更高效用（即更低 cookies 与更高 milk）。
- **红色曲线（Tommy's red curve）**：代表 Tommy 的无差异曲线。其“喜好偏好”表明 **cookies 为正常品**（高消费更优），milk 的偏好较弱（可能为中性或低权重）。曲线斜率为负，但因偏好刚性，内部区域可能不存在有效替代（类似上文 Mutt-Jeff 模型的 max 结构）。
- **预设黑色线（Black line）**：与问题 (b) 要求绘制的帕累托最优轨迹一致，形成于两条线段的交点（kink point），即 $(5,7)$。其形状直接反映**偏好刚性对有效边界的决定作用**。
- **阴影区域**：问题 (a) 要求涂色的集合，表示双方均认为优于 $(7,8)$ 的组合。  
  - **Mrs. Twit 的优于集**：由于 cookies 为厌恶品，优于 $(7,8)$ 的组合需同时满足 cookies $\leq 7$（更健康）且 milk $\geq 8$（或隐含补偿）。在图表中，蓝曲线左侧/上方区域（如更低 cookies 和更高 milk）为更优。  
  - **Tommy 的优于集**：由于 cookies 为正常品，优于 $(7,8)$ 的组合需 cookies $\geq 7$（更高偏好）。  
  - **交集**：阴影区域为两集交集，呈扇形——**cookies 减少但 milk 不下降的区域**（近似蓝曲线向左上延伸的部分），体现双方偏好冲突下的有限交易区域。

##### 帕累托最优轨迹的动态含义
问题 (b) 指出帕累托最优轨迹由 **$(8,4) \to (5,7) \to (2,7)$** 两段线段构成，核心在于**偏好刚性导致合同曲线退化**：
- **第一段（从 $(8,4)$ 到 $(5,7)$）**：  
  - 斜率 $= \frac{7-4}{5-8} = -1$，表示此时 **Tommy 的边际替代率（MRS）等于 1**（每放弃 1 单位 cookies 需补偿 1 单位 milk 以维持效用）。  
  - 但 MRS 的连续性被破坏：Mrs. Twit 的厌恶品偏好（cookies 为坏）使内部区域不存在有效替代（类似上文 Charlotte 模型的**负效用边界解**）。 trade 仅在 **milk 增加与 cookies 减少同步** 时可行，效果类似上文 **"price ratio mimics MRS at boundaries"** 的拓扑扩展。
- **第二段（从 $(5,7)$ 到 $(2,7)$）**：  
  - 恒定 milk $=7$，cookies 从 5 降至 2，形成**水平线段**。  
  - 含义：当 milk $\leq 7$ 时，Tommy 的效用主要取决于 cookies（类似上文 Mutt-Jeff 的 $\max\{m,j\}$ 结构），MRS 趋向无穷（milk 变化对效用影响可忽略）。而 Mrs. Twit 在 milk $=7$ 时视 cookies 变化为“过度消费”，触发**二元决策**（cookies 仅能单调减少）。  
  - **关键机制**：点 $(5,7)$ 为**刚性转折点**——与上文 Mutt-Jeff 的 **"preference dominant efficiency boundaries"** 完全呼应：  
    > - 若 milk $>7$，Mrs. Twit 的“健康约束”失效，偏好刚性消失；  
    > - 仅当 milk $\leq 7$ 且 cookies 单调递减时，达成帕累托最优（避免双方效用损失）。

##### 与上文知识点的连续性
- **偏好刚性驱动效率边界**：  
  此图是上文 Mutt-Jeff 模型的**变体拓展**。上文 Mutt-Jeff 因 $\max\{m,j\}$ 效用函数导致帕累托最优解**束缚于资源边界**（如 $(0,8)$ 或 $(8,0)$）；本图中 Mrs. Twit 的厌恶品偏好（cookies）与 Tommy 的选择偏好，使最优解**束缚于内部折线**（非纯边界，但受刚性约束）。两者共同验证 **"actual consumption proportions are set by preference rigidities"** ——禀赋（总资源 16×16）仅提供规模，而效率形状完全由偏好决定。
  
- **帕累托最优与交易方向的延续性**：  
  - 上文 Mutt-Jeff 中，初始禀赋（如 $(4,4)$）因非边界解而存在改进空间；本图中，基准点 $(7,8)$ 位于阴影外（即无效率区域），**贸易必须驱动至 $(5,7)$ 附近**。  
  - 具体机制：  
    - 在 $(7,8)$，Tommy 偏好高 cookies（无效率），但 Mrs. Twit 视高 cookies 为“有害”；  
    - 通过减少 cookies 至 5–2 区间，增加 milk 至 7–8 区间，达成 **"gains-from-trade"**（贸易利得）——这与上文 **"trade through eliminating endowment misallocation"** 一致，但此处因偏好刚性，贸易路径**被锚定在折线轨迹**而非连续曲线。

- **关键差异点**：  
  上文 Charlotte 模型因**单一商品负效用**导致单侧退出（$b_c=0$），而本图因 **"dual rigidities"**（多重刚性：cookies 对 Mrs. Twit 为恶/对 Tommy 为好）触发**内部折线解**，而非纯边界解。这深化了上文 **"preference rigidities produce non-standard efficiency sets"** 的结论——变体偏好类型（厌恶品、极值偏好）均导向退化合同曲线，但形态随扭曲机制变化。

> **图表动态总结**：  
> 蓝/红曲线的冲突斜率 $\rightarrow$ 阴影区域受限 $\rightarrow$ 帕累托最优退化为折线。  
> 此过程**完全由偏好刚性主导**：Mrs. Twit 的健康厌恶（类似负效用）与 Tommy 的选择偏好（类似极值）共同约束解空间，与禀赋分布无关（总资源仅缩放解集），是上文 **"contract curve topology is preference-determined"** 的实证延伸。

---
### Page/Slide 14



### 提取当前图片中的所有文字、公式

#### 文字内容
- 页码：370  
- 标题：EXCHANGE (Ch. 29)  
- 正文：  
  "On the planet Drongo there is just one commodity, cake, and two time periods. There are two kinds of creatures, “old” and “young.” Old creatures have an income of $I$ units of cake in period 1 and no income in period 2. Young creatures have no income in period 1 and an income of $I^*$ units of cake in period 2. There are $N_1$ old creatures and $N_2$ young creatures. The consumption bundles of interest to creatures are pairs $(c_1, c_2)$, where $c_1$ is cake in period 1 and $c_2$ is cake in period 2. All creatures, old and young, have identical utility functions, representing preferences over cake in the two periods. This utility function is $U(c_1, c_2) = c_1^a c_2^{1-a}$, where $a$ is a number such that $0 \leq a \leq 1$."  

- (a) 部分：  
  "If current cake is taken to be the numeraire, (that is, its price is set at 1), write an expression for the present value of a consumption bundle $(c_1, c_2)$. $c_1 + c_2 / (1 + r)$. Write down the present value of income for old creatures $I$ and for young creatures $I^* / (1 + r)$. The budget line for any creature is determined by the condition that the present value of its consumption bundle equals the present value of its income. Write down this budget equation for old creatures: $c_1 + c_2 / (1 + r) = I$ and for young creatures: $c_1 + c_2 / (1 + r) = I^* / (1 + r)$."  

- (b) 部分：  
  "If the interest rate is $r$, write down an expression for an old creature’s demand for cake in period 1 $c_1 = a I$ and in period 2 $c_2 = (1 - a) I (1 + r)$. Write an expression for a young creature’s demand for cake in period 1 $c_1 = a I^* / (1 + r)$ and in period 2 $c_2 = (1 - a) I^*$. (Hint: If its budget line is $p_1 c_1 + p_2 c_2 = W$ and its utility function is of the form proposed above, then a creature’s demand function for good 1 is $c_1 = a W / p_1$ and demand for good 2 is $c_2 = (1 - a) W / p_2$.) If the interest rate is zero, how much cake would a young creature choose in period 1? $a I^*$. For what value of $a$ would it choose the same amount in each period if the interest rate is zero? $a = 1/2$. If $a = .55$, what would $r$ have to be in order that young creatures would want to consume the same amount in each period? $.22$."  

- (c) 部分：  
  "The total supply of cake in period 1 equals the total cake earnings of all old creatures, since young creatures earn no cake in this period. There are $N_1$ old creatures and each earns $I$ units of cake, so this total is $N_1 I$. Similarly, the total supply of cake in period 2 equals the total amount earned by young creatures. This amount is $N_2 I^*$."  

#### 公式汇总
| 项目 | 公式 |
|------|------|
| 效用函数 | $U(c_1, c_2) = c_1^a c_2^{1-a}$ |
| 消费束现值 | $c_1 + \frac{c_2}{1 + r}$ |
| 老生物收入现值 | $I$ |
| 年轻生物收入现值 | $\frac{I^*}{1 + r}$ |
| 老生物预算线 | $c_1 + \frac{c_2}{1 + r} = I$ |
| 年轻生物预算线 | $c_1 + \frac{c_2}{1 + r} = \frac{I^*}{1 + r}$ |
| 老生物时期1需求 | $c_1 = a I$ |
| 老生物时期2需求 | $c_2 = (1 - a) I (1 + r)$ |
| 年轻生物时期1需求 | $c_1 = \frac{a I^*}{1 + r}$ |
| 年轻生物时期2需求 | $c_2 = (1 - a) I^*$ |
| 年轻生物时期1消费（$r=0$） | $a I^*$ |
| 消费平滑条件（$r=0$） | $a = \frac{1}{2}$ |
| 消费平滑条件（$a=0.55$） | $r = 0.22$ |
| 时期1总供给 | $N_1 I$ |
| 时期2总供给 | $N_2 I^*$ |

---

### 模型解析：与上文知识点的连续性

当前图片描述了一个**跨期交换经济模型**（intertemporal exchange economy），与上文知识点在结构上高度呼应，但将静态商品交换延伸至时间维度。核心在于**偏好参数 $a$ 如何驱动跨期消费路径**，验证了上文关于“preference rigidities”和“gains-from-trade”的机制。关键解析如下：

#### 1. **偏好结构与边际替代率（MRS）的延续性**
   - 上文知识点强调：MRS 是贸易的基础（如 Tommy 的 MRS = 1 驱动 cookies-milk 交换），且偏好刚性（如厌恶品）会扭曲 MRS 路径。
   - 本模型中，效用函数 $U(c_1, c_2) = c_1^a c_2^{1-a}$ 隐含 MRS 计算：
     $$
     \text{MRS} = \frac{MU_{c_1}}{MU_{c_2}} = \frac{a c_2}{(1 - a) c_1}
     $$
     - **与上文连续性**：MRS 直接决定跨期贸易条件，等价于上文的“price ratio mimics MRS at boundaries”。当 $a \neq 0.5$ 时（如 $a = 0.55$），MRS 生态不对称，迫使利率 $r$ 调整以达成消费平滑（$c_1 = c_2$）。这强化了上文结论——**消费比例由偏好刚性设定**：若 $a$ 偏离 0.5，偏好扭曲引发“类退化解”（如部分 (b) 中 $r = 0.22$ 时才能平衡消费），类似上文 Mrs. Twit 的“dual rigidities”导致内部折线解。
     - *差异点*：上文偏好刚性源于厌恶品等外生约束，本模型偏好刚性内生于 $a$ 参数，但机制一致：$a$ 越接近 0 或 1，MRS 对 $c_1/c_2$ 比例越敏感，逼近“极值偏好”（如上文 $\max\{m,j\}$），引发边界解（e.g., 若 $a \to 1$，老生物几乎不消费时期2）。

#### 2. **贸易路径与帕累托最优的动态延伸**
   - 上文知识点指出：贸易需消除禀赋错配（如基准点 $(7,8)$ 位于无效率区域），且路径受偏好约束锚定在折线。
   - 本模型中，禀赋分配天然错配：
     - 老生物仅在时期1有收入 ($I$)，年轻生物仅在时期2有收入 ($I^*$)。
     - 通过借贷市场（利率 $r$），实现 **“gains-from-trade”**：
       - 老生物储蓄（$c_1 < I$，$c_2 > 0$），年轻生物借贷（$c_1 > 0$，$c_2 < I^*$）。
     - **与上文连续性**：  
       - 此过程复刻上文 “trade through eliminating endowment misallocation”：初始禀赋（老生物占时期1收入，年轻生物占时期2）对应上文阴影区域，贸易将系统推向帕累托最优（如部分 (b) 中消费平滑）。  
       - 贸易方向由 $a$ 驱动：若 $a > 0.5$，老生物过度偏好时期1，需更高 $r$ 刺激储蓄（如 $a=0.55$ 时 $r=0.22$），类似上文 trade 仅在 “milk 增加与 cookies 减少同步” 时可行——**利率 $r$ 是跨期版的 “price ratio”**。

#### 3. **合同曲线拓扑的偏好依赖性强化**
   - 上文核心结论：**合同曲线形态由偏好决定，而非禀赋**（如 Mutt-Jeff 模型中 $\max\{m,j\}$ 使最优解束缚于边界）。
   - 本模型进一步实证：
     - 若 $a = 0.5$ 且 $r = 0$，消费平滑（$c_1 = c_2$），合同曲线为光滑曲线。
     - 若 $a \neq 0.5$，偏好扭曲迫使合同曲线退化为隐含“折线”（e.g., 部分 (b) 中 $r$ 需特定值以使消费比例匹配 $a$），直接呼应上文 “preference rigidities produce non-standard efficiency sets”。
     - *关键延续*：总供给 $N_1 I$ 和 $N_2 I^*$（部分 (c)）仅缩放解规模，不改变拓扑——与上文“禀赋仅提供规模，效率形状由偏好决定”完全一致。

#### 总结
本模型是上文静态交换经济的**跨期变体**：  
- $a$ 参数等价于上文的偏好刚性机制（如 cookies 厌恶品），驱动贸易路径（利率 $r$ 替代了上文的 milk-cookies 替代率）。  
- 无额外图表，但需求函数（部分 (b)）隐含动态调整过程：$a$ 扭曲消费平衡点，需 $r$ 矫正，这深化了上文 **“contract curve topology is preference-determined”** ——**偏好刚性将帕累托最优嵌入跨期利率的动态响应中**。  
此扩展表明，上文结论不仅适用于静态商品，也普适于时间维度的资源分配，验证了微观基础的统一性。

---
### Page/Slide 15



### 提取内容：文字与公式

#### 文字内容
- **(d)** At the equilibrium interest rate, the total demand of creatures for period-1 cake must equal total supply of period-1 cake, and similarly the demand for period-2 cake must equal supply. If the interest rate is $r$, then the demand for period-1 cake by each old creature is $aI$ and the demand for period-1 cake by each young creature is $aI^*/(1 + r)$. Since there are $N_1$ old creatures and $N_2$ young creatures, the total demand for period-1 cake at interest rate $r$ is $N_1 a I + N_2 a I^*/(1 + r)$.  
- **(e)** Using the results of the last section, write an equation that sets the demand for period-1 cake equal to the supply. $N_1 a I + N_2 a I^*/(1 + r) = N_1 I$. Write a general expression for the equilibrium value of $r$, given $N_1$, $N_2$, $I$, and $I^*$. $r = \frac{N_2 I^* a}{N_1 I (1 - a)} - 1$. Solve this equation for the special case when $N_1 = N_2$ and $I = I^*$ and $a = 11/21$. $r = 10\%$.  
- **(f)** In the special case at the end of the last section, show that the interest rate that equalizes supply and demand for period-1 cake will also equalize supply and demand for period-2 cake. (This illustrates Walras’s law.) Supply = demand for period 2 if $N_1 (1 - a)I(1 + r) + N_2 (1 - a)I^* = N_2 I^*$. If $N_1 = N_2$ and $I = I^*$, then $(1 - a)(1 + r) + (1 - a) = 1$. If $a = 11/21$, then $r = 10\%$.

#### 公式内容
- 时期1需求：  
  $aI$（老生物）, $\quad \dfrac{aI^*}{1 + r}$（年轻生物）  
  $\text{总需求} = N_1 a I + N_2 \dfrac{a I^*}{1 + r}$  
- 均衡条件（时期1）：  
  $N_1 a I + N_2 \dfrac{a I^*}{1 + r} = N_1 I$  
- 均衡利率通解：  
  $r = \dfrac{N_2 I^* a}{N_1 I (1 - a)} - 1$  
- 特殊案例解：  
  $N_1 = N_2, \, I = I^*, \, a = \dfrac{11}{21} \implies r = 10\%$  
- 时期2供需均衡：  
  $\text{供给} = \text{需求} \iff N_1 (1 - a) I (1 + r) + N_2 (1 - a) I^* = N_2 I^*$  
  特殊案例下：  
  $(1 - a)(1 + r) + (1 - a) = 1 \quad \text{and} \quad r = 10\%$  

---

### 解析：延续偏好驱动的跨期均衡机制

#### 1. **均衡利率公式直接体现偏好参数 $a$ 的刚性约束**  
- 上文强调 $a$ 内生决定 **消费比例刚性**（如 $a \neq 0.5$ 时引发 "类退化解"），此处公式 $r = \frac{N_2 I^* a}{N_1 I (1 - a)} - 1$ 量化了该机制：  
  - $a$ 直接放大 $r$ 的均衡值（分子含 $a$，分母含 $1-a$），当 $a > 0.5$ 时（如 $a = 11/21 \approx 0.523 > 0.5$），$r > 0$ 以强制老生物减少 $c_1$、增加 $c_2$，实现消费平滑。  
  - 禀赋参数 ($N_1, N_2, I, I^*$) 仅缩放利率水平（作为分母或分子因子），但不改变 **偏好主导性**——若 $a$ 逼近 1（极度偏好时期1），$r \to \infty$，呼应上文 "极值偏好引发边界解"。  
- **连续性延伸**：此公式是上文 "MRS 生态不对称迫使利率调整" 的显式解。老生物的 $c_1$ 边际效用 $MU_{c_1} \propto a$ 高于 $c_2$ 的 $MU_{c_2} \propto 1-a$，需更高 $r$ 补偿储蓄成本，与上文 Tommy 的 MRS=1 驱动交换逻辑一致（利率 $r$ 作为跨期 "price ratio"）。

#### 2. **Walras 法则验证偏好对均衡路径的支配性**  
- 部分 (f) 证明：时期1的供需均衡（由 $a$ 和 $r$ 决定）自动保证时期2均衡，无需独立求解。这复刻了上文 **"合同曲线拓扑仅由偏好决定"** 的核心结论：  
  - 时期2方程 $N_1 (1 - a) I (1 + r) + N_2 (1 - a) I^* = N_2 I^*$ 的简化依赖 $a$ 和 $r$ 的关联（特殊案例中 $r$ 由 $a$ 唯一确定），而非禀赋规模。  
  - 当 $N_1 = N_2$ 且 $I = I^*$ 时，方程收缩为 $(1 - a)(1 + r) + (1 - a) = 1$，**$a$ 直接锁定 $r$ 的数值**（$a = 11/21 \implies r = 10\%$）。  
- **关键差异点**：上文静态模型中禀赋错配引致贸易路径，而此处跨期模型中，**时间维度强化了偏好刚性的作用**——$a$ 对 $r$ 的控制更绝对（如 $a$ 微小偏离 0.5 可显著扰动 $r$），体现了 "跨期贸易对偏好波动更敏感" 的延伸逻辑。

#### 3. **与上文知识点的统一性：无货币幻觉，利率纯由偏好校准**  
- 公式中 $r$ 的解 **仅依赖 $a$ 和禀赋比例**，与上文 "利率 $r$ 是跨期版 price ratio" 完全呼应：  
  - 当 $a = 0.5$ 时，$r = \frac{N_2 I^*}{N_1 I} - 1$，若 $N_1 = N_2, I = I^*$ 则 $r = 0$，对应无扭曲的消费平滑（上文 "光滑合同曲线" 情形）。  
  - 本例 $a > 0.5$ 要求 $r = 10\% > 0$，等同上文 Mrs. Twit 案例中 "dual rigidities 导致折线解" 的动态版本——$a$ 的刚性将帕累托最优约束嵌入利率动态。  
- **深化认知**：上文指出 "总供给仅提供规模"，此处通解 $r = \frac{N_2 I^* a}{N_1 I (1 - a)} - 1$ 中，$N_1, N_2, I, I^*$ 被约简为比率 $N_2 I^*/(N_1 I)$，不改变 $r$ 由 $a$ 主导的本质，直接验证 "效率形状由偏好决定" 的普适性。

---
### Page/Slide 16



# 交换理论章节过渡分析

## 图片内容提取
```
372 EXCHANGE (Ch. 29)
```

## 知识衔接与延续性分析

### 1. **章节定位与理论延续**
- 该页码标识表明当前处于跨期模型分析后的理论延伸阶段，"EXCHANGE"章节（第29章）将**系统化展开上文隐含的交换机制**：
  - 上文通过跨期消费选择展示的"偏好驱动均衡"逻辑，将在本章扩展至**多主体、多商品的一般交换框架**
  - 老生物与少生物的跨期交易模型实质是**二时期纯交换经济的特例**，本章将抽象为更通用的交换范式

### 2. **从跨期交换到纯交换经济的理论跃迁**
- 上文均衡条件 $N_1 a I + N_2 \frac{a I^*}{1 + r} = N_1 I$ 已隐含**总量守恒原理**，本章将显式构建：
  - **埃奇沃思盒状图**作为分析工具，替代上文隐含的"时间维度交换线"
  - 从单维度跨期选择转向**多维商品空间中的边际替代率均衡**
- **关键延续点**：上文证明的"偏好参数 $a$ 主导均衡路径"将泛化为**消费者偏好结构决定合同曲线拓扑**的核心定理

### 3. **Walras法则的显式化**
- 上文时期1均衡自动保证时期2均衡的论断（部分(f)），将在本章**形式化为一般均衡存在性定理**：
  - 跨期模型中的"隐性市场出清"将被提炼为$N$个市场中$N-1$个出清则全部出清的普适原则
  - 利率 $r$ 作为跨期价格，将扩展为**价格向量**在纯交换经济中的配置功能

> 该章节过渡标志着从**时间维度的特定交换机制**向**空间维度的普遍交换理论**的跃升，但始终延续"偏好结构塑造均衡路径"这一核心命题。上文建立的"参数 $a$ 对均衡利率的刚性约束"逻辑，将在本章发展为"偏好凸性与MRS差异决定合同曲线形态"的一般理论。
