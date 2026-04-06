# PDF_Chapter_13

### Page/Slide 1



### 1. 文字与公式提取  
- **章节标题**：Chapter 13、Risky Assets  
- **引言段落（Introduction）核心内容**：  
  > 消费者需在风险资产与安全资产间最优配置财富。组合预期收益率为安全资产收益率与风险资产预期收益率的加权平均（权重为财富占比）；组合标准差 = 风险资产标准差 × 风险资产财富占比。消费者面临风险-收益预算约束：全部配置安全资产时收益为安全利率、风险为0；增加风险资产配置比例 $ x $ 时，组合收益增量为 $ x(r_m - r_f) $，风险增量为 $ x\sigma_m $。预算线斜率 = 两资产收益差 ÷ 组合标准差，可通过无差异曲线-预算线分析求解最优风险承担。CAPM指出资产预期收益率 = 无风险利率 + 风险溢价。  
- **习题 13.1 (3)**：  
  > Ms. Lynch 可选择无风险资产（收益率 $ r_f $）和风险资产（预期收益率 $ r_m $、标准差 $ \sigma_m $）  
  **(a)** 组合预期收益率公式：$ r_x = x r_m + (1 - x) r_f $；组合标准差公式：$ \sigma_x = x \sigma_m $  

---

### 2. 核心理论解析（无图表，聚焦公式与逻辑连续性）  
#### （1）组合收益与风险的线性结构  
- **收益公式 $ r_x = x r_m + (1 - x) r_f $**：  
  直接体现引言所述"加权平均"逻辑。当 $ x = 0 $（全配安全资产）时，$ r_x = r_f $；当 $ x = 1 $（全配风险资产）时，$ r_x = r_m $。**财富在两类资产间的分割比例 $ x $ 线性决定组合收益**，为预算约束提供收益维度的数学表达。  

- **风险公式 $ \sigma_x = x \sigma_m $**：  
  验证引言核心结论——组合风险仅由风险资产占比 $ x $ 与风险资产固有风险 $ \sigma_m $ 决定（安全资产标准差为0，不贡献风险）。**风险与 $ x $ 严格线性正相关**，是预算约束中风险维度的数学表达。  

#### （2）预算约束的斜率含义（连接上文"预算线分析"）  
由 $ \sigma_x = x \sigma_m $ 得 $ x = \sigma_x / \sigma_m $，代入收益公式得：  
$$ r_x = r_f + \frac{r_m - r_f}{\sigma_m} \cdot \sigma_x $$  
此即预算线方程，**斜率 $ \frac{r_m - r_f}{\sigma_m} $ 称为"市场风险价格"**：  
- 分子 $ r_m - r_f $：风险资产相对于安全资产的**超额收益**（风险溢价来源）；  
- 分母 $ \sigma_m $：风险资产的**单位风险**；  
- 斜率表示"消费者每承担 1 单位组合风险，所能获得的额外预期收益"，是 CAPM 中风险-收益权衡的核心度量。  

#### （3）与上文知识的连续性  
- 引言中"无差异曲线-预算线分析"的实操基础：当前习题公式量化了**预算约束的边界条件**（收益-风险关系），为后续将无差异曲线（偏好）与预算线（约束）联立求解最优 $ x $ 提供数学工具。  
- CAPM 应用铺垫：公式中 $ r_m - r_f $ 直接对应 CAPM 的"风险调整项"，揭示**资产定价中风险与收益的量化关系**，为后续推导单个资产预期收益率与市场风险的关系提供逻辑起点。

---
### Page/Slide 2



### 一、文字与公式提取  
- **文字内容**：  
  - (b) 通过解第二个方程代入第一个方程，推导组合收益率关于组合风险性的表达式：$ r_x = \frac{r_m - r_f}{\sigma_m} \sigma_x + r_f $。  
  - (c) Ms. Lynch 以 $ r_f $ 借款投资风险资产：$ r_m = 20 $, $ r_f = 10 $, $ \sigma_m = 10 $，借入等于初始财富100%资金时，投资比例 $ x = 2 $，代入公式 $ r_x = x r_m + (1 - x) r_f $ 得 $ r_x = 2 \times 20 - 1 \times 10 = 30 $。  
  - (d) 允许无风险借贷时预算线公式：$ r_f = 10\% $, $ r_m = 20\% $, $ \sigma_m = 10\% $，得 $ r_x = \sigma_x + 10 $。  
  - (e) 资产偏好比较：  
    - Asset A ($ r_a = 17\% $, $ \sigma_a = 5\% $) → Better  
    - Asset B ($ r_b = 30\% $, $ \sigma_b = 25\% $) → Worse  

