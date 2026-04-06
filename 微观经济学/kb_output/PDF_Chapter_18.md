# PDF_Chapter_18

### Page/Slide 1



### 1. 提取文字与公式

**文字内容：**  
- **章节标题**: Chapter 18 Technology  
- **引言**:  
  - 本章研究生产函数，将企业产量与投入联系起来。生产理论与效用理论结构相似：  
    - 效用理论中，无差异曲线是满足相同效用的商品束轨迹；生产理论中，等产量线是满足相同产量的投入组合轨迹。  
    - 无差异曲线斜率为边际替代率 $ MU_1/MU_2 $，等产量线斜率为边际技术替代率 $ MP_1/MP_2 $。  
  - **核心差异**：效用函数在单调变换下唯一，但生产函数的单调变换会改变技术描述。  
- **例子-生产函数唯一性**：  
  - 两家企业生产函数分别为 $ f(x_1, x_2) = x_1 + x_2 $ 和 $ f^*(x_1, x_2) = (x_1 + x_2)^2 $。  
  - 当输入组合 $ (x_1, x_2) = (1,1) $ 时，产量分别为 2 和 4，说明技术不同。  
- **规模报酬分析**：  
  - 定义：若所有投入乘以 $ t > 1 $：  
    - 产出乘以 $ > t $：规模报酬递增；  
    - 产出乘以 $ = t $：规模报酬不变；  
    - 产出乘以 $ < t $：规模报酬递减。  
  - 例子：生产函数 $ f(x_1, x_2) = x_1^{1/2} x_2^{3/4} $ 的规模报酬计算。

**公式：**  
1. 生产函数对比：  
   $$
   f(x_1, x_2) = x_1 + x_2, \quad f^*(x_1, x_2) = (x_1 + x_2)^2
   $$  
2. 规模报酬计算：  
   $$
   f(tx_1, tx_2) = (tx_1)^{1/2}(tx_2)^{3/4} = t^{5/4} x_1^{1/2} x_2^{3/4} = t^{5/4} f(x_1, x_2)
   $$

---

### 2. 核心概念解析

#### （1）生产函数与效用函数的本质差异  
- **效用函数**：仅需保持偏好排序，单调变换（如平方）不改变消费者选择（例如 $ U $ 与 $ U^* $ 生成相同无差异曲线）。  
- **生产函数**：**直接描述技术能力**，单调变换会改变产量的绝对值（如 $ f^* $ 在输入 $ (1,1) $ 时产出为 4，而非 $ f $ 的 2），因此代表**不同技术**。

#### （2）规模报酬的数学判定  
- 对生产函数 $ f(x_1, x_2) = x_1^a x_2^b $，若 $ a + b > 1 $，则规模报酬递增；  
  - 本例中 $ a = 1/2 $, $ b = 3/4 $，故 $ a + b = 5/4 > 1 $，验证递增性质。  
- **关键逻辑**：产出对投入的弹性 $ a + b $ 决定规模效应：  
  - 弹性 $ >1 $：扩大生产时，单位投入的边际产出递增（如技术协同效应）；  
  - 弹性 $ =1 $：产出与投入同比例变化（如线性生产函数）；  
  - 弹性 $ <1 $：边际产出递减（如资源限制下的生产）。  

#### （3）等产量线斜率的经济含义  
- 等产量线斜率 $ |MRTS| = MP_1/MP_2 $ 反映**要素替代的边界条件**：  
  - $ MP_1 $ 与 $ MP_2 $ 分别为要素 $ x_1, x_2 $ 的边际产出；  
  - 斜率绝对值递减（凸性）隐含“边际技术替代率递减规律”，与消费者理论中的“边际替代率递减”逻辑一致。

---
### Page/Slide 2



# 解析当前图片

## 提取文字与公式

**文字内容**：  
- 示例：设生产函数为 $ f(x_1, x_2) = \min\{x_1, x_2\} $。则 $ f(tx_1, tx_2) = \min\{tx_1, tx_2\} = t \min\{x_1, x_2\} = t f(x_1, x_2) $。因此，当所有投入乘以 $ t $ 时，产出也乘以 $ t $。由此可知，该生产函数具有**规模报酬不变**。  
- 你将被要求判断：当增加单一要素投入而其他要素不变时，该要素的边际产量是增加还是减少。  
- 熟悉微积分者可知：边际产量是一阶偏导数；其变动取决于二阶导数符号（负、正或零）。  
- 示例：对于生产函数 $ f(x_1, x_2) = x_1^{1/2} x_2^{3/4} $，要素1的边际产量为 $ \frac{1}{2} x_1^{-1/2} x_2^{3/4} $，它是 $ x_1 $ 的递减函数；类似地，要素2的边际产量也随 $ x_2 $ 增加而减少。  
- 18.0 热身练习：计算边际产量与技术替代率。示例：$ f(x_1, x_2) = 2x_1 + \sqrt{x_2} $。  
  - $ x_1 $ 的边际产量：常数 2  
  - $ x_2 $ 的边际产量：$ \frac{1}{2\sqrt{x_2}} $  
  - 技术替代率（TRS）：$ -MP_1 / MP_2 = -4 \sqrt{x_2} $  

**公式**：  
1. $ f(x_1, x_2) = \min\{x_1, x_2\} $  
2. $ f(tx_1, tx_2) = t f(x_1, x_2) $  
3. $ f(x_1, x_2) = x_1^{1/2} x_2^{3/4} $  
4. $ MP_1 = \frac{1}{2} x_1^{-1/2} x_2^{3/4} $  
5. $ f(x_1, x_2) = 2x_1 + \sqrt{x_2} $  
6. $ MP_1 = 2 $  
7. $ MP_2 = \frac{1}{2\sqrt{x_2}} $  
8. $ TRS = -MP_1 / MP_2 = -4 \sqrt{x_2} $  

## 关键点解析

### （1）min生产函数的规模报酬特性  
该案例**补充上文规模报酬分类**：  
- 上文已通过 $ f = x_1^{1/2} x_2^{3/4} $（$ a+b=5/4>1 $）演示规模报酬递增，而此处 $ f = \min\{x_1, x_2\} $ 是**完美互补型技术**的典型例子。  
- 其规模报酬不变源于：投入必须严格1:1匹配（如机器与工人数），同比例扩张输入直接线性扩大产出。这与上文**核心差异**一致——生产函数直接描述技术约束，单调变换会改变产量绝对值（此处$ \min $函数保持比例关系）。  

### （2）边际产量递减的数学逻辑  
- 上文隐含**边际技术替代率递减**（等产量线凸性），此处明确其根源于**边际产量递减**：  
  - 边际产量的一阶导数定义（$ MP_i = \frac{\partial f}{\partial x_i} $）直接对应上文“等产量线斜率 $ |\text{MRTS}| = MP_1 / MP_2 $”。  
  - 通过二阶导数判断变动方向（如 $ f = x_1^{1/2} x_2^{3/4} $ 中 $ \frac{d MP_1}{d x_1} < 0 $），**解释了MRTS递减的微观机制**——要素替代能力随投入增加而衰减。  
- 此处强调：边际产量递减是**局部效应**（固定其他要素），而规模报酬是**全局效应**（所有要素同比例变化），二者无必然联系（如本例中min函数规模报酬不变，但单要素增加时MP可能突变为零）。  

### （3）线性-根号生产函数的生产特性  
$ f = 2x_1 + \sqrt{x_2} $ 为**不完全替代型技术**的代表：  
- **边际产量不对称性**：  
  - $ MP_1 = 2 $ 恒定 → $ x_1 $ 的完全替代性（体现为等产量线水平段）  
  - $ MP_2 = \frac{1}{2\sqrt{x_2}} $ 递减 → $ x_2 $ 边际贡献衰减  
  这延展了上文“要素替代边界”概念：替代可能性取决于边际产出变动方向。  