- **图表元素**：  
  - 坐标轴：横轴为 Standard deviation（0–40），纵轴为 Expected return（0–40）。  
  - 标签：Budget line（虚线）、U=0、U=5、U=10（无差异曲线）。  

---

### 二、图表解析  
结合上文核心理论，图中预算线 $ r_x = \sigma_x + 10 $ 是风险-收益预算约束的**具象化延伸**，关键说明如下：  

#### 1. **预算线斜率的实证意义**  
- 上文已定义预算线斜率 $ \frac{r_m - r_f}{\sigma_m} $ 为“市场风险价格”，在当前参数下 $ \frac{20\% - 10\%}{10\%} = 1 $，故方程 $ r_x = \sigma_x + 10 $ 直接体现：  
  - **截距 $ r_f = 10\% $**：对应 $ x = 0 $（全配安全资产），验证上文“风险为0时收益等于无风险利率”。  
  - **斜率 = 1**：表示每承担 **1 单位组合标准差**，预期收益增加 **1 单位**，即消费者承担 1% 额外风险可获 1% 额外收益。  
- **借贷场景的扩展**：  
  - 预算线向右延伸至 $ \sigma_x > 10 $（如 $ \sigma_x = 20 $ 时 $ r_x = 30 $），直观呈现习题 (c) 中 $ x > 1 $（借款杠杆）的情形。  
  - 与上文“预算约束仅限 $ x \in [0,1] $”不同，此处**允许借贷使预算线从 (0,10) 线性延展至风险更高区域**，强化了“风险-收益权衡的连续性”——最优解可落在 $ x > 1 $ 区域。  

#### 2. **无差异曲线与最优选择**  
- 无差异曲线 U=0、U=5、U=10 呈**凸向原点**，且 U 值越高劣集集向外扩张，符合上文“风险厌恶者偏好”的隐含假设：  
  - **凸性**：反映边际替代率递减——相同收益增量对高风险组合的效用补偿要求更高。  
  - **效用排序**：U=10 > U=5 > U=0，验证上文“无差异曲线越远离原点效用越高”的连续性。  
- **切点隐含最优解**：  
  - 虽图中未标切点，但根据上文“无差异曲线-预算线分析”，最优组合需满足：  
    $$
    \text{预算线斜率} = \frac{r_m - r_f}{\sigma_m} = \text{MRS（边际替代率）} = \frac{du/d\sigma_x}{du/dr_x}
    $$  
  - 该点即 **效用最大化组合**，首次将上文理论中的“求解最优 $ x $”转化为可视化均衡点。  

#### 3. **资产比较的逻辑深化**  
- 习题 (e) 利用预算线**斜率作为基准**评估新资产：  
  - 市场基准斜率 $ \frac{r_m - r_f}{\sigma_m} = 1 $，代表当前资产组合的风险回报效率。  
  - **Asset A**：$ \frac{17\% - 10\%}{5\%} = 1.4 > 1 $，单位风险超额收益更高 → **Better**（因其预算线更陡峭，需更高效用曲线才能相切）。  
  - **Asset B**：$ \frac{30\% - 10\%}{25\%} = 0.8 < 1 $，单位风险超额收益更低 → **Worse**（沿当前预算线无法达到，需接受更低效用）。  
- 此分析**直接应用上文 CAPM 逻辑**：资产价值取决于 $ \frac{r - r_f}{\sigma} $，而非绝对收益率，呼应“风险调整后收益”是定价核心。  

---

> **关键连续性说明**：本图将上文公式 $ r_x = r_f + \frac{r_m - r_f}{\sigma_m} \sigma_x $ 转化为可操作分析工具——通过借贷扩展预算线、无差异曲线定位最优解、斜率基准量化资产偏好，完整串联“约束定义-偏好分析-资产比较”三环节，为后续 CAPM 在多资产场景的推导铺垫实证基础。

---
### Page/Slide 3



### 当前图片文字与公式提取  
#### 文字内容  
- Asset C with $ r_c = 11\% $ and $ \sigma_c = 1\% $. **Same.**  
- Asset D with $ r_d = 25\% $ and $ \sigma_d = 14\% $. **Better.**  
- (f) Suppose Ms. Lynch’s utility function has the form $ u(r_x, \sigma_x) = r_x - 2\sigma_x $. How much of her portfolio will she invest in the original risky asset? (You might want to graph a few of Ms. Lynch’s indifference curves before answering; e.g., graph the combinations of $ r_x $ and $ \sigma_x $ that imply $ u(r_x, \sigma_x) = 0,1,\ldots $). **She will not invest anything in the risky asset.**  
- 13.2 (3) Fenner Smith is contemplating dividing his portfolio between two assets, a risky asset that has an expected return of 30% and a standard deviation of 10%, and a safe asset that has an expected return of 10% and a standard deviation of 0%.  
  - (a) If Mr. Smith invests $ x $ percent of his wealth in the risky asset, what will be his expected return? $ r_x = 30x + 10(1 - x) $.  
  - (b) If Mr. Smith invests $ x $ percent of his wealth in the risky asset, what will be the standard deviation of his wealth? $ \sigma_x = 10x $.  
  - (c) Solve the above two equations for the expected return on Mr. Smith’s wealth as a function of the standard deviation he accepts. **The budget line is $ r_x = 2\sigma_x + 10 $.**  
  - (d) Plot this “budget line” on the graph below.  

#### 图表元素  
- **坐标轴**：  
  - 横轴：Standard deviation（范围 0–20），刻度标记 0, 5, 10, 15, 20。  
  - 纵轴：Expected return（范围 0–40），刻度标记 0, 10, 20, 30, 40。  
- **图线标签**：  
  - Budget line（虚线）。  
  - Optimal choice（切点标记）。  
  - Indifference curves（凸向原点的曲线，共两条）。  

---

### 图表解析（结合上文知识点）  
本图表是对上文风险-收益理论的**参数更新扩展**和**具体案例应用**，核心变化在于风险资产参数（$ r_m = 30\% $, $ \sigma_m = 10\% $ 代替上文 $ r_m = 20\% $, $ \sigma_m = 10\% $），导致市场风险价格斜率从 1 升至 2。以下聚焦变化含义：  

#### 1. **预算线斜率的变化与参数实证**  
- 上文定义预算线斜率 $ \frac{r_m - r_f}{\sigma_m} $ 为“市场风险价格”，**本图中参数代入得**：  
  $$
  \frac{30\% - 10\%}{10\%} = 2 \quad \Rightarrow \quad r_x = 2\sigma_x + 10
  $$  
  - **截距 $ r_f = 10\% $**：延续上文逻辑，$ \sigma_x = 0 $ 时收益等于无风险利率（点 (0,10)）。  
  - **斜率 = 2**：表示每承担 **1 单位组合标准差**，预期收益增加 **2 单位**（对比上文斜率为 1 时仅增 1 单位）。这反映本场景下风险定价更“昂贵”——单位风险需更高超额收益补偿，源于风险资产回报率 $ r_m $ 从 20% 升至 30%（$ r_f $ 保持不变）。  
- **图表延伸含义**：  
  - 预算线覆盖 $ \sigma_x \in [0, 10] $（对应 $ x \in [0,1] $），未展示借贷（$ x > 1 $）区域。这与上文“允许借贷扩展预算线”形成对比，**凸显本例仅限自有资金配置**（因 $ \sigma_x = 10x $，$ x \leq 1 $ 时 $ \sigma_x \leq 10 $），验证上文理论中“约束范围由 $ x $ 定义”的连续性。  
  - 例如，$ \sigma_x = 5 $ 时 $ r_x = 20 $（点 (5,20)），对应投资比例 $ x = 50\% $（$ \sigma_x = 10x \Rightarrow x = 0.5 $），直观呈现风险-收益的线性权衡。  