- **TRS的动态特征**：  
  $ TRS = -4 \sqrt{x_2} $ 随 $ x_2 $ 增大而**绝对值上升**，说明等产量线变得陡峭——为维持同一产量，每单位 $ x_2 $ 增加需用更多 $ x_1 $ 替代（与上文“MRTS递减规律”一致，但此处因 $ MP_1 $ 恒定而呈现单调变化）。  

> **知识连续性说明**：热身练习为后续章节（成本最小化与生产者选择）提供工具基础。上文已建立“等产量线-MRTS”框架，此处通过具体函数强化计算逻辑，尤其凸显**非微积分学习者的简化处理方式**（查表法），体现技术参数的实用价值。

---
### Page/Slide 3



### 提取图片文字与公式  
图片为标题“Marginal Products and Technical Rates of Substitution”的表格，内容如下：  

| $f(x_1, x_2)$                     | $MP_1(x_1, x_2)$                              | $MP_2(x_1, x_2)$                              | $TRS(x_1, x_2)$                                     |  
|-----------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------------|  
| $x_1 + 2x_2$                      | $1$                                           | $2$                                           | $-1/2$                                              |  
| $a x_1 + b x_2$                   | $a$                                           | $b$                                           | $-a/b$                                              |  
| $50 x_1 x_2$                      | $50 x_2$                                      | $50 x_1$                                      | $-x_2 / x_1$                                        |  
| $x_1^{1/4} x_2^{3/4}$             | $\frac{1}{4} x_1^{-3/4} x_2^{3/4}$           | $\frac{3}{4} x_1^{1/4} x_2^{-1/4}$           | $-x_2 / (3 x_1)$                                    |  
| $C x_1^a x_2^b$                   | $C a x_1^{a-1} x_2^b$                        | $C b x_1^a x_2^{b-1}$                        | $- (a x_2) / (b x_1)$                               |  
| $(x_1 + 2)(x_2 + 1)$              | $x_2 + 1$                                     | $x_1 + 2$                                     | $- (x_2 + 1) / (x_1 + 2)$                           |  
| $(x_1 + a)(x_2 + b)$              | $x_2 + b$                                     | $x_1 + a$                                     | $- (x_2 + b) / (x_1 + a)$                           |  
| $a x_1 + b \sqrt{x_2}$            | $a$                                           | $b / (2 \sqrt{x_2})$                         | $- (2 a \sqrt{x_2}) / b$                            |  
| $x_1^a + x_2^a$                   | $a x_1^{a-1}$                                 | $a x_2^{a-1}$                                 | $- (x_1 / x_2)^{a-1}$                               |  
| $(x_1^a + x_2^a)^b$               | $b a x_1^{a-1} (x_1^a + x_2^a)^{b-1}$       | $b a x_2^{a-1} (x_1^a + x_2^a)^{b-1}$       | $- (x_1 / x_2)^{a-1}$                               |  

---

### 表格内容解析（结合上文知识点）  
此表格系统归纳了**边际产量**（$MP_i$）和**技术替代率**（$TRS$）的计算结果，直接扩展了上文“18.0 热身练习”的工具性框架。关键点如下：  

#### 1. **$TRS$ 公式的统一性**  
   - 表格中所有 $TRS$ 行均满足 $TRS = -MP_1 / MP_2$，这延续了上文对等产量线斜率的定义（$|\text{MRTS}| = MP_1 / MP_2$）。  
   - 例如：  
     - 线性函数（第1–2行）：$TRS$ 为常数（$-1/2$ 或 $-a/b$），**解释上文所述“完全替代技术”特性**——等产量线为直线，替代能力恒定。  
     - Cobb-Douglas 函数（第4–5行）：$TRS = - (a/b) (x_2 / x_1)$，**印证上文点（3）的“动态替代特征”**。若 $x_2$ 增加，$|TRS|$ 增大，导致等产量线变陡（需更多 $x_1$ 替代 $x_2$ 以维持产量），与**边际产量递减的微观机制**一致。  

#### 2. **边际产量行为的实证分类**  
   - **恒定边际产量**（第1–2、8行）：  
     - $MP_1$ 为常数（如 $a x_1 + b \sqrt{x_2}$ 中 $MP_1 = a$），**对应上文热身练习的延伸**。此情形下，等产量线存在水平/垂直段（如第8行 $TRS$ 含 $\sqrt{x_2}$），体现要素1的完全替代性。  
   - **递减边际产量**（第3–5、9–10行）：  
     - $MP_1$ 或 $MP_2$ 随自身投入增加而递减（如 $x_1^{1/4} x_2^{3/4}$ 中 $MP_1 \propto x_1^{-3/4}$），**直接验证上文“边际产量递减的数学逻辑”**——二阶导数为负（$\partial^2 f / \partial x_i^2 < 0$）。  
     - 对于 CES 函数（第9–10行），$TRS = - (x_1 / x_2)^{a-1}$ 的形态取决于 $a$：若 $a < 1$，$|TRS|$ 随 $x_1/x_2$ 增加而减小，**强化上文“MRTS 递减导致等产量线凸性”**。  

#### 3. **与上文关键点的衔接**  
   - **规模报酬无关性**：表格仅聚焦局部效应（单一要素变动），**凸显上文点（2）的核心结论**——边际产量递减是“局部”特性（固定其他要素），与规模报酬无必然联系（例如，第5行 $C x_1^a x_2^b$ 的规模报酬由 $a+b$ 决定，但 $MP$ 递减仅取决于 $a, b < 1$）。  
   - **互补性技术验证**：第6–7行 $(x_1 + a)(x_2 + b)$ 型函数中，$MP_1$ 随 $x_2$ 增加而增大，**延伸“min 函数”逻辑**（上文点（1））——要素间存在互补依赖，但因非严格配对，边际产量非突变（对比 min 函数的阶跃特性）。  

> **知识连续性**：此表格为后续章节（成本最小化）提供即用型工具库。上文已建立“等产量线-MRTS”分析框架，此处通过函数分类（线性、Cobb-Douglas、CES 等），**将微观机制（如 MP 递减）转化为可操作参数**，尤其为非微积分学习者提供 TRS 计算的查表依据，进一步支撑“技术参数决定替代边界”的分析主线。

---
### Page/Slide 4



### 图片内容提取

#### 文字与公式
- **页眉**：232 TECHNOLOGY (Ch. 18)  
- **标题**：Returns to Scale and Changes in Marginal Products  
- **指令**：  
  > For each production function in the table below, put an $I$, $C$, or $D$ in the first column if the production function has increasing, constant, or decreasing returns to scale. Put an $I$, $C$, or $D$ in the second (third) column, depending on whether the marginal product of factor 1 (factor 2) is increasing, constant, or decreasing, as the amount of that factor alone is varied.  

- **表格内容**：
  | $f(x_1, x_2)$                 | Scale | $MP_1$ | $MP_2$ |
  |---------------------------------|-------|--------|--------|
  | $x_1 + 2x_2$                  | C     | C      | C      |
  | $\sqrt{x_1} + 2x_2$           | D     | D      | D      |
  | $.2x_1x_2^2$                   | I     | C      | I      |
  | $x_1^{1/4}x_2^{3/4}$          | C     | D      | D      |
  | $x_1 + \sqrt{x_2}$            | D     | C      | D      |
  | $(x_1 + 1)^{.5}(x_2)^{.5}$    | D     | D      | D      |
  | $\left(x_1^{1/3} + x_2^{1/3}\right)^3$ | C | D | D |

- **习题 18.1**：  
  > Prunella raises peaches. Where $L$ is labor and $T$ is land, her output is $f(L, T) = L^{1/2}T^{1/2}$.  
  > (a) Points on the isoquant for 4 bushels satisfy $T = 16/L$.

---

### 关键解析（结合上文知识点）

#### 1. **规模报酬与边际产量的解耦验证**
表格通过 **I/C/D 分类** 直接验证了上文核心结论：**边际产量递减是局部特性，与规模报酬无必然联系**。具体体现：
- **Cobb-Douglas 案例**（$x_1^{1/4}x_2^{3/4}$）：  
  - 规模报酬为 **C**（指数和 $1/4+3/4=1$），但 $MP_1, MP_2$ 均为 **D**（因 $1/4<1, 3/4<1$）。  
  - 与上文“规模报酬由 $a+b$ 决定，边际产量递减仅取决于 $a,b<1$”完全一致。  