#### 2. **最优选择点的动态意义**  
- **切点定位**：  
  - 图中“Optimal choice”标记于 (5,20)，即预算线 $ r_x = 2\sigma_x + 10 $ 与无差异曲线切点。  
  - 此处 **边际替代率（MRS）等于预算线斜率**：  
    $$
    \text{MRS} = \frac{du/d\sigma_x}{du/dr_x} = 2 = \frac{r_m - r_f}{\sigma_m}
    $$  
    延续上文效用最大化条件，但**实际效用曲线族未指定**（与上文 U=0,5,10 不同），仅通过凸曲线示意风险厌恶者的偏好。  
- **与 Ms. Lynch 案例的对比**：  
  - 部分 (f) 中 $ u = r_x - 2\sigma_x $ 导致 MRS = 2，与预算线斜率相同，故效用沿预算线恒定（$ u = 10 $），最优解退化为 $ \sigma_x = 0 $（全配安全资产）。  
  - 但本图表展示的是 **MRS 递减的典型风险厌恶情形**（曲线凸性），故切点非端点，**强化上文“最优解取决于偏好与约束的共同作用”**——Ms. Lynch 例外因 MRS 恒定，而图中 investor 偏好使切点位于正风险区域。  

#### 3. **资产比较逻辑的深化应用**  
上文以市场斜率 $ \frac{r_m - r_f}{\sigma_m} $ 为基准评估资产（$ r_m = 20\% $ 时斜率为 1），**本图参数更新后基准升至 2**，直接解释 Asset C 和 D 的标注：  
- **Asset D ($ r_d = 25\% $, $ \sigma_d = 14\% $) → Better**：  
  $$
  \frac{r_d - r_f}{\sigma_d} = \frac{25\% - 10\%}{14\%} \approx 1.07 < 2 \quad \text{但图表隐含逻辑}
  $$  
  标注“Better”需结合上下文：因当前无其他资产比较，且 1.07 > 上文基准（1），**实际指相对于上文市场基准更高风险溢价**（但低于当前市场效率）。本图中其位于预算线下方（$ \sigma_d = 14 $ 时预算线要求 $ r_x = 38 $，实际 $ r_d = 25 < 38 $），故应属低效，标注可能为笔误或针对特定比较场景。  
- **Asset C ($ r_c = 11\% $, $ \sigma_c = 1\% $) → Same**：  
  $$
  \frac{r_c - r_f}{\sigma_c} = \frac{11\% - 10\%}{1\%} = 1 < 2
  $$  
  在预算线 $ \sigma_x = 1 $ 处要求 $ r_x = 12 $，但 $ r_c = 11 < 12 $，**明确低于效率前沿**，标注“Same”可能意指“与基准差异微小”，但实质为劣等资产。  
- **核心逻辑延续**：  
  > 资产价值取决于 $ \frac{r - r_f}{\sigma} $ 与当前市场基准 $ 2 $ 的比较，而非绝对收益。  
  > 此分析直接应用上文 CAPM 推导逻辑，但**参数更新后基准变化**，凸显理论对不同市场环境的适应性。  

---

### 知识连续性说明  
本图表实现三大关键延续：  
1. **预算线动态性**：从抽象公式 $ r_x = r_f + \frac{r_m - r_f}{\sigma_m} \sigma_x $ 演化为具体斜率 2 的实证绘制（$ r_m = 30\% $ 案例），验证“风险价格由资产参数定义”的上文理论。  
2. **最优解可视化**：切点 (5,20) 将上文 “MRS = 预算线斜率” 条件转化为直观均衡，补充 Ms. Lynch 例外案例的对比，阐明“偏好异质性决定最优配置”。  
3. **资产评估框架**：Asset C/D 的标注虽存歧义，但通过计算 $ \frac{r - r_f}{\sigma} $，重申上文“风险调整后收益是定价核心”的连续逻辑，为多资产组合决策奠基。  

> **关键差异点**：与上文 (e) 段中 $ r_m = 20\% $ 的 $ r_x = \sigma_x + 10 $ 不同，本图 $ r_x = 2\sigma_x + 10 $ 体现**参数变化对约束边界的直接影响**，证明理论可灵活适配不同市场条件。

---
### Page/Slide 4



### 当前图片解析

#### 1. 提取文字与公式
- **文本内容**：  
  - (e) If Mr. Smith’s utility function is \( u(r_x, \sigma_x) = \min\{r_x, 30 - 2\sigma_x\} \), then Mr. Smith’s optimal value of \( r_x \) is 20, and his optimal value of \( \sigma_x \) is 5. (Hint: You will need to solve two equations in two unknowns. One of the equations is the budget constraint.)  
  - (f) Plot Mr. Smith’s optimal choice and an indifference curve through it in the graph.  
  - (g) What fraction of his wealth should Mr. Smith invest in the risky asset? Using the answer to Part (a), we find an \( x \) that solves \( 20 = r_x = 30x + 10(1 - x) \). The answer is \( x = .5 \).  
  - 13.3 (2) Assuming that the Capital Asset Pricing Model is valid, complete the following table. In this table \( p_0 \) is the current price of asset \( i \) and \( Ep_1 \) is the expected price of asset \( i \) in the next period.  
  - 13.4 (2) Farmer Alf Alpha has a pasture located on a sandy hill... [truncated as per knowledge continuity; only relevant parts extracted].  
  - (a) One is located on low land that never floods. This pasture yields an expected return of $500 per year no matter what the weather is like. What is Alf Alpha’s expected rate of return on his total investment if he buys this pasture for his second pasture? 10%. What is the standard deviation of his rate of return in this case? 10%.  

- **公式**：  
  - 效用函数： \( u(r_x, \sigma_x) = \min\{r_x, 30 - 2\sigma_x\} \)  
  - 预算约束： \( r_x = 30x + 10(1 - x) = 20x + 10 \)  
  - 最优解方程： \( 20 = 20x + 10 \)  
  - 表格参数：  
    - \( r_i = \frac{Ep_1 - p_0}{p_0} \)  
    - CAPM 定价： \( r_i = r_f + \beta_i (r_m - r_f) \)  
  - CAPM 表格数据：  

    | \( r_f \) | \( r_m \) | \( r_i \) | \( \beta_i \) | \( p_0 \) | \( Ep_1 \) |
    |-----------|-----------|-----------|--------------|----------|----------|
    | 10        | 20        | 10        | 0            | 100      | 110      |
    | 10        | 20        | 25        | 1.5          | 100      | 125      |
    | 10        | 15        | 20        | 2            | 200      | 240      |
    | 0         | 30        | 20        | 2/3          | 40       | 48       |
    | 10        | 22        | 10        | 0            | 80       | 88       |

#### 2. 表格分析与上文知识连续性
当前图片无视觉图表，但 CAPM 表格【13.3 (2)】可视为动态化数据图表。结合【上文知识点总结】中的风险-收益权衡框架与资产比较逻辑，解读如下：

- **预算线参数的一致性与动态验证**：  
  - 案例 (e) 中，Mr. Smith 的预算约束 \( r_x = 20x + 10 \) 直接延续上文预算线公式 \( r_x = r_f + \frac{r_m - r_f}{\sigma_m} \sigma_x \)。  
    - 代入 \( \sigma_x = 10x \)（上文知识点中关键参数），得 \( r_x = 2\sigma_x + 10 \)，**斜率 2 与上文“当前市场基准 2”完全一致**，验证了风险价格（\( \frac{r_m - r_f}{\sigma_m} \)）由资产参数动态定义。  
  - 最优解 \( (r_x, \sigma_x) = (20, 5) \) 对应点 (5,20) 在上文分析的切点位置，但**偏好机制不同**：  
    - 上文 Ms. Lynch 案例（\( u = r_x - 2\sigma_x \)）因 MRS 恒定=2 导致退化解；  
    - 本案例效用函数 \( u = \min\{r_x, 30 - 2\sigma_x\} \) 产生角点最优解，**强化了“偏好异质性是决定最优配置的核心”**（上文知识点第 2 部分）。预算线斜率未变，但无差异曲线形态差异导致相同切点的经济逻辑不同，凸显约束与偏好的互动。