- **CES 函数案例**（$\left(x_1^{1/3} + x_2^{1/3}\right)^3$）：  
  - 规模报酬 **C**（齐次性为 1），但 $MP_1, MP_2$ 均为 **D**。  
  - 延续上文“CES 函数中 $a<1$ 时 $|TRS|$ 递减”，解释等产量线凸性来源。  
- **反例 $.2x_1x_2^2$**：  
  - 规模报酬 **I**（指数和 $1+2=3>1$），但 $MP_1 = \text{C}$（固定 $x_2$ 时 $MP_1$ 为常数），$MP_2 = \text{I}$（固定 $x_1$ 时 $MP_2$ 递增）。  
  - 突破“规模报酬与边际产量同步变动”的直觉，凸显局部效应与全局性质的分离。

#### 2. **边际产量分类的微观机制分类**
表格对 **$MP_1/MP_2$** 的分类是对上文“边际产量行为实证分类”的结构化延伸：
- **恒定边际产量**（$x_1 + 2x_2$ 和 $x_1 + \sqrt{x_2}$ 的 $MP_1$）：  
  - $MP_1 = C$ 对应 **完全替代技术**（上文第1–2行线性函数），但 $x_1 + \sqrt{x_2}$ 的 $MP_2 = D$ 引入非对称递减，体现部分互补性。  
- **递减边际产量**（多数案例）：  
  - $\sqrt{x_1} + 2x_2$ 和 $(x_1 + 1)^{.5}(x_2)^{.5}$ 中 $MP_1, MP_2 = D$，与上文“二阶导数为负”数学逻辑一致。  
  - $\sqrt{x_1} + 2x_2$ 的 **D 规模报酬** 源于 $x_1$ 的根号弱化其贡献，强化“要素替代效率随投入递减”的行为逻辑。

#### 3. **对习题 18.1 的延伸解释**
- **生产函数 $f(L,T) = L^{1/2}T^{1/2}$**：  
  - 属于 Cobb-Douglas 类型（上文第4行扩展），规模报酬 **C**，$MP_L = \frac{1}{2}L^{-1/2}T^{1/2}$ 和 $MP_T$ 均 **D**。  
  - 等产量线 $T = 16/L$ 直接导出 **TRS**：  
    $$
    \text{TRS} = -\frac{MP_L}{MP_T} = -\frac{T}{L} \quad \Rightarrow \quad T = \text{constant} \cdot L^{-1}
    $$  
    与上文“Cobb-Douglas 的 $|TRS|$ 随 $L$ 增加而减小”一致，验证等产量线凸向原点。

> **知识衔接**：本表格将生产函数分类与**规模报酬定义**（上文未明确定义）及**边际产量动态**显式关联，弥补上文“仅分析 TRS 与 MP 比值”的空白。通过 I/C/D 标签系统化呈现“技术参数如何决定要素回报趋势”，为成本最小化中“要素最优配置”的参数化分析奠定基础（例如：若 $MP_i = I$，则成本曲线可能存在下凸段）。

---
### Page/Slide 5



### 1. 文字与公式提取  
#### 文字内容：  
- 图片顶部：`NAME _______ 233`  
- 第一个图表下方：  
  > (b) This production function exhibits (constant, increasing, decreasing) returns to scale. **Constant returns to scale**.  
- (c) 部分：  
  > In the short run, Prunella cannot vary the amount of land she uses. On the graph below, use blue ink to draw a curve showing Prunella’s output as a function of labor input if she has 1 unit of land. Locate the points on your graph at which the amount of labor is 0, 1, 4, 9, and 16 and label them. The slope of this curve is known as the marginal **product** of **labor**. Is this curve getting steeper or flatter as the amount of labor increase? **Flatter**.  

#### 图表信息：  
- **上图（L-T坐标系）**：  
  - 横轴 $L$（0–16），纵轴 $T$（0–8）；  
  - 曲线为 $T = 16/L$（习题 18.1(a) 中 4 bushels 的等产量线）；  
  - 标注点：$(L,T) = (2,8),\ (4,4),\ (8,2),\ (16,1)$。  
- **下图（Labour-Output坐标系）**：  
  - 横轴 `Labour`（0–16），纵轴 `Output`（0–8）；  
  - `Blue line`：短期总产量曲线（$T=1$ 时 $f(L) = \sqrt{L}$）；  
  - `Red line`：疑似另一土地量下的总产量曲线；  
  - `Red MPL line`：边际产量曲线；  
  - 标注点：$L = 0,1,4,9,16$ 对应 $f(L) = 0,1,2,3,4$。  

---

### 2. 图表解析（基于上文知识点）  
#### (1) 上图：等产量线 $T = 16/L$  
- **含义**：此曲线为习题 18.1(a) 中产出 $f(L,T) = L^{1/2}T^{1/2} = 4$ 的轨迹，满足 $LT = 16$。  
- **结合上文**：  
  - 上文指出 Cobb-Douglas 生产函数 $f(L,T) = L^{1/2}T^{1/2}$ 属于**规模报酬不变**（C）类型（指数和 $1/2+1/2=1$），且 $MP_L$、$MP_T$ 均为**递减**（D）。  
  - 等产量线**凸向原点**，直接反映 $|TRS| = T/L$ 随 $L$ 增加而递减（如上文关键解析所述）。图中曲线斜率从 $L=2$ 处的陡峭（$|TRS|=4$）逐渐变缓（$L=16$ 处 $|TRS|=1/16$），验证了“边际替代率递减”源于要素边际产量递减的机制。  

#### (2) (b) 选项与结果：规模报酬判断  
- **“Constant returns to scale”**：  
  - 与上文对 Cobb-Douglas 函数的分析一致：当 $f(tL,tT) = t^k f(L,T)$ 时，$k=1$ 即 CRS。此处 $f(tL,tT) = (tL)^{1/2}(tT)^{1/2} = t \cdot f(L,T)$，故 $k=1$。  
  - 延续上文知识衔接：**规模报酬属于全局性质**（与投入成比例变化相关），而 $MP$ 递减是局部特性（固定一要素变另一要素），二者解耦（如 $\left(x_1^{1/3} + x_2^{1/3}\right)^3$ 规模报酬为 C 但 $MP$ 仍递减）。  

#### (3) 下图：短期总产量曲线（$T=1$ 固定时）  
- **Blue line 行为**：  
  - 函数为 $f(L,1) = \sqrt{L}$，代入 $L=0,1,4,9,16$ 得 $f(L)=0,1,2,3,4$，与图中标注点一致。  
  - 曲线斜率（即 $MP_L = \frac{d}{dL}\sqrt{L} = \frac{1}{2\sqrt{L}}$）随 $L$ 增加而**递减**（例如：$L=1$ 时 $MP_L=0.5$，$L=16$ 时 $MP_L=0.125$），导致曲线逐渐**变平缓**（答案 “Flatter”）。  
- **结合上文**：  
  - 上文关键解析强调：**边际产量递减直接决定短期总产量曲线的凸性**。此处 $MP_L = \frac{1}{2}L^{-1/2}$ 满足 $MP_L$ 的一阶导数为负（$MPL$ 递减），与上文“Cobb-Douglas 中 $a<1$ 时 $MP_i$ 递减”逻辑一致。  
  - 图中 `Red MPL line` 递减趋势进一步验证：当 $T$ 固定时，**劳动的边际产量递减是要素替代效率衰减的微观表征**（与上文“部分互补性”中 $MP$ 递减的机制相同）。  

#### (4) 短期成本最小化的隐含联系  
- 上文指出“若 $MP_i = I$，则成本曲线可能存在下凸段”。而此处 $MP_L = D$，意味着**短期边际成本递增**（因 $MC = w/MP_L$，$MP_L$ 递减导致 $MC$ 递增），为后续成本分析提供图像依据。  

> **知识延续**：本图通过短期总产量曲线，将上文“边际产量递减”的理论结论转化为**可观察的几何形态**（曲线变平缓），直接验证了“Cobb-Douglas 参数决定局部要素回报趋势”的核心机制，并为理解“为什么等产量线凸向原点”提供了动态视角。

---
### Page/Slide 6



### 1. 提取文字与公式  
#### (d) 段落  
- **文字**：  
  "Assuming she has 1 unit of land, how much extra output does she get from adding an extra unit of labor when she previously used 1 unit of labor? $\sqrt{2} - 1 \approx .41$. 4 units of labor? $\sqrt{5} - 2 \approx .24$. If you know calculus, compute the marginal product of labor at the input combination (1,1) and compare it with the result from the unit increase in labor output found above."  
- **公式**：  
  $$
  \text{Derivative is } \frac{1}{2\sqrt{L}}, \quad \text{so the MP is } .5 \text{ when } L = 1 \text{ and } .25 \text{ when } L = 4.
  $$

#### (e) 段落  
- **文字**：  
  "In the long run, Prunella can change her input of land as well as of labor. Suppose that she increases the size of her orchard to 4 units of land. Use red ink to draw a new curve on the graph above showing output as a function of labor input. Also use red ink to draw a curve showing marginal product of labor as a function of labor input when the amount of land is fixed at 4."  

#### 18.2(0) 部分  
- **生产函数**：  
  $f(x_1, x_2) = \min\{x_1, x_2\}$  
- **关键数值与描述**：  
  - $x_1 < x_2$ 时：  
    - $MP_{x_1} = 1$（remains constant）  
    - $MP_{x_2} = 0$（remains constant）  
    - $TRS = \text{infinity}$  
    - Returns to scale: **constant**  
  - $x_1 = x_2 = 20$ 时：  
    - $MP_{x_1} = 0$，$MP_{x_2} = 0$  
    - $MP_{x_1}$ **increases** if $x_2$ increases slightly  

#### Calculus 18.3(0) 部分  
- **生产函数**：  
  $f(x_1, x_2) = x_1^{1/2} x_2^{3/2}$  
- **公式**：  
  $$
  MP_{x_1} = \frac{1}{2} x_1^{-1/2} x_2^{3/2}
  $$  

---

### 2. 图表关联与知识延续  
#### (1) 问题 (d) 与短期边际产量  
- **核心验证**：  
  计算 $\Delta L =1$ 时的边际产出（$\sqrt{2}-1 \approx 0.41$ 和 $\sqrt{5}-2 \approx 0.24$）与微分结果（$MP_L = \frac{1}{2\sqrt{L}}$）**严格对应上文结论**：  
  - 当 $L=1$ → $MP_L = 0.5$（理论值），实际离散增量 $0.41$ 因 $\Delta L=1$ 为有限变化，符合 $MP$ 递减的连续性。  
  - $L=4$ → $MP_L = 0.25$，进一步验证 $MP_L \downarrow$ 的速度（比离散增量 $0.24$ 略高），说明**总产量曲线凸性源于 $MP$ 递减的非线性**。  
- **几何关联**：  
  此处数值直接对应下图中 `Blue line` 的斜率变化：$L$ 从 1→4 时，曲线斜率从 $0.5$ 降至 $0.25$，解释“**曲线逐渐变平缓（Flatter）**”的直观来源。

#### (2) 问题 (e) 与土地扩张的短期效应  
- **隐含曲线特性**：  
  - **总产量曲线（Red line）**：当 $T=4$ 时，$f(L) = \sqrt{4L} = 2\sqrt{L}$，几何上为 `Blue line` 的垂直拉伸（如 $L=4$ 时输出从 2→4）。其斜率 $MP_L = \frac{1}{\sqrt{L}}$ 比 $T=1$ 时更大（例如 $L=4$ 时 $MP_L=0.5$ vs 原 $0.25$），导致新曲线**起始更陡峭**，但依然因 $MP_L \downarrow$ 而逐渐平缓。  
  - **Red MPL line 对应位置**：$T=4$ 时的 $MP_L$ 曲线与 `Red MPL line` 重合，表明**土地增加仅提升边际产量水平，不改变递减规律**（与上文“规模报酬 vs 边际报酬”解耦逻辑一致）。  

#### (3) 18.2(0) 与生产技术对比  
- **固定比例技术**（$f=\min\{x_1,x_2\}$）揭示：  
  - **等产量线形态**：直角 L 形（上图中不存在此类曲线），说明**无连续替代可能**（$TRS=\infty$）。  
  - **与 Cobb-Douglas 核心差异**：  
    - $x_1 \neq x_2$ 时 $MP$ 为常数（而非递减），直接导致**总产量曲线分段线性**（非凸向原点）；  
    - 仅在 $x_1=x_2$ 处 $MP=0$，体现“瓶颈约束”的离散跳跃，与上文“要素互补性”形成极限情况对照。  

#### (4) 18.3(0) 与 Cobb-Douglas 扩展  
- **参数化验证**：  
  - $MP_{x_1} = \frac{1}{2} x_1^{-1/2} x_2^{3/2}$ 明确显示：  
    - $MP_{x_1}$ 随 $x_1$ 递增而递减（指数 $-1/2 <0$）；  
    - 随 $x_2$ 递增而递增（指数 $3/2 >0$），**与上文“土地增加推升劳动边际产出”完全一致**。  
  - 若 $x_2$ 固定，此式回归为 $MP_L$ 关于 $L$ 的递减函数，为分析短期生产提供更一般化的公式基础。  

> **知识延续**：图像通过具体数值（如 $MP_L=0.5$ at $L=1$）和代数表达式（$1/(2\sqrt{L})$）**将上文抽象结论落地为可计算的微观证据**，同时引入固定比例技术与高阶 Cobb-Douglas 案例，**完善“要素互动”的连续谱分析**：从完全互补（18.2）到连续替代（18.1），再到参数推广（18.3）。

---
### Page/Slide 7



### 提取内容  
当前图片中的文字与公式如下：  

#### (b)  
- 文字：*The marginal product of $x_1$ (increases, decreases, remains constant) **decreases** for small increases in $x_1$, holding $x_2$ fixed.*  

#### (c)  
- 公式：$\frac{3}{2} x_1^{1/2} x_2^{1/2}$  
- 文字：*The marginal product of factor 2 is $\frac{3}{2} x_1^{1/2} x_2^{1/2}$, and it (increases, remains constant, decreases) **increases** for small increases in $x_2$.*  

#### (d)  
- 文字：*An increase in the amount of $x_2$ (increases, leaves unchanged, decreases) **increases** the marginal product of $x_1$.*  

#### (e)  
- 公式：$-\frac{x_2}{3x_1}$  
- 文字：*The technical rate of substitution between $x_2$ and $x_1$ is $-\frac{x_2}{3x_1}$.*  

#### (f)  
- 文字：*Does this technology have diminishing technical rate of substitution? **Yes**.*  

#### (g)  
- 文字：*This technology demonstrates (increasing, constant, decreasing) **increasing** returns to scale.*  

#### 18.4 (0)  
- 生产函数：$f(K, L) = \frac{L}{2} + \sqrt{K}$  
  - (a) 文字：*There are (constant, increasing, decreasing) **decreasing** returns to scale. The marginal product of labor is **constant** (constant, increasing, decreasing).*  
  - (b) 文字：*In the short run, capital is fixed at 4 units. Labor is variable. On the graph below, use blue ink to draw output as a function of labor input in the short run. Use red ink to draw the marginal product of labor as a function of labor input in the short run. The average product of labor is defined as total output divided by the amount of labor input. Use black ink to draw the average product of labor as a function of labor input in the short run.*  

---

### 图表含义解析（基于上文知识点延续）  
当前图片中无实际图表，但18.4(b)要求绘制资本固定（$K=4$）时的短期生产曲线。结合**上文知识点总结**中对短期生产的系统分析（尤其是问题(d)与(e)的几何关联），此处推导并解释预期图表行为：  