- **CAPM 表格对资产比较逻辑的深化**：  
  表格中每行数据体现不同市场参数下的资产定价，延续上文“资产价值取决于风险调整后收益”的核心逻辑：  
  - **市场基准动态变化**：上文知识点强调参数更新使基准从 1 升至 2（例如 \( r_m = 30\% \) 案例）。  
    - 此表格中，市场风险溢价 \( (r_m - r_f) \) 在行间动态变化（10, 5, 30, 12），**直接验证理论对不同市场环境的适应性**（上文知识点第 3 部分）。  
    - 例如第 3 行：\( r_m - r_f = 5 \)，远低于第 1 行（10），反映市场风险定价降低，资产 \( i \) 的公允收益 \( r_i = 20 \) 由系统性风险 \( \beta_i = 2 \) 支撑。  
  - **风险调整收益的比率一致性**：  
    - 上文以 \( \frac{r - r_f}{\sigma} \) 为指标比较资产（如 Asset C/D 分析）；  
    - 此表格改用 CAPM 的 \( \beta_i \) 作为风险度量，公式 \( \frac{r_i - r_f}{\beta_i} = r_m - r_f \) 本质相同：  
      - 第 2 行：\( \frac{25 - 10}{1.5} = 10 = r_m - r_f \)，表明该资产风险调整后收益与市场基准匹配；  
      - 第 5 行：\( \beta_i = 0 \) 时，\( r_i = r_f \)，对应上文“安全资产无风险溢价”的结论。  
    - **关键延续**：表格隐含的夏普比率 \( \frac{r_i - r_f}{\sigma_i} \)（虽未显式计算）在 CAPM 均衡下应与市场组合一致，**强化了“风险调整收益是定价核心”的统一逻辑**（上文知识点第 3 部分末句）。

- **13.4 (2)(a) 的补充意义**：  
  - 预期回报率 10%、标准差 10% 的结果，展示将无风险资产（低地牧场）纳入组合后，总风险下降（从原牧场标准差 $100 降至比例标准差 10%）。  
  - **直接呼应上文风险-收益权衡线性模型**：添加安全资产使组合沿预算线向左移动，降低 \( \sigma_x \) 但以降低 \( r_x \) 为代价，**实证了预算线斜率（风险价格）在资产配置中的指导性**（上文知识点第 1 部分）。

> **总结**：此图片通过 Mr. Smith 的具体优化问题（参数化预算约束）和 CAPM 表格（动态市场参数），将上文抽象的“风险-收益权衡”与“资产比较框架”实证化。无视觉图表，但表格数据动态演示了市场基准变化如何重塑资产定价，印证了理论对不同风险偏好和资产环境的鲁棒性，无缝延续了上文“理论灵活适配市场条件”的结论。

---
### Page/Slide 5



### 当前图片内容解析

#### 1. 文字与公式提取
- **页眉**：`NAME ________________ 179`  
- **问题 (b)**：  
  > Another pasture that he could buy is located on the very edge of the river. This gives very good yields in dry years but in wet years it floods. This pasture also costs $5,000. The expected return from this pasture is $500 and the standard deviation is $100. Every inch of rain below average means an extra $100 in profit and every inch of rain above average means another $100 less profit than average. If Alf buys this pasture and keeps his original pasture on the sandy hill, what is his expected rate of return on his total investment? **10%**. What is the standard deviation of the rate of return on his total investment in this case? **0%**.  
- **问题 (c)**：  
  > If Alf is a risk averter, which of these two pastures should he buy and why? **He should choose the second pasture since it has the same expected return and lower risk.**  

- **隐含公式**：  
  - 单个牧场预期回报率：\(\frac{\$500}{\$5,000} = 10\%\)  
  - 单个牧场回报率标准差：\(\frac{\$100}{\$5,000} = 2\%\)  
  - 总投资组合预期回报率：\(10\%\)（给定）  
  - 总投资组合回报率标准差：\(0\%\)（给定）  

---

#### 2. 数据含义解析与上文知识连续性
当前图片无视觉图表，但问题 (b) 和 (c) 提供的**组合风险归零**场景是上文风险-收益权衡框架的动态验证，直接衔接 **13.4 (2)(a)** 的逻辑延伸。以下结合上文知识点提炼关键连续性：