#### 核心生产函数推导  
- 固定 $K=4$ 时：  
  $$
  f(L) = \frac{L}{2} + \sqrt{4} = \frac{L}{2} + 2
  $$  
  由此：  
  - **总产量（TP）**：$TP(L) = \frac{L}{2} + 2$ → 线性函数（斜率恒为 $0.5$）  
  - **边际产量（MPL）**：$MP_L = \frac{d(TP)}{dL} = \frac{1}{2}$ → 常数  
  - **平均产量（APL）**：$AP_L = \frac{TP(L)}{L} = \frac{1}{2} + \frac{2}{L}$ → 随 $L$ 增加而递减，趋近于 $0.5$  

#### 与上文知识点的连续性解析  
1. **边际产量行为**：  
   - 当前18.4(a)中 $MP_L$ **constant** 与上文**Cobb-Douglas生产函数（如 $f = \sqrt{L}$）** 形成关键对比：  
     - 上文18.1/18.3中，$MP_L = \frac{1}{2\sqrt{L}}$ 递减（导致总产量曲线**凸性**，如上文提及 "曲线逐渐变平缓"）；  
     - 本例 $MP_L$ 常数 → 总产量为**直线**（无凸性），验证上文隐含的逻辑：**仅当 $MP$ 递减时，总产量曲线才凸向原点**。此差异凸显要素技术特性（如线性 vs. Cobb-Douglas）如何决定产量曲线形态。  
   - 直接呼应上文 "规模报酬 vs 边际报酬" 解耦原则：  
     - 递减规模报酬（18.4a中 **decreasing**）与 $MP_L$ **constant** 共存 → 说明规模报酬由所有投入同比例变化决定，而边际报酬仅关注单一投入变动，二者独立（如上文 "土地增加仅提升边际产量水平，不改变递减规律" 的逆向案例）。  

2. **短期曲线几何特性**（预期绘图结果）：  
   - **蓝色线（TP）**：从 $(L=0, TP=2)$ 开始的直线，斜率恒为 $0.5$。  
     - 与上文Cobb-Douglas的"凸形曲线"不同：上文因 $MP$ 递减导致斜率下降（如 $L=1$ 时斜率 $0.5$，$L=4$ 时 $0.25$），而本例**斜率不变**，实证 **"线性生产函数使总产量无边际递减效应"**。  
   - **红色线（MPL）**：水平线 $y = 0.5$。  
     - 对比上文Cobb-Douglas的"递减MPL曲线"：上文提及 $MP_L \downarrow$ 导致曲线平缓化，而本例**MPL无变动**，说明**当生产函数含线性项时，边际报酬不递减**（如上文固定比例技术的"分段线性"的简化延续）。  
   - **黑色线（APL）**：从 $L \to 0^+$ 时 $AP_L \to +\infty$ 递减至渐近线 $y=0.5$。  
     - 与上文MPL曲线关联：APL始终在MPL上方递减，且与MPL在 $L \to \infty$ 时重合——这延续了上文隐含的**平均-边际关系**（如问题(e)中土地扩张仅平移曲线，不改变MPL递减规律；本例无递减，故APL仅收敛于恒定MPL）。  

3. **扩展知识连续性**：  
   - 从"要素互补连续谱"视角：  
     - 上文18.2的固定比例技术（完全互补，$TRS=\infty$） → 上文18.3的Cobb-Douglas（连续替代，$MP$ 递减） → **本例18.4（劳动完全替代，资本固定时线性生产）**。  
     - 本例 $MP_L$ 常数体现**劳动要素的无限可替代性**（与上文Cobb-Douglas中 $MP_L$ 随 $L$ 增加而递减形成端点对比），完善了"技术替代弹性"的连续范围分析。  
   - 18.4(g)中 **increasing returns to scale** 与 (e) 的 $TRS$ 公式 $-\frac{x_2}{3x_1}$ 结合：  
     - $TRS$ 递减（18.4(f) 为 **Yes**） → 等产量线凸向原点，但**规模报酬递增**（如上文18.3的扩展） → 说明 $TRS$ 递减仅保证单一投入变动的边际递减，不影响所有投入同比例变化的整体效率。  

> **关键延续点**：本例将上文"边际产量递减的非线性"（18.3）与"要素互补极限"（18.2）统一于一个**线性-非线性混合技术**框架，证实：**短期MPL是否递减取决于生产函数中该要素的幂次（线性项→常数MP；分数幂→递减MP）**，而上文数值验证（如 $\Delta L=1$ 时离散增量≈微分结果）在此处退化为精确相等（因 $MP_L$ 恒定）。

---
### Page/Slide 8



### 图表解析：线性生产函数的短期产出曲线  
基于【上文知识点总结】（18.4节），当前图片中的图表对应**固定资本下的短期生产函数**，其中劳动（Labour）为唯一可变投入。图表标注与上文推导完全一致，以下仅针对图表内容进行精确解析，不重复上文已述结论，但延续技术特性逻辑。

#### 1. 文字与公式提取  
- **页面信息**：`236 TECHNOLOGY (Ch. 18)`  
- **图表标注**：  
  - y轴：`Fragiles`（实际指**产出量**，上文18.4中称为"Frages"或"产出"，此处为术语变体）  
  - x轴：`Labour`  
  - 曲线标签：`Blue line`（蓝线）、`Black line`（黑线）、`Red line`（红线）  
- **问题文本**（18.5节，但与图表无直接关联）：  
  > `18.5 (0) General Monsters Corporation has two plants for producing juggernauts, one in Flint and one in Inkster. The Flint plant produces according to \( f_F(x_1, x_2) = \min\{x_1, 2x_2\} \) and the Inkster plant produces according to \( f_I(x_1, x_2) = \min\{2x_1, x_2\} \), where \( x_1 \) and \( x_2 \) are the inputs.`  
  > `(a) On the graph below, use blue ink to draw the isoquant for 40 juggernauts at the Flint plant. Use red ink to draw the isoquant for producing 40 juggernauts at the Inkster plant.`  
- **关键公式**（源于上文18.4，图表直接体现）：  
  \[
  TP(L) = \frac{L}{2} + 2, \quad MP_L = \frac{1}{2}, \quad AP_L = \frac{1}{2} + \frac{2}{L}
  \]

#### 2. 图表变化含义解析  
图表为**短期生产曲线图**，基于上文线性生产函数 \( TP(L) = \frac{L}{2} + 2 \) 绘制。结合上文知识点，重点说明曲线几何特性的技术含义，避免重复推导。

- **蓝线（TP曲线）**：  
  从 \((L=0, TP=2)\) 起始的直线，斜率恒为 \(0.5\)（如 \(L=0\) 到 \(L=12\) 时，\(TP\) 从 \(2\) 增至 \(8\)，\(\Delta TP / \Delta L = 0.5\)）。  
  **含义**：与上文Cobb-Douglas函数（如 \(TP = \sqrt{L}\)）的凸形曲线形成反例——**当生产函数对劳动为线性时（即劳动幂次=1），边际产量恒定，总产量无相对于原点的凸性，且不存在边际报酬递减**。这直接验证上文隐含的"边际产量函数形态决定TP曲线弯曲方向"准则：仅当 \(MP_L\) 递减（如分数幂）时，TP曲线凸向原点。

- **红线（\(MP_L\) 曲线）**：  
  位于 \(y=0.5\) 的水平直线。  
  **含义**：作为蓝线（TP）的斜率，其不变性说明**劳动力的边际技术替代率（MRTS）在短期恒定**，与上文Cobb-Douglas案例中 \(MP_L\) 递减导致的"曲线平缓化"形成端点对比。结合上文"规模报酬与边际报酬解耦"原则，此例中 \(MP_L\) 常数但规模报酬为递减（上文18.4(a)），进一步证实**边际报酬仅反映单一投入变动效应，与所有投入同比例变化的规模报酬无关**。

- **黑线（\(AP_L\) 曲线）**：  
  从高处（\(L \to 0^+\) 时 \(AP_L \to +\infty\)）递减并渐近于 \(y=0.5\)。  
  **含义**：始终位于红线（\(MP_L\)）上方，且随 \(L\) 增大而趋近于红线。这延续上文"平均-边际关系"：  
  - 当 \(L < 4\) 时（如 \(L=2\)，\(AP_L=1.5 > MP_L=0.5\)），投入效率受固定成本拖累；  
  - 当 \(L \to \infty\) 时，\(AP_L \to MP_L\)，表明**固定要素影响被稀释，平均产出收敛于边际产出水平**。  
  此规律与上文Cobb-Douglas案例一致，但因本例无边际递减，\(AP_L\) 的递减速率仅由固定截距（2）决定，而非常见的幂次效应。

#### 3. 知识连续性要点  
- **技术特性定位**：本图表将上文"要素互补连续谱"补全——  
  上文18.2（固定比例技术，完全互补）→ 上文18.3（Cobb-Douglas，连续替代）→ **本例（劳动完全可替代，线性技术）**。  
  \(MP_L\) 常数体现劳动的**无限替代弹性**，即增加劳动始终带来等量产出增量，与上文18.3中"边际递减需劳动幂次<1"的结论形成边界验证。  
- **短期分析启示**：  
  上文指出短期 \(MP_L\) 行为取决于生产函数中该要素的幂次（线性项→常数 \(MP_L\)），本例是其精确图示——**离散增量（\(\Delta L=1\) 时 \(\Delta TP=\Delta AP \times \Delta L\)）与微分结果严格相等**，突破上文18.3中"近似相等"的约束条件。  
- **图表误标提示**：页脚18.5节内容讨论固定比例技术（Leontief）的等产量线，但**与本图表无关**。本图表属18.4节，用于演示"单一可变投入"场景；18.5的等产量线需在两投入空间绘制（L形），但本图仅含劳动轴，承袭上文短期分析框架。

---
### Page/Slide 9



### 1. 提取图片文字与公式  
#### 图表标签  
- 坐标轴：X₁（横轴，0–80），X₂（纵轴，0–80）  
- 等产量线标注：  
  - "Red isoquant"（红等产量线）  
  - "Blue isoquant"（蓝等产量线）  
  - "Black isoquant"（黑等产量线）  
- 点标记：a, b, c  

#### 文字内容  
> *(b) Suppose that the firm wishes to produce 20 juggernauts at each plant. How much of each input will the firm need to produce 20 juggernauts at the Flint plant? $x_1 = 20, x_2 = 10$. How much of each input will the firm need to produce 20 juggernauts at the Inkster plant? $x_1 = 10, x_2 = 20$. Label with an a on the graph, the point representing the total amount of each of the two inputs that the firm needs to produce a total of 40 juggernauts, 20 at the Flint plant and 20 at the Inkster plant.*  
>  
> *(c) Label with a b on your graph the point that shows how much of each of the two inputs is needed in toto if the firm is to produce 10 juggernauts in the Flint plant and 30 juggernauts in the Inkster plant. Label with a c the point that shows how much of each of the two inputs that the firm needs in toto if it is to produce 30 juggernauts in the Flint plant and 10 juggernauts in the Inkster plant. Use a black pen to draw the firm’s isoquant for producing 40 units of output if it can split production in any manner between the two plants. Is the technology available to this firm convex? Yes.*  
>  
> *18.6 (0) You manage a crew of 160 workers who could be assigned to make either of two products. Product A requires 2 workers per unit of output. Product B requires 4 workers per unit of output.*  
>  
> *(a) Write an equation to express the combinations of products A and B that could be produced using exactly 160 workers. $2A + 4B = 160$.*  

#### 公式  
- Flint plant 生产 20 个 juggernauts：$x_1 = 20,\ x_2 = 10$  
- Inkster plant 生产 20 个 juggernauts：$x_1 = 10,\ x_2 = 20$  
- 问题 18.6(a)：$2A + 4B = 160$  

---

### 2. 图表变化含义解析  
#### 图表类型与技术背景  
本图为**两投入空间等产量线图**，分析多工厂联合生产的技术特性。上文 18.2 详述固定比例技术（Leontief 生产函数），此处为核心案例延伸：  
- **Flint plant** 生产函数：$f_F(x_1, x_2) = \min\{x_1, 2x_2\}$（由 $x_1=20, x_2=10$ 产 20 单位推导）  
- **Inkster plant** 生产函数：$f_I(x_1, x_2) = \min\{2x_1, x_2\}$（上文知识点明确给出）  
- **总产出目标**：40 juggernauts（可拆分至两工厂）  

#### 关键曲线几何特性  
| 曲线         | 位置与形状                              | 技术含义                                                                 | 与上文连续性                                                                 |
|--------------|----------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Red isoquant** | L 形：垂直段 $x_1=20$（$x_2 \geq 40$），水平段 $x_2=40$（$x_1 \geq 20$），拐点 $(20,40)$ | Inkster plant 的 40 单位等产量线。**严格固定比例技术**：$x_1/x_2 = 1/2$ 时最优，偏离需冗余投入。 | 对应上文 18.2 **完全互补技术**，是边际技术替代率（MRTS）为 0 或 $\infty$ 的极端案例，与上文 Cobb-Douglas 的连续替代形成连续谱端点。 |
| **Blue isoquant** | L 形：垂直段 $x_1=40$（$x_2 \geq 20$），水平段 $x_2=20$（$x_1 \geq 40$），拐点 $(40,20)$ | Flint plant 的 40 单位等产量线。固定比例 $\left(x_2/x_1 = 1/2\right)$，与 Inkster 互为转置。 | 延续固定比例技术框架，但**要素权重分配差异**（Flint 重 $x_1$，Inkster 重 $x_2$）为后续凸性分析埋下伏笔。 |
| **Black isoquant** | 直线：$x_1 + x_2 = 60$（$x_1 \in [20,40], x_2 \in [20,40]$），通过 $a(30,30)$、$b(25,35)$、$c(35,25)$ | 总产出 40 单位的**联合等产量线**。由两工厂最优投入求和得：<br> - $x_1 = \frac{y_F}{1} + \frac{y_I}{2}$<br> - $x_2 = \frac{y_F}{2} + \frac{y_I}{1}$<br> 代入 $y_F + y_I = 40$ 得 $x_1 + x_2 = 60$。 | **突破单一工厂限制**：上文指出“固定比例技术本身非凸”，但多工厂配置通过产量分拆使整体技术凸（回答 "Yes"）。这验证了上文“规模报酬与边际报酬解耦”原则的扩展——<br> **“产量配置自由度可柔化要素互补性，使集合整体凸”**，为一般均衡中凸性假设提供微观基础。 |

#### 优化路径与凸性本质  
- **点 $a$**：均分产量（20+20）→ $(30,30)$。**非效率点**：总投入 $x_1 + x_2 = 60$，但单厂无冗余。  
- **点 $b$ 与 $c$**：非对称分产（如 Flint 10 + Inkster 30）→ $b(25,35)$, $c(35,25)$。**效率边界**：总投入和恒为 60，但 $x_1$ 与 $x_2$ 交换替代（MRTS = -1）。  
- **凸性机制**：  
  黑线为直线（凸）而非两 L 形并集的缺角形状，因为：  
  - 在 $b$ 区域：Inkster 承担高产量（重 $x_1$ 输入），Flint 用 $x_1$ 富余；  
  - 在 $c$ 区域：Flint 承担高产量（重 $x_2$ 输入），Inkster 用 $x_2$ 富余。  
  **交替专业化**替代了单一工厂的严格互补性，使替代弹性从 0 突增至 1——呼应上文“线性技术体现无限替代弹性”，但此处为**分厂配置驱动**的特殊凸化。  

---

### 3. 知识连续性要点  
- **互补连续谱补全**：上文 18.2（单一固定比例）→ **本例（多工厂固定比例组合）** → 上文 18.3（Cobb-Douglas 连续替代）。  
  - L 形（非凸）→ 直线（凸）的转变，证明**技术凸性可源于组织架构**，而非仅函数形式，深化了上文“替代弹性决定生产集形状”的论断。  