- **风险分散机制的实证强化**：  
  - 单个牧场（河岸牧场）回报与降雨负相关（`rain below average → +$100 profit`，`rain above average → -$100 profit`），而“sandy hill”原牧场隐含正相关（未明述但由总风险归零反推）。  
  - **组合后 \(\sigma = 0\)** 证明资产间**完美负相关**（相关系数 \(\rho = -1\)），将原本有风险的单个资产转化为**无风险组合**。  
  - **呼应上文**：延续上文 **13.4 (2)(a)** 中“将无风险资产纳入组合后总风险下降”的核心，但此处非添加外部安全资产，而是通过**内部资产对冲**实现风险消除。验证了风险价格逻辑：  
    - 预算线斜率（风险价格）在组合中体现为风险调整的等效性。当 \(\sigma_x \to 0\)，组合移动至预算线最左端（无风险点），与上文“安全资产无风险溢价”结论一致。  
    - 总回报率 \(10\%\) 且 \(\sigma = 0\) 时，该回报率等价于无风险利率，**直接强化 CAPM 中 \(r_i = r_f\)（当 \(\beta_i = 0\)）的均衡条件**（见上文知识点 CAPM 表格第 5 行）。

- **风险-收益权衡的动态演示**：  
  - 河岸牧场单独持有时：\(\text{风险调整收益} = \frac{10\% - r_f}{2\%}\)（假设 \(r_f\) 为无风险利率），但组合后风险归零，使相同预期回报的效用最大化。  
  - **无缝衔接上文偏好分析**：对比上文 Ms. Lynch（\(u = r_x - 2\sigma_x\)）的退化解与 Mr. Smith（\(u = \min\{r_x, 30 - 2\sigma_x\}\)）的角点解，此处风险厌恶者（Alf）选择**相同回报下零风险资产**：  
    - 体现“偏好异质性是决定最优配置的核心”（上文知识点第 2 部分）。  
    - 该决策使无差异曲线在预算线最左端（无风险点）达到切点，印证“约束与偏好的互动决定均衡”。

- **对资产比较逻辑的深化**：  
  - 河岸牧场与原牧场单独风险相同（标准差 $100），但组合后风险消除，说明**资产价值取决于系统性风险（\(\beta\)）而非个体波动**。  
  - **直指CAPM核心**：异质资产通过负相关对冲，使组合 \(\beta = 0\)，故 \(r_i = r_f = 10\%\)，与上文 CAPM 表格中 \(\beta_i = 0\) 时 \(r_i = r_f\) 的定价规则完全一致。  
  - 隐含夏普比率：单个资产夏普比率 \(\frac{10\% - r_f}{2\%}\) 低于市场基准，但组合后因风险消除，其实际风险调整收益趋近无穷，**支撑上文“风险调整收益是定价唯一依据”的统一逻辑**。

> **总结**：此场景将上文理论转化为具体决策案例——资产组合通过风险对冲实现 \( (\sigma_x, r_x) = (0, 10\%) \) 的无风险点，实证了预算线斜率（市场风险价格）在动态环境中的指导性。它延续了“风险-收益权衡”的分析框架，同时凸显偏好（风险厌恶）与资产结构共同定义最优解，无缝呼应上文“理论灵活适配市场条件”的结论。

---
### Page/Slide 6



# 风险资产章节页码解析

## 1. 图片文字提取
- `180 RISKY ASSETS (Ch. 13)`

## 2. 与上文知识点的内在关联

此页码标识直接定位到教材第13章"风险资产"的核心内容，与上文知识点形成**结构性呼应**：

- **章节定位连续性**：  
  页码180印证了上文知识点涉及的正是本章核心案例——通过牧场投资组合验证风险对冲机制。该页码标志着资产组合风险分析理论的实证阶段（对应上文 **13.4 (2)(a)** 部分），衔接CAPM模型应用场景。

- **理论框架印证**：  
  "RISKY ASSETS"标题页揭示本章核心课题：如何将微观风险偏好与宏观资产定价统一。此定位完美对应上文总结的**风险-收益权衡刚性**（预算线斜率=市场风险价格）和**风险消除机制**（ρ=-1时σ=0）。

- **知识体系构建**：  
  该页码暗示后续内容将展开：
  - 单资产风险定价 → 上文隐含公式中10%预期回报率的理论依据
  - 资产间相关性度量 → 河岸牧场与"sandy hill"牧场的负相关验证
  - 无风险组合构建 → 解释上文"总风险归零"的数学条件

> 此页码非孤立标识，而是将上文具体案例（牧场投资）置于"风险资产"理论框架的**定位锚点**，表明所讨论的牧场组合策略正是本章系统性理论在实践中的典型应用。这与上文总结中"风险-收益权衡的动态演示"形成逻辑闭环。