- **短期分析扩展**：上文短期生产曲线聚焦单一可变投入，而本例通过**多工厂联合**将固定比例技术纳入一般均衡框架——当企业可配置子单元时，即使单工厂无替代弹性，**总量层面可生成线性投入集**（类似上文线性技术 $TP(L)$ 的 $MP_L$ 恒定特征，但此处为多维空间）。  
- **图表定位校正**：上文知识点提示“18.5 节讨论 Leontief 等产量线”，本图表即为其核心例证。**非上文 18.4 的 TP 曲线图**，但二者逻辑衔接：  
  - 18.4（线性/单投入）→ 边际报酬常数；  
  - 18.5（Leontief/双投入）→ MRTS 突变；  
  - **凸化后技术** → MRTS 恒定（黑线），形成跨模型一致性。

---
### Page/Slide 10



### 1. 图片中提取的文字与公式  

#### 图表部分  
- **坐标轴**：  
  - 横轴（A）：0–80，单位为产品A的产量  
  - 纵轴（B）：0–80，单位为产品B的产量  
- **阴影区域标注**：  
  - `Red shading`（红色阴影）：由公式 $4A + 2B = 180$ 定义的区域  
  - `Blue shading`（蓝色阴影）：由劳动力约束定义的区域（隐含公式 $2A + 4B = 160$）  
  - `Black shading`（黑色阴影）：上述两个约束的交集区域  

#### 文字部分  
- 题目 (b)：  
  - 条件：1单位A需4铲子+2工人，1单位B需2铲子+4工人；180铲子限制。  
  - 公式：**$4A + 2B = 180$**（铲子约束边界）  
- 题目 (d)：  
  - 联立约束方程：**$2A + 4B = 160$**（劳动力约束）和 **$4A + 2B = 180$**（铲子约束）  
- 题目 (e)：  
  - 最大A产量：**45 units**（当 $B=0$ 时）  
  - 未用尽的资源：**Workers**（工人）  
  - 剩余量：**70**  
- 习题 18.7 (0)：  
  - 生产函数1：$f(x,y) = \min\{2x, x+y\}$  
  - 生产函数2：$f(x,y) = x + \min\{x, y\}$  

---

### 2. 图表解析：约束条件与生产集凸性  

#### **约束边界与阴影区域的经济学含义**  
- **红色阴影（$4A + 2B = 180$）**：  
  - 铲子资源的固定比例约束：生产需严格满足 $4A + 2B \leq 180$。  
  - 类似上文 **严格固定比例技术**（Leontief 技术），体现 **要素投入的不可替代性**（例如：增产A必须同步增加铲子投入）。  

- **蓝色阴影（$2A + 4B = 160$）**：  
  - 劳动力资源的固定比例约束：隐含 $2A + 4B \leq 160$。  
  - 与上文 **多工厂技术对比**：  
    - 上文 Inkster 和 Flint 工厂分别对应单一要素权重（$x_1/x_2 = 1/2$ vs $x_2/x_1 = 1/2$）。  
    - 本例中 A 和 B 的生产比例互为 **转置互补**：  
      - A 重“铲子”（$s/l = 2$），B 重“工人”（$l/s = 2$），与上文 Inkster/Flint 逻辑一致。  

- **黑色阴影（双重约束交集）**：  
  - 可行生产集：满足 $2A + 4B \leq 160$ 且 $4A + 2B \leq 180$ 的 (A, B) 组合。  
  - **凸性来源**：  
    - 单约束边界（红色、蓝色）为线性，其交集区域为 **凸多边形**（顶点：(0,40), (33.3,23.3), (45,0)）。  
    - 与上文 **凸性机制** 直接呼应：  
      > “**产量配置自由度可柔化要素互补性**” —— 通过动态调整 A 和 B 的产量比例（如减少 B 以增产 A），使总量层面形成替代可能性（MRTS 恒定为 -1/2 在交界区域内），突破单一产品的固定比例限制。  

#### **关键点解析**  
- **题目 (d)**：  
  - 解方程组 $2A + 4B = 160$ 和 $4A + 2B = 180$ 的交点 **(33.3, 23.3)** 是 **资源充分利用的帕累托有效点**。  
  - 对应上文 **点 $a$（30,30）**：  
    - 两案例均表示 **“交替专业化”** 的平衡状态 —— 两种生产模式（或资源）均无冗余。  

- **题目 (e)**：  
  - 最大 A 产量 **45 units**（$B=0$）时：  
    - **铲子完全耗尽**（$4 \times 45 = 180$），但 **工人剩余 70**（$2 \times 45 = 90 < 160$）。  
    - 对应上文 **点 $b$ 或 $c$**：  
      > “**Inkster 承担高产量（重 $x_1$ 输入）**” → 本例中 A 作为 “铲子密集型” 产品，类似 Inkster 将一个要素用至极限。  
      - **替代弹性突变**：在 $B=0$ 边界处，MRTS 从 -1/2 突变为 0（仅调整 A 时无法再增产）。  

---

### 3. 与【上文知识点】的知识连续性  

| 概念                | 上文案例（多工厂）                          | 本例（双产品）                              |  
|---------------------|------------------------------------------|------------------------------------------|  
| **固定比例技术**    | Inkster: $x_1/x_2 = 1/2$               | A: 铲子/工人 = 2:1                      |  
| **互补性转置**      | Flint 与 Inkster 互为要素权重转置        | A 与 B 互为资源密集度转置               |  
| **凸性来源**        | 产量分拆：单工厂非凸 → 多工厂联合凸      | 产量组合：单产品约束线性 → 资源交集凸    |  
| **效率边界**        | 黑线 $x_1 + x_2 = 60$（MRTS = -1）     | 两线段交界处（MRTS = -1/2）             |  
| **冗余投入**        | 点 $a$ 处单厂无冗余，总投入和恒定        | (45,0) 处工人冗余 70，铲子无冗余        |  

- **核心延续**：  
  > 本例 **验证了上文凸性机制的普适性** —— 无论组织单元是“多工厂”还是“多产品”，**通过分割或组合技术，可将局部非凸性转化为总量层面的线性替代关系**。  
  - 深化结论：  
    > “替代弹性 0（Leontief）与 ∞（线性）之间的连续谱，亦可通过 **资源多任务配置**（而非仅单一技术函数）实现。”  
  - 与上文图示衔接：  
    > 本图表即上文 **18.5 节 Leontief 技术** 的生产可能性边界扩展（非 18.4 的单投入 TP 曲线），共同完成“固定比例→连续替代”的逻辑闭环。

---
### Page/Slide 11



## Extracted Content from Current Image

### Header
- **NAME ________ 239**

### Instruction Text
- Both do. On the same graph, use black ink to draw a couple of isoquants for the second firm.

### Chart Details
- **Axes**:  
  - X-axis: Labeled from 0 to 40 (intervals of 10).  
  - Y-axis: Labeled from 0 to 40 (intervals of 10).  
- **Isoquants**:  
  - **Red isoquants**: Vertical line segments with horizontal arrows (← →) labeled "Red isoquants".  
  - **Black isoquants**: Linear downward-sloping line segment with downward arrow (↓) labeled "Black isoquants".  

### Formulas and Questions
**18.8 (0)**  
- Production function:  
  \[
  f(x_1, x_2, x_3) = A x_1^a x_2^b x_3^c
  \]  
- Condition: \(a + b + c > 1\).  
- Proof for increasing returns to scale:  
  \[
  \text{For any } t > 1, \, f(tx_1, tx_2, tx_3) = A (tx_1)^a (tx_2)^b (tx_3)^c = t^{a+b+c} f(x_1, x_2, x_3) > t f(x_1, x_2, x_3).
  \]

**18.9 (0)**  
- Production function:  
  \[
  f(x_1, x_2) = C x_1^a x_2^b
  \]  
  where \(a, b, C > 0\).  
- **(a)** Returns to scale conditions:  
  - Decreasing returns: \(C > 0\) and \(a + b < 1\).  
  - Constant returns: \(C > 0\) and \(a + b = 1\).  
  - Increasing returns: \(C > 0\) and \(a + b > 1\).  
- **(b)** Decreasing marginal product for factor 1:  
  \(C > 0\), \(b > 0\), and \(a < 1\).

---

## Chart Explanation with Continuity from Previous Knowledge

### 1. **Isoquant Shapes and Their Significance**  
The chart displays two distinct isoquant sets for a two-firm system, directly extending the "fixed proportion → continuous substitution" logic from the previous knowledge:  
- **Red isoquants (vertical segments)**: Represent a Leontief *fixed-proportions* technology. This mirrors the $x_1/x_2 = 1/2$ constraint in Inkster (or A’s "铲子/工人 = 2:1" ratio), where output requires rigid input combinations. **Changes at the boundary**: Vertical segments imply **zero substitutability** within a single firm/technology—a direct analog to the "alternating specialization" in the earlier production set, but now visualized in *input space*. When one input is fixed (e.g., $x_1 = 10$), increasing $x_2$ alone yields no output gain.  
- **Black isoquants (downward-sloping line)**: Represent a perfect-substitutes technology (linear), where the constant slope (MRTS) enables continuous input substitution. This contrasts with the red Leontief isoquants but **connects to the previous convexity mechanism**: While individual firms may be technically non-convex (e.g., red isoquants), aggregating firms with *complementary* rigidities (as with Inkster/Flint) generates a convex *aggregate* isoquant envelope. Here, the black isoquants symbolize the "marginal" flexibility that, when combined with the red technology, allows the economy-wide MRTS to stabilize—like how adjusting A/B ratios created a linear PPF segment in the earlier case.

### 2. **Link to Key Concepts from Previous Summary**  
- **Convexity origin**:  
  The red and black isoquants illustrate how **local technological non-convexities (Leontief) can be smoothed through aggregation**—just as the intersection of $2A + 4B \leq 160$ and $4A + 2B \leq 180$ created a convex production set. Vertically rigid red isoquants (fixed proportions) paired with linear black isoquants (smooth substitutes) yield a non-convex *individual* firm set, but when firms operate jointly (e.g., one specializes in red-technology segments, the other in black), the *envelope* of feasible input combinations becomes convex. This embodies the core principle:  
  > "*Production possibilities convexity arises from dynamic reallocation of resources across heterogeneous technologies*."  

- **Substitution elasticity and returns to scale**:  
  The black isoquants’ linearity implies infinite substitution elasticity—contrasting with the red isoquants’ zero elasticity. This pairs with 18.9(a), where $a + b$ dictates returns to scale:  
  - When $a + b < 1$ (decreasing returns), isoquants become less steep (reduced marginal productivity), but the **comparison of red/black sets highlights context-dependence**: A single technology (e.g., pure Leontief) imposes inherent non-convexities, while scale effects (18.8–18.9) emerge from the *functional form*. Critically, the chart confirms that **aggregate convexity requires heterogeneous technologies** (as in the A/B production example), not just smooth single-technology returns-to-scale properties.  

- **Real-world relevance**:  
  The chart visualizes the "transposed complementarity" described earlier (e.g., A heavy on "shovels" vs. B on "labor"). Here, the red isoquants could represent an "input-heavy" firm (e.g., high $x_1$ requirement), while black isoquants reflect a "balanced" firm. Their combined feasible set explains why the efficiency frontier in the prior PPF (e.g., the line segment with constant MRTS = -1/2) emerges: It is the *lower envelope* of all possible isoquant tangencies.  

### 3. **Why the Chart Matters**  
This extends the previous summary’s focus on *output-side* constraints (e.g., 2A + 4B ≤ 160) to *input-side* mechanisms. The simultaneous presentation of Leontief (red) and linear (black) isoquants—anchored in the same graph—demonstrates that:  
> "*The spectrum of substitution elasticity (0 for pure Leontief, ∞ for perfect substitutes) narrows when multiple technologies are deployed, enabling quasi-linear frontiers even with embedded Leontief subtechnologies.*"  

This bridges seamlessly to 18.8–18.9: The Cobb-Douglas function’s returns to scale (dependent on $a+b+c$) show how continuous parameters can *formally* capture what the red/black isoquant pair *graphically* implies—**technological aggregation generates substitutability where none existed in isolated components**. Thus, the chart is not just about individual firms; it is the input-space counterpart to the production possibility set’s convexity in Section 18.5, completing the transition from fixed proportions to viable alternatives.

---
### Page/Slide 12



### 1. 提取文字与公式  
#### 页眉  
240   TECHNOLOGY   (Ch. 18)  

#### 内容  
- **(c)** For what positive values of $a$, $b$, and $C$ is there diminishing technical rate of substitution?  
  **For all positive values.**  

- **18.10 (0)** Suppose that the production function is $f(x_1, x_2) = (x_1^a + x_2^a)^b$, where $a$ and $b$ are positive constants.  
  - **(a)**  
    - Decreasing returns to scale? $ab < 1$.  
    - Constant returns to scale? $ab = 1$.  
    - Increasing returns to scale? $ab > 1$.  

- **18.11 (0)** Suppose that a firm has the production function $f(x_1, x_2) = \sqrt{x_1} + x_2^2$.  
  - **(a)**  
    - Marginal product of factor 1: **decreases** as $x_1$ increases.  
    - Marginal product of factor 2: **increases** as $x_2$ increases.  
  - **(b)**  
    - Returns to scale are **not uniformly defined** due to input比例 dependence.  
      - Doubling inputs **more than doubles output**: $x_1 = 1, x_2 = 4$.  
      - Doubling inputs **less than doubles output**: $x_1 = 4, x_2 = 0$.  

---

### 2. 结合上文的解析  
#### 与上文知识点的关联  
当前图片中的 **18.10–18.11** 直接验证了上文总结中关于 **"scale effects emerge from functional form"** 的核心论点：  
- **18.10** 通过幂函数 $f(x_1, x_2) = (x_1^a + x_2^a)^b$ 的参数约束（$ab < 1$, $ab = 1$, $ab > 1$），**形式化刻画了规模报酬的动态性**。其结论（如 $ab = 1$ 时为常规模报）与上文提到的 "Cobb-Douglas function’s returns to scale (dependent on $a+b+c$)" 逻辑一致，印证了函数形式对规模效应的决定性影响。  
- **18.11** 的非齐次生产函数 $f(x_1, x_2) = \sqrt{x_1} + x_2^2$ 进一步揭示：  
  - 边际生产力的非对称性（$MP_1$ 递减 vs. $MP_2$ 递增）与上文 **"input-heavy vs. balanced firms"** 的异质技术隐喻相呼应；  
  - 规模报酬**依赖于投入比例**（如 $x_1 = 1, x_2 = 4$ 时递增，$x_1 = 4, x_2 = 0$ 时递减），**直接支撑了上文 "the spectrum of substitution elasticity narrows when multiple technologies are deployed"** 的论断——单一函数内部因比例差异即可产生等效于 "技术异质性" 的行为，无需依赖外部技术集合。  

#### 关键延伸  
- 上文强调 **"aggregate convexity requires heterogeneous technologies"**，而 18.11 证明：**单一非齐次函数即可通过投入组合变化生成局部非凸性**。这补充了上文逻辑——即使无显式多技术，函数内部的参数非对称性（如平方根与平方项并存）也能模拟异质性，进而促成 "quasi-linear frontiers" 的形成。  
- 18.10 中 $ab = 1$ 的常规模报条件，是上文 **"Cobb-Douglas function’s returns to scale"** 的数学具象化，将抽象的参数化规模效应（$a+b+c$）转化为幂函数特定结构（$ab$）的直观判据。  

> **知识衔接**：当前问题从微观层面解构了上文图表隐含的机制——技术异质性（由函数形式编码）如何通过投入比例调控，最终推导出宏观生产可能集的凸性。
