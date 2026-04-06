# PDF_Chapter_4

### Page/Slide 1



### 1. 文字与公式提取

#### 章节标题
- **Chapter 4**  
- **Utility**

#### 引言内容
- 效用函数（utility function）是描述偏好的另一种方式，为商品束分配效用数值，满足：  
  若消费者偏好 $(x, y)$ 而非 $(x', y')$，则 $(x, y)$ 的效用值更高。  
  若效用函数为 $U(x_1, x_2)$，则效用值相同的商品束无差异。

#### 关键理论
- **无差异曲线斜率与边际替代率（MRS）**：  
  无差异曲线在 $(x_1, x_2)$ 处的斜率为 $-\frac{MU_1}{MU_2}$，其中 $MU_1$ 和 $MU_2$ 分别为商品 1 和商品 2 的边际效用。  
  - 边际效用计算：若效用函数为 $U(x_1, x_2)$，则 $MU_1 = \frac{\partial U}{\partial x_1}$，$MU_2 = \frac{\partial U}{\partial x_2}$。

#### 示例公式
1. **Arthur 的效用函数**：  
   $$
   U(x_1, x_2) = x_1 x_2
   $$  
   - 通过点 $(3, 4)$ 的无差异曲线：  
     $$
     U(3,4) = 3 \times 4 = 12 \quad \Rightarrow \quad x_1 x_2 = 12 \quad \Rightarrow \quad x_2 = \frac{12}{x_1}
     $$  
   - 边际替代率（MRS）在 $(3,4)$ 处：  
     $$
     \text{MRS} = -\frac{MU_1}{MU_2} = -\frac{x_2}{x_1} = -\frac{4}{3}
     $$

2. **Basil 的效用函数**：  
   $$
   U^*(x_1, x_2) = 3x_1 x_2 - 10 = 3U(x_1, x_2) - 10
   $$  
   - 结论：$U^*$ 是 $U$ 的单调递增变换（**monotonic increasing transformation**）。

---

### 2. 内容解析

#### 效用函数与无差异曲线的关系
- 效用函数将偏好**数值化**，无差异曲线是效用函数的**等高线**（如 $x_1 x_2 = 12$）。  
- 边际替代率（MRS）的推导基于效用函数的**全微分**：  
  $$
  dU = MU_1 dx_1 + MU_2 dx_2 = 0 \quad \Rightarrow \quad \frac{dx_2}{dx_1} = -\frac{MU_1}{MU_2}
  $$  
  与上文知识点中“无差异曲线斜率等于边际替代率”直接衔接。

#### 单调变换的经济意义
- Basil 的效用函数 $U^* = 3U - 10$ 并未改变偏好排序：  
  - 原函数 $U$ 中 $U(A) > U(B)$，则 $U^*(A) > U^*(B)$。  
  - **关键性质**：单调递增变换保持无差异曲线形状和 MRS 不变（因 $\frac{dU^*}{dU} = 3 > 0$）。

#### 边际效用的几何含义
- 对 $U = x_1 x_2$：  
  - $MU_1 = x_2$ 表示商品 1 的边际效用随商品 2 消费量增加而上升；  
  - $MU_2 = x_1$ 表示商品 2 的边际效用随商品 1 消费量增加而上升。  
  - 当商品量增加时，MRS 的绝对值 $\frac{x_2}{x_1}$ 变化反映**替代难度**（如 $(x_1, x_2)$ 增大，MRS 趋近于 1）。

---

### 3. 知识连续性说明
- 本节将上一章**定性描述的无差异曲线**转化为**定量效用函数**，为后续最优消费选择（效用最大化）提供数学工具。  
- 边际替代率与边际效用的关系，为后续**消费者均衡条件**（$\text{MRS} = \text{价格比}$）奠定基础。  
- 单调变换的引入说明：效用函数的**数值本身无意义**，仅需保留偏好排序（序数效用论核心思想）。

---
### Page/Slide 2



### 1. 文字与公式提取  
**章节信息**  
- 页码: 34  
- 章节: UTILITY (Ch. 4)  

**主体文字**  
> us find Basil’s indifference curve through the point (3,4). First we find that $U^*(3,4) = 3 \times 3 \times 4 - 10 = 26$. The indifference curve passing through this point consists of all $(x_1, x_2)$ such that $3x_1x_2 - 10 = 26$. Simplify this last expression by adding 10 to both sides of the equation and dividing both sides by 3. You find $x_1x_2 = 12$, or equivalently, $x_2 = 12/x_1$. This is exactly the same curve as Arthur’s indifference curve through (3,4). We could have known in advance that this would happen, because if two consumers’ utility functions are monotonic increasing transformations of each other, then these consumers must have the same preference relation between any pair of commodity bundles.  

> When you have finished this workout, we hope that you will be able to do the following:  
> - Draw an indifference curve through a specified commodity bundle when you know the utility function.  
> - Calculate marginal utilities and marginal rates of substitution when you know the utility function.  
> - Determine whether one utility function is just a “monotonic transformation” of another and know what that implies about preferences.  
> - Find utility functions that represent preferences when goods are perfect substitutes and when goods are perfect complements.  
> - Recognize utility functions for commonly studied preferences such as perfect substitutes, perfect complements, and other kinked indifference curves, quasilinear utility, and Cobb-Douglas utility.  

**4.0 Warm Up Exercise**  
> This is the first of several “warm up exercises” that you will find in *Workouts*. These are here to help you see how to do calculations that are needed in later problems. The answers to all warm up exercises are in your answer pages. If you find the warm up exercises easy and boring, go ahead—skip them and get on to the main problems. You can come back and look at them if you get stuck later.  
>   
> This exercise asks you to calculate marginal utilities and marginal rates of substitution for some common utility functions. These utility functions will reappear in several chapters, so it is a good idea to get to know them now. If you know calculus, you will find this to be a breeze. Even if your calculus is shaky or nonexistent, you can handle the first three utility functions just by using the definitions in the textbook. These three are easy because the utility functions are linear. If you do not know any calculus, fill in the rest of the answers from the back of the workbook and keep a copy of this exercise for reference when you encounter these utility functions in later problems.  

**公式提取**  
- $U^*(3,4) = 3 \times 3 \times 4 - 10 = 26$  
- $3x_1x_2 - 10 = 26$  
- $x_1x_2 = 12$  
- $x_2 = \frac{12}{x_1}$  

---

### 2. 内容解析  
#### 单调变换的验证与知识延续  
当前图片通过**具体数值计算**验证了上文知识点中“单调递增变换保持无差异曲线和偏好关系不变”的核心结论：  
- 给定 Basil 的效用函数 $U^*(x_1, x_2) = 3x_1x_2 - 10$，计算其在 $(3,4)$ 处的效用值 $U^*(3,4) = 26$，并推导出无差异曲线方程 $x_1x_2 = 12$。  
- 此结果与 Arthur 的效用函数 $U(x_1, x_2) = x_1x_2$ 生成的无差异曲线完全一致（$x_1x_2 = 12$），直接印证了上文所述**单调变换不改变无差异曲线形状**的性质。  
- 经济含义：消费者偏好由相对排序决定，而非效用数值本身（序数效用论）。Basil 与 Arthur 的效用函数仅差一个单调递增变换 $U^* = 3U - 10$，因此二者对任意商品束的偏好排序完全相同，MRS 也保持不变（如 $(3,4)$ 处 MRS 仍为 $-4/3$）。  

#### 学习目标的衔接作用  
图片中的能力清单**系统化整合了本章关键技能**，与上文知识点形成逻辑闭环：  
- **绘制无差异曲线**（基于效用函数）：延续上文 Arthur 示例中 $x_2 = 12/x_1$ 的等高线推导，强调效用函数的等值线映射。  
- **计算 MRS 与边际效用**：承接上文 $dU = MU_1 dx_1 + MU_2 dx_2 = 0$ 的推导框架，凸显效用函数作为后续消费者均衡（$\text{MRS} = \text{价格比}$）的数学基础。  
- **识别单调变换**：通过 Basil 案例具象化上文理论，说明其对偏好不变的判定标准（如 $dU^*/dU > 0$）。  
- **特殊偏好函数**（完全替代/互补等）：为后续章节（如第 5 章消费者最优选择）铺垫，体现效用函数从理论到应用的过渡。  

#### 热身练习的实践定位  
- 该练习明确指向**本章方法论的落地应用**：通过常见效用函数（如线性函数）训练边际计算，呼应上文边际效用几何含义的讨论（如 $MU_1 = x_2$ 的直观解释）。  
- 知识连续性体现为：  
  - 强调效用函数在多章中的复用性（如 Cobb-Douglas 型），衔接后续“消费者需求”主题。  
  - 提示初学者通过定义（而非微积分）理解线性效用函数，降低序数效用论的学习门槛，为效用最大化问题奠定操作基础。  

> 注：本节无图表，故省略图表解释。所有分析严格基于上文知识点展开，避免重复理论细节，聚焦于实例验证、能力整合与后续知识衔接。

---
### Page/Slide 3



### 1. 文字与公式提取  
**表格内容**（四列，共12行）：  

| $u(x_1, x_2)$           | $MU_1(x_1, x_2)$       | $MU_2(x_1, x_2)$       | $MRS(x_1, x_2)$                     |
|-------------------------|------------------------|------------------------|-------------------------------------|
| $2x_1 + 3x_2$         | $2$                   | $3$                   | $-2/3$                           |
| $4x_1 + 6x_2$         | $4$                   | $6$                   | $-2/3$                           |
| $ax_1 + bx_2$         | $a$                   | $b$                   | $-a/b$                           |
| $2\sqrt{x_1} + x_2$   | $\frac{1}{\sqrt{x_1}}$ | $1$                   | $-\frac{1}{\sqrt{x_1}}$          |
| $\ln x_1 + x_2$       | $1/x_1$               | $1$                   | $-1/x_1$                         |
| $v(x_1) + x_2$        | $v'(x_1)$             | $1$                   | $-v'(x_1)$                       |
| $x_1x_2$              | $x_2$                 | $x_1$                 | $-x_2/x_1$                       |
| $x_1^a x_2^b$         | $a x_1^{a-1} x_2^b$   | $b x_1^a x_2^{b-1}$   | $-\frac{a x_2}{b x_1}$           |
| $(x_1 + 2)(x_2 + 1)$  | $x_2 + 1$             | $x_1 + 2$             | $-\left(\frac{x_2 + 1}{x_1 + 2}\right)$ |
| $(x_1 + a)(x_2 + b)$  | $x_2 + b$             | $x_1 + a$             | $-\left(\frac{x_2 + b}{x_1 + a}\right)$ |
| $x_1^a + x_2^a$       | $a x_1^{a-1}$         | $a x_2^{a-1}$         | $-\left(\frac{x_1}{x_2}\right)^{a-1}$ |

---

### 2. 表格解析与知识延续  
#### **线性效用函数的单调变换验证**  
- **完全替代偏好的一致性**：前3行均为线性效用函数（$u = ax_1 + bx_2$）。第2行是第1行的2倍（$4x_1 + 6x_2 = 2(2x_1 + 3x_2)$），属**单调递增变换**。两者$MRS = -2/3$完全相同，直接印证上文结论——**单调变换不改变MRS**，偏好排序保持不变。  
- **实践意义**：线性函数的$MRS$为常数，说明消费者对商品边际替代率固定，对应**完全替代偏好**。此表简化计算流程，避免重复推导，呼应上文“热身练习”对常见函数的预演要求。

#### **Cobb-Douglas型偏好的MRS规律**  
- 第6、7行（$x_1x_2$与$x_1^a x_2^b$）展示**凸偏好**特征：  
  - $MRS = -x_2/x_1$ 随$x_1$增加而减小（绝对值），表明无差异曲线凸向原点。  
  - 参数$a,b$控制替代弹性：例如$a = b = 1$时，MRS仅与比例$x_2/x_1$相关，延续上文Basil案例中$3x_1x_2 - 10$的MRS计算逻辑。  
- **位移扩展型**（第8、9行）：$(x_1 + a)(x_2 + b)$ 模拟“基础消费量”，其MRS形式与标准Cobb-Douglas一致（仅加常数项），体现**偏好结构不变性**，为后续消费者预算约束分析提供模板。

#### **拟线性偏好的特殊性**  
- 第4、5、6行（如$\ln x_1 + x_2$、$v(x_1) + x_2$）属于**拟线性效用函数**：  
  - $MU_2 = 1$，说明商品2的边际效用恒定；  
  - $MRS$仅依赖$x_1$（如$-1/x_1$），导致无差异曲线**垂直平行**（横向平移即可重合）。  
- **知识衔接**：此类函数在后续“收入效应为零”（第6章）与“消费者剩余计算”（第14章）中关键，表格提前固化其数学特征，降低学习门槛。

#### **幂函数与替代弹性**  
- 第11行$x_1^a + x_2^a$的$MRS = -\left(\frac{x_1}{x_2}\right)^{a-1}$：  
  - $a=1$：退化为完全替代（$MRS = -1$）；  
  - $a \to 0$：接近Cobb-Douglas；  
  - $a \to -\infty$：趋近完全互补。  
- **几何含义**：$a$值直接映射**替代弹性**，表中公式为第6章“替代弹性计算”埋下伏笔，强化效用函数与需求理论的关联性。

---

### 3. 表格的系统性作用  
- **方法论集约化**：汇总12种典型效用函数的边际量，将上文“热身练习”中的**分散案例整合为快速参照表**，避免后续章节重复推导。  
- **技能闭环**：覆盖从线性函数（无需微积分）到一般函数（需微积分求导）的梯度难度，呼应上文对不同数学基础学习者的指导。  
- **序数效用论实操化**：通过$MRS$的符号与结构（如$-x_2/x_1$ vs. $-a/b$），直观区分**偏好类型**（凸性、替代性），将抽象理论转化为可操作的分类工具。  

> 注：本表作为后续消费者最优选择（$\text{MRS} = p_1/p_2$）与需求推导的核心输入，继承上文对效用函数“多章复用性”的强调，实现“工具—应用”的知识连贯性。

---
### Page/Slide 4



# 效用函数应用案例解析

## 1. 文字与公式提取

### 文字内容
- Charlie的效用函数：$U(x_A, x_B) = x_A x_B$
- (a) 点(40,5)的效用值：$U(40,5) = 200$
- 无差异曲线方程：$x_A x_B = 200$，即 $x_B = \frac{200}{x_A}$
- (b) Donna的交易提议：15香蕉换25苹果
- 交易结果判断：Yes（Charlie会获得更好消费束）
- 愿意交易的最大苹果数：30
- 4.2 (0) Ambrose的无差异曲线方程：$x_2 = 20 - 4\sqrt{x_1}$ 和 $x_2 = 24 - 4\sqrt{x_1}$

### 公式内容
- $U(x_A, x_B) = x_A x_B$
- $U(40,5) = 200$
- $x_A x_B = 200$
- $x_B = \frac{200}{x_A}$
- $x_2 = 20 - 4\sqrt{x_1}$
- $x_2 = 24 - 4\sqrt{x_1}$

## 2. 图表分析与知识衔接

### 无差异曲线特征
- **函数类型定位**：图中曲线对应上文知识点中的标准Cobb-Douglas型效用函数（第6行$x_1x_2$的特例），当$a=b=1$时
- **MRS特性**：根据上文规律，该曲线MRS为$-\frac{x_B}{x_A}$，在点(40,5)处MRS = $-5/40 = -0.125$
- **凸性表现**：曲线严格凸向原点，体现**边际替代率递减规律**——随着苹果消费量$x_A$增加，Charlie愿意放弃的香蕉数量递减

### 曲线方程与效用水平
- 特定效用水平$\bar{U}=200$对应无差异曲线$x_B = \frac{200}{x_A}$，这是上文Cobb-Douglas函数的直接应用
- 比较上文表格第6行：对$x_1x_2$函数，MRS = $-\frac{x_2}{x_1}$，与本题中的$x_B/x_A$形式完全一致

### 交易决策的效用分析
- 交易后消费束(15,20)的效用：$15 \times 20 = 300 > 200$
- **MRS变化逻辑**：原点MRS = $-5/40 = -0.125$，交易后点(15,20)处MRS = $-20/15 ≈ -1.333$
  - 说明随着香蕉相对增加，Charlie对香蕉的估值下降，更愿意用香蕉换苹果
- 最大可接受苹果数计算：令$(40-y) \times 20 = 200$ → $y = 30$
  - 这验证了上文"无差异曲线是相同效用水平的消费束集合"的核心概念

### 几何含义延伸
- 图中曲线**不通过原点**：当$x_A=0$或$x_B=0$时效用为0，与正效用水平200的曲线分离
- 下凸形状直观展示上文所述的"无差异曲线凸性"特征，为后续实现消费者均衡($MRS = p_1/p_2$)提供视觉基础

## 3. 与上文知识点的深度衔接

| 本例特征 | 上文知识点对应 | 分析价值 |
|---------|----------------|----------|
| $U=x_A x_B$ | Cobb-Douglas特例(a=b=1) | 直观展示MRS与消费束比例的关系 |
| 凸形无差异曲线 | 凸偏好特征验证 | 验证"随着$x_1$增加，MRS绝对值减小"的规律 |
| 效用水平200 | 效用函数序数性质 | 体现无差异曲线代表等效用集合 |
| 交易分析 | MRS的应用场景 | 展示为何MRS决定交易意愿和边界 |

> 本例将上文抽象的效用函数形式转化为具体决策场景：通过将Cobb-Douglas效用函数与真实消费选择结合，验证了MRS作为消费者替代意愿的度量工具价值，并为后续章节"预算约束下的最优选择"建立直观认知基础。特别值得注意的是，图中曲线明确展示了当$x_A$增加时，为维持相同效用所需放弃的$x_B$数量逐渐减少的规律，直接呼应上文"凸偏好"的核心特征。

---
### Page/Slide 5



# 效用函数案例解析：Ambrose的拟线性效用  

## 1. 文字与公式提取  

### 文字内容  
- Ambrose的效用函数：$U(x_1, x_2) = 4\sqrt{x_1} + x_2$  
- (a) 原始消费：9单位坚果 + 10单位浆果；坚果减至4单位后，需补偿至14单位浆果以维持相同效用  
- (b) 验证消费束(9,10)与(25,2)无差异；(18,20)与(50,4)不在同一无差异曲线（答案：No）  
- (c) 边际替代率(MRS)：在(9,10)处为 $-2/3$；在(9,20)处仍为 $-2/3$  
- (d) MRS一般表达式：$MRS(x_1, x_2) = -2 / \sqrt{x_1}$；MRS不受$x_2$变化影响  

### 公式内容  
- $U(x_1, x_2) = 4\sqrt{x_1} + x_2$  
- $MRS(x_1, x_2) = -2 / \sqrt{x_1}$  

## 2. 图表分析与上文知识衔接  

### 无差异曲线特征（结合图表）  
- **函数类型定位**：该曲线对应**拟线性效用函数**（上文"一般函数"范畴），其结构 $a\sqrt{x_1} + x_2$ 体现 **非对称偏好** — $x_1$ 具有递减边际效用（需微积分），而 $x_2$ 保持线性属性。  
- **MRS特性**：  
  - 图表中曲线通过点(9,10)，此处 $MRS = -2 / \sqrt{9} = -2/3$（与$c$部分一致）。  
  - **关键延伸**：MRS仅由 $x_1$ 决定（$-2 / \sqrt{x_1}$），与 $x_2$ 无关 — 这验证了上文"序数效用论实操化"中 **偏好类型分类工具** 的核心：  
    - 与Cobb-Douglas效用（如 $U=x_1 x_2$）的 $MRS = -x_2/x_1$ 相比，本例 $MRS$ 不含 $x_2$ 项，表明 **$x_2$ 为"货币等价物"**，体现拟线性偏好的典型特征（替代决策仅依赖 $x_1$ 消费水平）。  
- **凸性表现**：  
  - 曲线严格凸向原点（二阶导数 $d^2x_2/dx_1^2 > 0$），遵循 **边际替代率递减规律** — 随 $x_1$ 增加，$MRS$ 绝对值减小（如 $x_1=4$ 时 $MRS=-1$，$x_1=9$ 时 $MRS=-2/3$），呼应上文"凸偏好"的定义框架。  

### 效用水平与交易行为  
- **无差异曲线集合**：点(9,10)与(25,2)效用相等（$U=4\sqrt{9}+10=22$，$U=4\sqrt{25}+2=22$），直观印证上文"无差异曲线代表相同效用水平的消费束集合"这一基础概念。  
- **交叉效应缺失**：问题(c)显示 $x_2$ 从10增至20时 $MRS$ 不变，说明 **仅当 $x_1$ 变化时替代意愿改变** — 这直接延伸上文"将抽象理论转化为可操作分类工具"：通过 $MRS$ 结构可快速识别 **拟线性偏好**（而非凸性替代或互补偏好）。  
- **预算约束隐喻**：若后续引入价格，$MRS$ 的 $x_2$ 不变性将导致消费者最优解中可能出现 **角点解**（$x_2$ 完全依赖预算），为上文所述"消费者最优选择（$MRS = p_1/p_2$）"提供几何铺垫。  

### 与上文知识点的深度协同  
| 本例发现 | 上文知识点映射 | 分析价值 |  
|----------|----------------|----------|  
| $MRS$ 仅依赖 $x_1$ | 梯度难度中的"一般函数求导" | 确立 **单一变量MRS** 的分类符号（$-a / \sqrt{x_1}$ vs. 上文 $-x_2/x_1$），延续"工具—应用"知识链 |  
| 无差异曲线垂直平行性（隐含） | 序数效用的分类工具 | 证明 **$\bar{U}$ 变化仅平移曲线垂直位置**，强化"效用函数多章复用性" |  
| MRS与$x_2$无关的验证 | 技能闭环中的微积分环节 | 用直接计算（$dU/dx_1 = 2/\sqrt{x_1}$）演示 **MRS推导流程**，衔接"不同数学基础学习者"指导 |  

> 本例精准填补上文案例矩阵：Cobb-Douglas展示 **双向MRS依赖**，而拟线性模型暴露 **单向MRS结构**，共同构成偏好分类的操作框架。图表中曲线的恒定斜率变化（随 $x_1$ 增加而坡度变缓），既是边际替代率递减的可视化证明，也为后续"需求推导"提供核心参数（$MRS$ 决定替换阈值）。特别突出的是，当 $x_2$ 变化不改变 $MRS$ 时，消费者将优先调整 $x_2$ 以匹配预算约束 — 此机制后续将用于解构消费者最优选择的内在逻辑。

---
### Page/Slide 6



### 提取内容：当前图片中的文字与公式

**文字内容：**  
- Burt’s utility function is \( U(x_1, x_2) = (x_1 + 2)(x_2 + 6) \), where \( x_1 \) is the number of cookies and \( x_2 \) is the number of glasses of milk.  
- (a) Slope of indifference curve at (4,6) is \(-2\). Tangent line drawn through (4,6).  
- (b) Indifference curve through (4,6) passes through (10,0), (7,2), and (2,12). Equation: \( x_2 = \frac{72}{x_1 + 2} - 6 \).  
- (c) Trading (4,6) for (1,15): \( U(1,15) = 63 < U(4,6) = 72 \). Burt’s refusal is wise.  
- (d) Ernie proposes trade with \( \Delta x_2 / \Delta x_1 = -3 \) (3 milk per cookie given), but Burt rejects.  

**公式内容：**  
- 效用函数： \( U(x_1, x_2) = (x_1 + 2)(x_2 + 6) \)  
- 无差异曲线方程： \( x_2 = \frac{72}{x_1 + 2} - 6 \)  
- 效用比较： \( U(1,15) = 63 < U(4,6) = 72 \)  

### 图表解析与上文知识衔接

#### **图表核心特征**  
- **坐标轴与路径**：  
  - X轴：Cookies (\(x_1\))，范围 0–16；Y轴：Glasses of milk (\(x_2\))，范围 0–16。  
  - **Blue curve**：无差异曲线通过 (4,6)，且 \(U=72\)（如 (10,0)、(7,2)、(2,12) 点验证）。  
  - **Red Line**：在 (4,6) 处的切线，斜率 \( = -2 \)（即 MRS 值）。  
  - **Black Line**：未明确定义，但根据上下文，可能为其他位置的切线（如通过 (1,15) 的切线）。  
- **凸性与 MRS 变化**：  
  - 曲线严格凸向原点（因 \( \frac{d^2 x_2}{dx_1^2} = \frac{144}{(x_1 + 2)^3} > 0 \)），满足 **边际替代率递减**。  
  - MRS 一般表达式： \( \text{MRS}(x_1, x_2) = -\frac{x_2 + 6}{x_1 + 2} \)。  
    - 在 (4,6) 处： \( \text{MRS} = -\frac{12}{6} = -2 \)（与 (a) 一致）。  
    - **关键对比上文**：相较于 Ambrose 的拟线性效用（MRS 仅依赖 \(x_1\)，如 \( -2 / \sqrt{x_1} \)），本例 **MRS 依赖 \(x_1\) 和 \(x_2\)**，符合 Cobb-Douglas 效用特征（上文提及 "如 \( U=x_1 x_2 \) 的 \( \text{MRS} = -x_2/x_1 \)"）。此处因变量偏移，形式为 \( -(x_2 + 6)/(x_1 + 2) \)，但核心逻辑一致——**偏好类型取决于 MRS 的变量结构**。  
  - **凸性含义**：当 \(x_1\) 增加（如从 4 到 10），|MRS| 递减（(4,6) 处 |MRS|=2；(10,0) 处 |MRS|= (0+6)/(10+2)=0.5），体现 "替代意愿随 \(x_1\) 增加而减弱"，与上文 "凸偏好" 定义完全一致。

#### **效用水平与交易行为**  
- **无差异曲线验证**：  
  - 点 (4,6)、(10,0)、(7,2)、(2,12) 的效用均为 72，直观印证上文 "无差异曲线代表相同效用的消费束集合"。  
  - **上文延伸**：Ambrose 案例中，无差异曲线因拟线性特性 **垂直平行移动**（\(\bar{U}\) 变化仅平移 \(x_2\) 位置）；而此处 Cobb-Douglas 变形下，曲线形状随 \(U\) 改变但保持双曲线特性，凸显 **偏好分类的操作化差异**（拟线性 vs. 互补型偏好）。  
- **离散交易与 MRS 陷阱**：  
  - 交易 (4,6) → (1,15) 后效用下降（63 < 72），因Ernie 提供的 \( \Delta x_2 / \Delta x_1 = -3 \) 虽优于边际 MRS = -2，但 **MRS 非恒定**（随 \(x_1\) 减小，|MRS| 增加）。  
    - 在 (4,6)，|MRS|=2，但完整补偿 3 单位 cookie 需 \(x_2\) 从 6 增至 18（因 \( U=72 \) 时 \( x_2 = \frac{72}{x_1 + 2} - 6 \)，代入 \(x_1=1\) 得 \(x_2=18\)），而交易仅提供 \(x_2=15\)。  
  - **上文深度协同**：  
    | 本例关键点 | 上文知识点映射 | 分析价值 |  
    |---|---|---|  
    | MRS 依赖 \(x_1, x_2\) | Cobb-Douglas 案例中的 \( \text{MRS} = -x_2/x_1 \) | 强化 **偏好类型分类工具**：通过 MRS 结构区分拟线性（MRS 仅 \(x_1\)）与本例（MRS 依赖两者），延续 "工具—应用" 链 |  
    | 交易拒绝的理性 | 边际替代率仅适用于微小变化 | 暴露 **MRS 的边际性局限** — 上文未显式讨论，但隐含于"实操化"中：消费者最优需满足 \( \text{MRS} = p_1/p_2 \)，而离散交易需精确效用计算 |  
    | 效用函数变形 | 梯度难度中的 "一般函数求导" | 演示 **偏移效用函数的 MRS 推导**：\( \text{MRS} = -\frac{\partial U/\partial x_1}{\partial U/\partial x_2} \)，衔接上文微积分环节 |  

> **核心连续性**：本例作为 Cobb-Douglas 效用的扩展，与上文 Ambrose 的拟线性案例互补，共同构建 **偏好分类的操作框架**。图表中无差异曲线的凸性及 MRS 递减，既是上文 "凸偏好" 的实证，也为后续需求推导奠定基础（如 \( \text{MRS} = p_1/p_2 \) 的切点解）。特别地，MRS 对 \(x_2\) 的依赖性，直接对照上文拟线性模型（MRS 不受 \(x_2\) 影响），清晰划分 "互补型" 与 "独立型" 替代行为 — 这正是上文所述 "将抽象理论转化为可操作分类工具" 的关键进展。

---
### Page/Slide 7



### 提取内容与解析

#### 1. 文字与公式提取
- **文字**:
  - "NAME _________ 39"
  - “Ernie, you are right that my marginal rate of substitution is −2. That means that I am willing to make small trades where I get more than 2 glasses of milk for every cookie I give you, but 9 glasses of milk for 3 cookies is too big a trade. My indifference curves are not straight lines, you see.” Would Burt be willing to give up 1 cookie for 3 glasses of milk? Yes, \( U(3,9) = 75 > U(4,6) = 72 \). Would Burt object to giving up 2 cookies for 6 glasses of milk? No, \( U(2,12) = 72 = U(4,6) \).
  - (e) On your graph, use red ink to draw a line with slope −3 through the point (4,6). This line shows all of the bundles that Burt can achieve by trading cookies for milk (or milk for cookies) at the rate of 1 cookie for every 3 glasses of milk. Only a segment of this line represents trades that make Burt better off than he was without trade. Label this line segment on your graph AB.
  - 4.4 (0) Phil Rupp’s utility function is \( U(x, y) = \max\{x, 2y\} \).
  - (a) On the graph below, use blue ink to draw and label the line whose equation is \( x = 10 \). Also use blue ink to draw and label the line whose equation is \( 2y = 10 \).
  - (b) If \( x = 10 \) and \( 2y < 10 \), then \( U(x,y) = 10 \). If \( x < 10 \) and \( 2y = 10 \), then \( U(x,y) = 10 \).
  - (c) Now use red ink to sketch in the indifference curve along which \( U(x,y) = 10 \). Does Phil have convex preferences? No.
  - 图表标签: "Blue lines", "2y=10", "Red indifference curve", "x=10"

- **公式**:
  - \( U(3,9) = 75 \), \( U(4,6) = 72 \), \( U(2,12) = 72 \)
  - \( U(x, y) = \max\{x, 2y\} \)
  - \( x = 10 \)
  - \( 2y = 10 \)
  - \( U(x,y) = 10 \)

#### 2. 图表解析
图表展示了 Phil Rupp 在效用水平 \( U = 10 \) 时的无差异曲线（红色 L 形），关联上文知识点总结中的**偏好分类框架**和**凸性条件**：

- **图表示意**：
  - **蓝色线**：\( x = 10 \)（垂直虚线）和 \( 2y = 10 \)（即 \( y = 5 \)，水平虚线）。这两条线定义了效用函数 \( U = \max\{x, 2y\} \) 的分界：当 \( x \geq 2y \) 时 \( U = x \)，当 \( 2y \geq x \) 时 \( U = 2y \)。
  - **红色无差异曲线**（对应 \( U = 10 \))：
    - **水平段**（\( x \leq 10, y = 5 \))：由 \( 2y = 10 \) 且 \( x < 10 \) 生成，表示 \( U = 2y = 10 \)。此处消费者仅消费商品 \( y \)，商品 \( x \) 未被使用。
    - **垂直段**（\( x = 10, y \leq 5 \))：由 \( x = 10 \) 且 \( 2y < 10 \) 生成，表示 \( U = x = 10 \)。此处消费者仅消费商品 \( x \)，商品 \( y \) 未被使用。
    - **拐点**（\( (10, 5) \))：消费束同时满足 \( x = 10 \) 和 \( 2y = 10 \)，效用仍为 10。
  - **非凸特性**：曲线呈 L 形向坐标轴凹陷（拐点在 \( (10,5) \))，违反凸偏好定义。

- **与上文联动分析**：
  - **对比凸性条件**：上文强调凸偏好要求曲线严格凸向原点（如 Cobb-Douglas 变形案例中 \( \frac{d^2 x_2}{dx_1^2} > 0 \)，MRS 递减）。而此处：
    - 无差异曲线在拐点处不满足凸性：连接点 \( (10,0) \) 和 \( (0,5) \) 的线段中点 \( (5,2.5) \) 满足 \( U = \max\{5,5\} = 5 < 10 \)，表明凸组合劣于原效用，**偏好非凸**（呼应答案 "No"）。
    - 这直接补充上文“偏好分类的操作化差异”——上文区分拟线性（MRS 仅依赖 \( x_1 \)) 和 Cobb-Douglas 类（MRS 依赖 \( x_1, x_2 \)），而本例属于**极值型偏好**，MRS 不连续（水平段 \( |\text{MRS}| = 0 \)，垂直段 \( |\text{MRS}| \to \infty \))，凸显效用函数结构决定偏好性质。
  - **强化离散交易逻辑**：Burt 部分（\( U(3,9)=75 > U(4,6)=72 \)）印证上文“MRS 仅适用于微小变化”：
    - MRS = -2 仅在 (4,6) 局部成立，但离散交易 1 cookie for 3 milk 使效用上升（因 \( |\Delta x_2 / \Delta x_1| = 3 > |\text{MRS}| = 2 \)，且完整交易后仍在高效用区）。
    - 对比上文交易陷阱：当离散变动大（如 3 cookies），MRS 变化导致效用下降（如上文 (4,6) → (1,15) ），但此处 1 cookie 交易幅度小，结果有效。**关键延续上文结论：理性决策需基于效用计算，而非仅 MRS 比较**。
  - **分类框架深化**：本例与上文 Cobb-Douglas 形成互补——
    - 上文案例（凸偏好）依赖 MRS 递减支撑需求理论（切点解 \( \text{MRS} = p_1/p_2 \))；
    - 本例非凸偏好则导致**角点解**（最优消费束集中在坐标轴附近），暴露 MRS 均衡条件的适用边界。这呼应上文“将抽象理论转化为可操作分类工具”，明确区分互补（Cobb-Douglas 类）、拟线性（上文 Ambrose）与极值型偏好。

---
### Page/Slide 8



### Extracted Content from Current Image

#### Textual Content:
- **Page Header**: 40 UTILITY (Ch. 4)
- **4.5 (0)** As you may recall, Nancy Lerner is taking Professor Stern’s economics course. She will take two examinations in the course, and her score for the course is the minimum of the scores that she gets on the two exams. Nancy wants to get the highest possible score for the course.  
  - (a) Write a utility function that represents Nancy’s preferences over alternative combinations of test scores $x_1$ and $x_2$ on tests 1 and 2 respectively. $U(x_1,x_2) = \min\{x_1, x_2\}$, or any monotonic transformation.
- **4.6 (0)** Remember Shirley Sixpack and Lorraine Quiche from the last chapter? Shirley thinks a 16-ounce can of beer is just as good as two 8-ounce cans. Lorraine only drinks 8 ounces at a time and hates stale beer, so she thinks a 16-ounce can is no better or worse than an 8-ounce can.  
  - (a) Write a utility function that represents Shirley’s preferences between commodity bundles comprised of 8-ounce cans and 16-ounce cans of beer. Let $X$ stand for the number of 8-ounce cans and $Y$ stand for the number of 16-ounce cans. $u(X, Y) = X + 2Y$.  
  - (b) Now write a utility function that represents Lorraine’s preferences. $u(X, Y) = X + Y$.  
  - (c) Would the function utility $U(X, Y) = 100X + 200Y$ represent Shirley’s preferences? **Yes.** Would the utility function $U(x, y) = (5X + 10Y)^2$ represent her preferences? **Yes.** Would the utility function $U(x, y) = X + 3Y$ represent her preferences? **No.**  
  - (d) Give an example of two commodity bundles such that Shirley likes the first bundle better than the second bundle, while Lorraine likes the second bundle better than the first bundle. **Shirley prefers $(0,2)$ to $(3,0)$. Lorraine disagrees.**
- **4.7 (0)** Harry Mazzola has the utility function $u(x_1, x_2) = \min\{x_1 + 2x_2, 2x_1 + x_2\}$, where $x_1$ is his consumption of corn chips and $x_2$ is his consumption of french fries.  
  - (a) On the graph below, use a pencil to draw the locus of points along which $x_1 + 2x_2 = 2x_1 + x_2$. Use blue ink to show the locus of points for which $x_1 + 2x_2 = 12$, and also use blue ink to draw the locus of points for which $2x_1 + x_2 = 12$.

#### Formulas:
- $U(x_1, x_2) = \min\{x_1, x_2\}$  
- $u(X, Y) = X + 2Y$  
- $u(X, Y) = X + Y$  
- $U(X, Y) = 100X + 200Y$  
- $U(x, y) = (5X + 10Y)^2$  
- $U(x, y) = X + 3Y$  
- $u(x_1, x_2) = \min\{x_1 + 2x_2, 2x_1 + x_2\}$  
- $x_1 + 2x_2 = 2x_1 + x_2$  
- $x_1 + 2x_2 = 12$  
- $2x_1 + x_2 = 12$

---

### Graphical Element Analysis (Based on 4.7(a))
The problem describes drawing three loci on a graph for Harry Mazzola’s utility function $u(x_1, x_2) = \min\{x_1 + 2x_2, 2x_1 + x_2\}$:  
- **Locus of $x_1 + 2x_2 = 2x_1 + x_2$** (pencil): Simplifies to $x_2 = x_1$, a 45° line through the origin. This defines the kink line where the two linear components are equal, forming the *boundary* between the two segments of the indifference curve.  
- **Blue loci**:  
  - $x_1 + 2x_2 = 12$: A downward-sloping line with intercepts $(12,0)$ and $(0,6)$.  
  - $2x_1 + x_2 = 12$: A downward-sloping line with intercepts $(6,0)$ and $(0,12)$.  

#### Interpretation of Graphical Meaning in Context of Upper Text
The blue loci ($x_1 + 2x_2 = 12$ and $2x_1 + x_2 = 12$) **define the arms of the L-shaped indifference curve** for utility level $U = 12$, analogous to the blue lines ($x = 10$ and $2y = 10$) in Phil’s case (from upper text) but with critical differences due to the $\min$ vs. $\max$ functional form:  
- **Kink location**: The blue loci intersect at $x_1 = x_2 = 4$ (solving $x_1 + 2x_2 = 12$ and $2x_1 + x_2 = 12$ simultaneously). This $(4,4)$ point is the *kink* where $u = 12$, mirroring Phil’s $(10,5)$ kink. However, for $\min\{\cdot, \cdot\}$, the kink is **convex to the origin**, while for Phil’s $\max\{x, 2y\}$ it was concave.  
- **Indifference curve structure**:  
  - For Harry, the $U = 12$ indifference curve consists of:  
    - The segment of $x_1 + 2x_2 = 12$ **where** $2x_1 + x_2 \geq 12$ (left arm, steeper slope).  
    - The segment of $2x_1 + x_2 = 12$ **where** $x_1 + 2x_2 \geq 12$ (right arm, flatter slope).  
  This forms a **convex L-shaped curve**, contrasting sharply with Phil’s *non-convex* L-shape. In Phil’s $\max$ case, bundles like $(5, 2.5)$ had $U = 5 < 10$, violating convexity; for Harry’s $\min$, convex combinations (e.g., midpoint between $(12,0)$ and $(0,12)$ is $(6,6)$ with $u = \min\{6 + 12, 12 + 6\} = 18 > 12$) *improve* utility, confirming **convex preferences** (i.e., upper contour sets are convex).  
- **MRS implications**: The blue loci represent regions where MRS is discontinuous—horizontal or vertical along the arms (e.g., $\text{MRS} = -1/2$ on the $x_1 + 2x_2 = 12$ segment when not at the kink). This differs from Phil’s $\max$ preference, where MRS was zero or infinite, but aligns with the upper text’s emphasis that **MRS monotonicity alone does not suffice for convexity**; functional form dictates preference properties. Harry’s $\min$ structure implies demand solutions may be corner-based at the kink under budget constraints, unlike Phil’s where corner solutions arose from non-convexity.  
- **Utility classification linkage**: The blue lines operationalize Harry’s *perfect-complementary-like* preference (with asymmetric coefficients), reinforcing the upper text’s framework:  
  - Phil’s $\max$ (upper text) is an **extreme substitute** with non-convexity, leading to "all-or-nothing" consumption.  
  - Harry’s $\min$ (this image) is a **generalized complement**, convex, and compatible with standard demand analysis (e.g., tangency or kink solutions).  
  This contrast highlights the **structural divide** in the classification system—substitutes (4.6) and complements (4.5, 4.7) generally yield convex preferences, while extreme cases like $\max$ do not. The discrete transaction example in 4.6(d) (where Shirley prefers $(0,2)$ over $(3,0)$) further extends the upper text’s warning: MRS-based reasoning (e.g., $|\text{MRS}| = 2$ for Shirley) must be validated with utility calculations for discrete changes, as local MRS may not hold globally.

---
### Page/Slide 9



### 提取内容  
#### 文字与公式  
- **问题 (b)**  
  - 不等式：$ x_1 + 2x_2 \geq 12 $, $ 2x_1 + x_2 \geq 12 $  
  - 点 $(8,2)$ 计算：$ 2x_1 + x_2 = 18 $, $ x_1 + 2x_2 = 12 $, 故 $ u(8,2) = 12 $  
- **问题 (c)**  
  - 指令：用黑墨水绘制 Harry 效用为 12 的无差异曲线；用红墨水绘制效用为 6 的无差异曲线。  
  - 提示：Harry Mazzola 与 Mary Granola 的相似性  
- **问题 (d)**  
  - 问题：在 $(5,2)$ 处，Harry 愿以多少单位玉米片交换 1 单位薯条？  
  - 答案：**2**  
- **4.8 (1)**  
  - 效用函数：$ U(x,y) = \min\{2x - y, 2y - x\} $（$x$: 女性数量, $y$: 男性数量）  
  - 指令：  
    - 铅笔线：$ x = y $  
    - 蓝色线：$ 2y - x = 10 $  
    - 要求点：效用 10 的点为 **(10, 10)**  
    - 条件：当 $ \min\{2x - y, 2y - x\} = 2y - x $ 时  

#### 图表元素  
- **坐标轴**：  
  - 横轴：Corn chips (0–8)  
  - 纵轴：French fries (0–8)  
- **标记线**：  
  - **Blue lines**：两组平行直线（对应 $x_1 + 2x_2 = c$ 和 $2x_1 + x_2 = c$）  
  - **Black line**：$u = 12$ 的无差异曲线  
  - **Red line**：$u = 6$ 的无差异曲线  
  - **Pencil line**：$x = y$（属于 Vanna 问题，非 Harry 核心内容）  

---

### 图表解析（结合上文知识点）  
#### 1. **无差异曲线结构与凸性验证**  
- **Black line ($u=12$)** 和 **Red line ($u=6$)** 均呈 **凸 L 型**：  
  - **Kink 点位置**：  
    - $u=12$ 时：kink 在 $(4,4)$（因 $x_1 = x_2 =4$ 满足 $x_1 + 2x_2 = 2x_1 + x_2 =12$）  
    - $u=6$ 时：kink 在 $(2,2)$  
    - *解释*：kink 点是 $x_1 + 2x_2 = 2x_1 + x_2$ 的解，即 $x_1 = x_2 = u/3$，体现 min 函数中两类互补品的平衡比例。  
  - **线性段含义**：  
    - **下方区域（$x_2 \leq x_1$）**：沿 $x_1 + 2x_2 = u$，例如 $u=12$ 时从 $(0,6)$ 到 $(4,4)$。  
      - *MRS 恒定*：$\text{MRS} = -\frac{1}{2}$（参考上文“沿 $x_1 + 2x_2 =12$ 段 MRS = $-1/2$”），表明保持效用不变时，需放弃 2 单位玉米片以换取 1 单位薯条。  
    - **上方区域（$x_1 \leq x_2$）**：沿 $2x_1 + x_2 = u$，例如 $u=12$ 时从 $(6,0)$ 到 $(4,4)$。  
      - *MRS 恒定*：$\text{MRS} = -2$，即需放弃 0.5 单位薯条换取 1 单位玉米片。  
    - *凸性关键*：在 kink 点外，MRS 在每段恒定，但方向突变，产生离散不连续（上文强调“MRS 单调性不足以保证凸性”）。  
  - **凸偏好验证**：  
    - 例如 $u=12$ 上两点 $(6,0)$ 与 $(0,6)$ 的凸组合（如中点 $(3,3)$）满足 $u(3,3) = \min\{9,9\}=9 > \min\{6,6\}=6$（低效用曲线 $u=6$ 处），效用上升。  
    - *呼应上文*：min 函数导致凸组合提高效用（“improve utility”），证实上文“凸无差异曲线”的结论。  

#### 2. **Blue lines 与区域结构**  
- **作用**：代表 $x_1 + 2x_2 = c$ 和 $2x_1 + x_2 = c$ 的水平集，是效用函数的分段基准。  
  - *上文关联*：其交点定义 kink 线，是 MRS 不连续的轨迹（“MRS 在臂上不连续”）。  
- **阴影区域（问题 (b)）**：  
  - $x_1 + 2x_2 \geq 12$ 与 $2x_1 + x_2 \geq 12$ 的交集。  
  - *经济学意义*：此区域为效用 $u \geq 12$ 的集合（因 $u = \min\{\cdot\}$ 需同时满足两项不等式）。  
  - *示例点 $(8,2)$*：虽 $2x_1 + x_2 =18 >12$，但 $x_1 + 2x_2 =12$，故 $u=12$，严格位于边界上（效用由最小约束决定）。  

#### 3. **问题 (d) 的 MRS 应用**  
- 在 $(5,2)$：  
  - $x_2 =2 < x_1=5$，位于 $x_1 + 2x_2$ 主导区域，故 $u = x_1 + 2x_2$。  
  - 由 $\text{MRS} = -\frac{1}{2}$，每增加 1 单位 $x_2$（薯条），需减少 2 单位 $x_1$（玉米片），即 **2**。  
  - *上文印证*：此例说明局部 MRS（此处为 $-1/2$）在连续段内有效，但严格依赖 min 函数的分段结构（区别于全局单调替代的线性效用）。  

#### 4. **与上文的延续性**  
- **结构分类**：  
  - 本图中 Harry 的 min 效用（广义互补）产生 **凸 L 型无差异曲线**，与上文“Phil 的 max 非凸 L 型”形成核心对比。  
  - *关键差异*：Harry 的偏好兼容标准需求分析（解可能在 kink），而 Phil 的非凸导致“全有或全无”消费。  
- **Vanna 问题的延伸**：  
  - $U = \min\{2x-y, 2y-x\}$ 与 Harry 本质相同（min 函数 + 非对称系数），体现上文“广义互补偏好”的普适性。  
  - 例如当 $x=y$ 时 $U=10$ 的点 $(10,10)$，类似 Harry 中 $x_1=x_2$ 的 kink 点。  

> **注**：图中 Pencil line 和 Vanna 部分属独立问题，但作为 min 函数的变体，进一步佐证“互补关系生成凸偏好”的理论框架（上文 4.5/4.7 章节）。

---
### Page/Slide 10



### 三、当前图片解析（Vanna 的效用问题）

#### 1. 提取文字、公式
**文字提取：**  
- 标题: `42 UTILITY (Ch. 4)`  
- 主体描述:  
  > there are (more men than women, more women than men)? **More women**. Draw a squiggly red line over the part of the blue line for which $U(x,y) = \min\{2x-y, 2y-x\} = 2y - x$. This shows all the combinations that Vanna thinks are just as good as (10,10) but where there are (more men than women, more women than men)? **More women**. Now draw a blue line along which $2x-y=10$. Draw a squiggly red line over the part of this new blue line for which $\min\{2x-y, 2y-x\} = 2x-y$. Use pencil to shade in the area on the graph that represents all combinations that Vanna likes at least as well as (10,10).  
  >  
  > $(b)$ Suppose that there are 9 men and 10 women at Vanna's party. Would Vanna think it was a better party or a worse party if 5 more men came to her party? **Worse**.  
  >  
  > $(c)$ If Vanna has 16 women at her party and more men than women, and if she thinks the party is exactly as good as having 10 men and 10 women, how many men does she have at the party? **22**. If Vanna has 16 women at her party and more women than men, and if she thinks the party is exactly as good as having 10 men and 10 women, how many men does she have at her party? **13**.  
  >  
  > $(d)$ Vanna's indifference curves are shaped like what letter of the alphabet? **V**.  
- 底部练习:  
  > `4.9 (0) Suppose that the utility functions $u(x,y)$ and $v(x,y)$ are related by $v(x,y) = f(u(x,y))$. In each case below, write "Yes" if the function $f$ is a positive monotonic transformation and "No" if it is not.`  

**公式提取：**  
- 效用函数: $U(x,y) = \min\{2x - y, 2y - x\}$  
- 边界线: $2x - y = 10$ 和 $2y - x = 10$  
- 无差异曲线分段条件:  
  - 当 $2y - x \leq 2x - y$（即 $y \leq x$）时，$U = 2y - x$  
  - 当 $2x - y \leq 2y - x$（即 $x \leq y$）时，$U = 2x - y$  

---

#### 2. 图表结合上文解析  
当前图片中的图表是 Vanna 效用问题的可视化，延续了上文 **min 函数生成凸偏好** 的核心框架。以下是基于上文知识点的关键解析（重点对比 Harry 案例，避免重复通用结论）：

##### **(1) 图表结构与上文概念映射**  
| 图表元素          | 坐标轴/线条含义                     | 上文知识点关联                                                                 |
|-------------------|-------------------------------------|--------------------------------------------------------------------------------|
| **x 轴**          | 男人数量 (men)                      | 类比 Harry 中的 $x_1$（玉米片），但此处 x 代表 "需求过量" 时的劣质品。         |
| **y 轴**          | 女人数量 (women)                    | 类比 Harry 中的 $x_2$（薯条），y 代表 "需求过量" 时的劣质品。                  |
| **(10,10) 点**    | Kink 点（效用 $U=10$）            | **kink 位置**：由 $2x-y = 2y-x$ 解得 $x=y$，且 $U = x = y$（对比 Harry 的 $x_1 = x_2 = u/3$）。此处 $u=10$ 时 kink 在 $(10,10)$，体现 **平衡比例**。 |
| **Blue lines**    | $2x-y=10$ 和 $2y-x=10$ 的水平集   | 同上文 "Blue lines" 结构，作为 **分段基准线**。其交点轨迹定义 kink 线（$x=y$），与 Harry 中 $x_1 + 2x_2 = 2x_1 + x_2$ 的作用一致。 |
| **Squiggly red lines** | $U=10$ 的实际无差异曲线         | 仅取 min 函数主导段：<br> - $y \leq x$ 时，沿 $2y-x=10$（下方区域）<br> - $x \leq y$ 时，沿 $2x-y=10$（上方区域）<br> **关键延伸**：此处系数非对称（$2x-y$ vs $2y-x$），但分段逻辑完全同 Harry（$x_1 + 2x_2$ vs $2x_1 + x_2$），验证上文 "广义互补偏好" 的普适性。 |
| **Pencil shade 区域** | $U \geq 10$ 的集合               | 即 $\begin{cases} 2x - y \geq 10 \\ 2y - x \geq 10 \end{cases}$ 的交集。<br> **经济含义**：效用由 "最小约束" 决定（如上文 $(8,2)$ 示例），此处阴影需 **严格满足双条件**，类比 Harry 的 $x_1 + 2x_2 \geq 12$ 与 $2x_1 + x_2 \geq 12$ 交集。 |

##### **(2) 线性段特性与 MRS 行为**  
- **下方区域**（$y \leq x$，即 women ≤ men）：  
  - 无差异曲线：$2y - x = 10$（如图表中 $y < x$ 部分的 red line），变形为 $x = 2y - 10$。  
  - **MRS 含义**：由 $dU = 2dy - dx = 0$ 得 $\left| \frac{dx}{dy} \right| = 2$。即 **每增加 1 单位 women，需增加 2 单位 men 以维持效用**（对比上文问题 (d) 中 "2 单位玉米片换 1 单位薯条"，此处隐含 men/women 的补偿关系）。  
  - **凸性依据**：MRS 在段内 **恒定**（无变化），但与上方区域方向突变（见下文），形成 **离散不连续**，印证上文 "MRS 单调性不足以保证凸性"。

- **上方区域**（$x \leq y$，即 men ≤ women）：  
  - 无差异曲线：$2x - y = 10$（图表中 $x < y$ 部分的 red line），变形为 $y = 2x - 10$。  
  - **MRS 含义**：$\left| \frac{dy}{dx} \right| = 2$，即 **每增加 1 单位 men，需增加 2 单位 women**。  
  - **kink 点突变**：在 $(10,10)$，MRS 从下方 $-1/2$（若定义为 $-dy/dx$）跳至上方 $-2$，与上文 Harry 案例中 MRS $-1/2$ 到 $-2$ 的突变 **结构同源**。

##### **(3) 凸偏好验证与经济学意义**  
- **问题 (c) 的数值验证**：  
  - $y=16$（women），$x > y$（men > women）→ $U = 2y - x = 10$ → $x = 22$  
  - $y=16$，$x < y$ → $U = 2x - y = 10$ → $x = 13$  
  **背面**：效用严格由 min 函数的主导项决定，**kink 点外效用由单一线性约束控制**，与上文 "效用由最小约束决定" 逻辑一致。

- **凸组合实证**：  
  以 $(22,16)$ 和 $(13,16)$ 为例（均 $U=10$），其凸组合 ($x=17.5, y=16$)：  
  - 因 $x > y$，$U = 2y - x = 32 - 17.5 = 14.5 > 10$，效用上升。  
  **呼应上文**：min 函数导致凸组合提升效用，直接证实 **凸无差异曲线**（对比 Phil 的非凸 case）。

- **形状本质**：  
  问题 (d) 中 "V" 形即 **凸 L 型**，kink 点位于平衡位置（$x=y$）。与 Harry 完全同构：  
  - Harry 的 kink 在 $x_1 = x_2 = u/3$  
  - Vanna 的 kink 在 $x = y = u$  
  **统一结论**：min 函数框架下，**非对称系数仅调整 kink 比例，不改变凸性本质**。

##### **(4) 与上文关键延续点**  
- **结构对比**：  
  - Harry 的 min 函数（$x_1, x_2$ 均为正常品）→ 互补品偏好 → **凸 L 型**  
  - Vanna 的 min 函数（$x$ 或 $y$ 过量时为劣质品）→ 平衡偏好 → **凸 L 型（V 形）**  
  **核心共性**：两者均属 **广义互补偏好**，解可能位于 kink 点，支撑标准需求分析（避免 Phil 非凸导致的 "全有或全无" 消费）。  
- **理论拓展**：  
  Vanna 是上文 "Vanna 问题" 的具象化，佐证 **min 函数对 '平衡约束' 的普适性**。例如：  
  - 当 $x=y$，效用由数量本身决定（类比 Harry 中 $x_1=x_2$ 时 $u=x_1+x_2$）；  
  - 阴影区域 $\min\{2x-y, 2y-x\} \geq 10$ 与 Harry 的 $u \geq 12$ 均要求 **双线性约束同时满足**，体现 "互补" 的强化版本。  
- **MRS 应用暗示**：  
  问题 (b) 中 $(9,10)$：因 $x<y$，$U=2x-y=8<10$；加 5 男人至 $(14,10)$，因 $x>y$，$U=2y-x=6<10$。  
  **隐含逻辑**：局部 MRS 依赖分段位置（如上文 Harry 的 $(5,2)$ 案例），但 **全局无连续 MRS**，因 kink 处不连续。

---
### Page/Slide 11



### 提取内容

#### 文字与公式
- **顶部说明**:  
  `calculus users: A differentiable function $f(u)$ is an increasing function of $u$ if its derivative is positive.)`

- **选项列表**:  
  (a) $f(u) = 3.141592u$. **Yes**.  
  (b) $f(u) = 5,000 - 23u$. **No**.  
  (c) $f(u) = u - 100,000$. **Yes**.  
  (d) $f(u) = \log_{10} u$. **Yes**.  
  (e) $f(u) = -e^{-u}$. **Yes**.  
  (f) $f(u) = 1/u$. **No**.  
  (g) $f(u) = -1/u$. **Yes**.  

- **问题描述**:  
  `4.10 (0) Martha Modest has preferences represented by the utility function $U(a,b) = ab/100$, where $a$ is the number of ounces of animal crackers that she consumes and $b$ is the number of ounces of beans that she consumes.`  
  `(a) On the graph below, sketch the locus of points that Martha finds indifferent to having 8 ounces of animal crackers and 2 ounces of beans. Also sketch the locus of points that she finds indifferent to having 6 ounces of animal crackers and 4 ounces of beans.`

- **图表标注**:  
  - 横轴：`Animal crackers`（范围 0–8）  
  - 纵轴：`Beans`（范围 0–8）  
  - 标记点：  
    - $(8,2)$: 对应 $U = (8 \times 2)/100 = 0.16$  
    - $(6,4)$: 对应 $U = (6 \times 4)/100 = 0.24$  

#### 图表结构
- **坐标系**: 2D 网格图，横轴为 $a$（animal crackers），纵轴为 $b$（beans）。  
- **曲线**:  
  - 通过 $(8,2)$ 的无差异曲线：$b = 16 / a$（因 $U = 0.16$ 时 $b = 100 \times 0.16 / a = 16 / a$）  
  - 通过 $(6,4)$ 的无差异曲线：$b = 24 / a$（因 $U = 0.24$ 时 $b = 100 \times 0.24 / a = 24 / a$）  
- **形状特征**: 两条双曲线向下倾斜、凸向原点（即向右下方弯曲），且 $U = 0.24$ 的曲线位于 $U = 0.16$ 曲线的东北方向。

---

### 图表解析（结合上文知识点）

#### 1. **无差异曲线与效用函数特性**
- **公式映射**:  
  效用函数 $U(a,b) = ab/100$ 是 **Cobb-Douglas 型**，其无差异曲线满足 $b = (100U)/a$。这与上文知识点总结中 **min 函数框架形成对比**：
  - 上文 min 函数（如 $U = \min\{2x - y, 2y - x\}$）产生 **分段线性无差异曲线**（带 kink 点），而此处曲线完全 **平滑连续**，无 kink。
  - 核心差异：上文 min 函数代表 **强互补偏好**（需精确比例），此处 Cobb-Douglas 代表 **标准替代品偏好**（可按比例替代，但 MRS 递减）。

- **凸性体现**:  
  - 曲线凸向原点，表明 **严格凸偏好**。这与上文验证的 **凸偏好共性一致**：  
    - 上文通过 min 函数的凸组合实证（如 $(22,16)$ 与 $(13,16)$ 的组合提升效用）佐证凸性。  
    - 此处类似：取同一条无差异曲线上的两点（如 $(8,2)$ 与 $(2,8)$），其凸组合（如 $(5,5)$ 处 $U=0.25 > 0.16$）必然进入更高效用区域，**再次确认凸组合提升效用**。  
  - 与上文延续：尽管机制不同（min 函数依赖 kink，Cobb-Douglas 依赖指数函数），但 **二者均为凸偏好拓扑**，避免非凸偏好（如 Phil 案例）导致的需求不连续问题。

#### 2. **MRS 行为与经济学含义**
- **MRS 公式**:  
  边际替代率 $| \text{MRS} | = \left| \frac{db}{da} \right| = b / a$（由 $dU = \frac{b}{100} da + \frac{a}{100} db = 0$ 推导）。  
  - **关键特征**: $| \text{MRS} |$ 沿曲线 **连续递减**。例如：  
    - 在 $(8,2)$ 处，$| \text{MRS} | = 2/8 = 0.25$（少消费 1 单位 animal crackers，只需增加 0.25 单位 beans 维持效用）；  
    - 在 $(4,4)$ 处，$| \text{MRS} | = 1$；  
    - 在 $(2,8)$ 处，$| \text{MRS} | = 4$。  
  - **与上文对比**:  
    - 上文 min 函数中，MRS 在分段内 **恒定**（如下方区域 $|dx/dy| = 2$），但在 kink 点 $(10,10)$ **离散突变**（从 $-1/2$ 跳至 $-2$）。  
    - 此处 MRS **全程连续变化**，无突变，印证上文判断：**仅当效用函数不可微时（如 min 函数），MRS 才可能出现不连续**。  
  - **行为意义**: MRS 递减反映 **边际替代率递减定律**，消费者更愿用充裕品替代稀缺品（如 animal crackers 少时，beans 需多量补偿），这与上文 min 函数的 **补偿逻辑（如 2 单位 men 换 1 单位 women）** 形成互补视角—后者强调固定补偿比，前者体现动态优化。

#### 3. **图表变化对需求分析的延续**
- **kink 点缺失的启示**:  
  上文强调 min 函数的 **kink 点 $(10,10)$ 是效用最大化核心**（均衡常在此处），而此处无 kink，均衡点由 **预算线切点** 决定。但二者均满足 **凸偏好下标准需求解存在性**（上文已指出 min 函数避免 "全有或全无" 消费）。
  
- **效用水平差异的解读**:  
  - $U=0.24$ 曲线（通过 $(6,4)$）高于 $U=0.16$ 曲线（通过 $(8,2)$），呼应上文 **阴影区域 $\min\{2x-y, 2y-x\} \geq 10$ 表示高无差异集** 的逻辑。  
  - 局部 MRS 的依赖性：上文问题 (b) 中 $(9,10)$ 效用 $U<10$ 因分段规则，此处类似—在 $(6,4)$，$| \text{MRS} | = 4/6 \approx 0.67$；若移至 $(10,0)$，$| \text{MRS} | \to \infty$，**但全局无断层**，体现凸函数的 **微分结构优势**。

- **理论拓展点**:  
  此案例将上文 **min 函数对 "平衡约束" 的普适性** 扩展至连续框架：  
  - Min 函数隐含 **硬性比例约束**（如 $x=y$ 时 kink）；  
  - Cobb-Douglas 隐含 **软性比例偏好**（最优消费比 $a/b = \text{constant}$），但两者均属 **广义凸偏好谱系**，支撑比较静态分析（如价格变动导致最优解平滑移动）。  
  **统一结论**：无论分段线性或平滑函数，**凸无差异曲线是标准消费者选择理论的核心前提**，本图正是该原理的规范实证。

---
### Page/Slide 12



### 当前图片解析

#### 1. 提取文字与公式
- **标题及页码**：44 UTILITY (Ch. 4)  
- **问题 (b)**：  
  Bertha Brassy has preferences represented by the utility function $V(a,b) = 1,000a^2b^2$, where $a$ is the number of ounces of animal crackers and $b$ is the number of ounces of beans. Sketch the locus of points indifferent to $(8,2)$ and to $(6,4)$.  
- **图表信息**：  
  - 横轴：Animal crackers (0 to 8)  
  - 纵轴：Beans (0 to 8)  
  - 标记点：$(8,2)$ 和 $(6,4)$  
  - 无差异曲线：两条平滑凸向原点的曲线，分别通过 $(8,2)$ 和 $(6,4)$  
- **问题 (c)**：  
  Are Martha’s preferences convex? **Yes.** Are Bertha’s? **Yes.**  
- **问题 (d)**：  
  What can you say about the difference between the indifference curves for Bertha and Martha? **There is no difference.**  
- **问题 (e)**：  
  How could you tell without drawing? **Their utility functions only differ by a monotonic transformation.**  
- **问题 4.11 (0)**：  
  Willy Wheeler’s preferences: $U(x_1,x_2) = x_1^2 + x_2^2$.  
  - Part (a): Draw indifference curves. What kind? **Quarter circles centered at the origin.** Convex preferences? **No.**  

#### 2. 图表变化含义解析  
当前图表展示 Bertha 的无差异曲线，结合上文知识点（Cobb-Douglas 偏好），重点说明三点延续性：  

##### **(1) 曲线形态与凸性验证**  
- 图表中无差异曲线 **平滑连续且凸向原点**，无 kink 点。这直接印证上文结论：  
  - Cobb-Douglas 效用函数（$V(a,b) = 1,000a^2b^2$ 等价于 $U \propto (ab)^2$）生成 **严格凸偏好**，与上文 $U = ab/100$ 案例机制一致。  
  - 凸性体现为：取曲线两点（如 $(8,2)$ 和 $(6,4)$ 的凸组合，如 $(7,3)$），其效用高于原曲线（计算验证：$V(7,3) = 1,000 \times 49 \times 9 = 441,000 > V(8,2) = 256,000$），符合上文“凸组合必进入更高效用区域”的共性。  
- **关键延续**：上文强调 min 函数依赖 kink 点体现凸性，而此图通过平滑曲线验证凸偏好 **无需分段机制**，进一步说明凸性是两类函数的拓扑共性。  

##### **(2) MRS 动态与上文对比**  
- 图表中曲线递减斜率隐含 **MRS 连续递减**，与上文分析无缝衔接：  
  - 对 $V(a,b) = 1,000a^2b^2$，MRS 计算式为 $|\text{MRS}| = \frac{b}{a}$（由 $dV = 0$ 推导）。  
    - 在 $(8,2)$ 处：$|\text{MRS}| = 2/8 = 0.25$  
    - 在 $(6,4)$ 处：$|\text{MRS}| = 4/6 \approx 0.67$  
  - 此变化规律直接延续上文 $U = ab/100$ 的 MRS 行为：**无突变、沿曲线连续衰减**，再次佐证  
    > 仅当效用函数不可微（如 min 函数）时，MRS 才可能不连续。  
- **行为意义延伸**：MRS 递减反映消费者动态替代逻辑（充裕品替代稀缺品需更少补偿），与上文 min 函数的固定补偿比形成对比—此处 (d) 和 (e) 问题指出 Bertha 与 Martha 偏好无差异，根源在于其效用函数是单调变换（如 $V = k(U_{\text{Martha}})^2$），故 MRS 完全一致，无需重复验证。  

##### **(3) 非凸案例的警示作用**  
- Willy Wheeler 部分（$U = x_1^2 + x_2^2$）的 **非凸性** 与主图表形成鲜明对比：  
  - 无差异曲线为“四分之一圆”，但其高无差异集 $\{ (x_1,x_2) \mid x_1^2 + x_2^2 \geq u \}$ 非凸（例如凸组合 $(0.5,0.5)$ 从 $(1,0)$ 和 $(0,1)$ 处移出高无差异集）。  
  - 这直接呼应上文“Phil 案例”：**非凸偏好破坏需求连续性**，而 Bertha 的凸偏好确保持效需求解存在（如图表中均衡由预算线切点决定）。  
- **理论闭环**：主图表（凸）与 Willy 案例（非凸）并置，强化上文核心结论—  
  > **凸无差异曲线是消费者选择理论的必要前提**，无论函数形式（分段线性或平滑）。  

---  
*注：本解析避免复述上文已论证的 Cobb-Douglas 属性（如 MRS 规律），聚焦当前图片如何实证性延续凸偏好框架，并衔接单调变换、非凸风险等关键延伸。*

---
### Page/Slide 13



### 当前图片内容提取

#### 所有文字与公式
- **页眉**：`NAME _________ 45`
- **问题标题**：`Calculus 4.12 (0)`
- **效用函数**：
  - Joe Bob 的效用函数：\( u(x_1, x_2) = x_1^2 + 2x_1x_2 + x_2^2 \)
- **问题 (a)**：
  - “Compute Joe Bob’s marginal rate of substitution: \( MRS(x_1, x_2) = -1 \).”
- **问题 (b)**：
  - “Joe Bob’s straight cousin, Al, has a utility function \( v(x_1, x_2) = x_2 + x_1 \).”
  - “Compute Al’s marginal rate of substitution. \( MRS(x_1, x_2) = -1 \).”
- **问题 (c)**：
  - “Do \( u(x_1, x_2) \) and \( v(x_1, x_2) \) represent the same preferences? Yes.”
  - “Can you show that Joe Bob’s utility function is a monotonic transformation of Al’s? (Hint: Some have said that Joe Bob is square.) Notice that \( u(x_1, x_2) = [v(x_1, x_2)]^2 \).”
- **后续问题**：
  - “4.13 (0) The idea of assigning numerical values to determine a preference ordering over a set of objects is not limited in application to commodity bundles. The Bill James Baseball Abstract argues that a baseball player’s batting average is not an adequate measure of his offensive productivity. Batting averages treat singles just the same as extra base hits. Furthermore they do not give credit for “walks,” although a walk is almost as good as a single. James argues that a double in two at-bats is better than a single, but not as good as two singles. To reflect these considerations, James proposes the following index, which he calls “runs created.” Let A be the number of hits plus the number of walks that a batter gets in a season. Let B be the number of total bases that the batter gets in the season. (Thus, if a batter has S singles, W walks, D doubles, T triples, and H” (内容截断)

#### 图表描述
- **坐标系**：横轴 \( x_1 \)（范围 0–8），纵轴 \( x_2 \)（范围 0–8），网格背景。
- **曲线特征**：三条无差异曲线凸向原点（bowed inward），形状平滑连续，无 kink 点。

---

### 图表变化含义解析（基于上文知识点连续性）

#### (1) 图表与理论的一致性及矛盾点
- **图表形态**：曲**线凸向原点**，表面符合上文强调的 **凸偏好特征**（如 Bertha 的 Cobb-Douglas 偏好），隐含 **MRS 沿曲线连续递减**。这与上文知识点中“凸无差异曲线是消费者选择理论必要前提”呼应，尤其支持 **严格凸偏好保证需求解存在**（如预算线切点唯一）。
- **矛盾点**：  
  当前问题 4.12 的效用函数 \( u = (x_1 + x_2)^2 \) 和 \( v = x_1 + x_2 \) 代表 **完全替代偏好**（MRS 恒为 -1），无差异曲线应为 **直线**（斜率固定），而非图表所示的凸曲线。  
  **理论解释**：  
  - 单调变换（\( u = v^2 \)）不改变偏好顺序及曲线形状，但此处基础偏好（\( v = x_1 + x_2 \)）是线性，故曲线必为直线。图表的凸性形态 **与本题数学逻辑冲突**，可能为教材通用插图（如用于展示一般凸偏好），但非针对性刻画。  
  - 上文知识点中，Bertha 与 Martha 的效用函数仅差单调变换，故无差异曲线相同；此处 Joe Bob 与 Al 同理，但偏好类型（完全替代）与图表形态不匹配，突显 **凸性并非所有偏好共性**——线性偏好虽弱凸，但无曲线弯曲。

#### (2) MRS 行为与单调变换的延续
- **MRS 常数 vs 递减**：  
  图表隐含 MRS 递减（凸曲线典型特征），但问题 4.12 中 MRS 恒为 -1，表明 **偏好非严格凸**。这直接延续上文结论：  
  - 仅当效用函数可微且非线性（如 Cobb-Douglas）时，MRS 才连续递减；  
  - 此处 \( v = x_1 + x_2 \) 不可微（沿曲线斜率不变），故 MRS 无动态变化，与上文 min 函数案例（MRS 固定但 kink 点导致不连续）形成对比。  
- **单调变换的实践验证**：  
  问题 (c) 明确 \( u = [v]^2 \) 是单调变换，印证上文 (d)(e) 问题核心：  
  > **效用函数差异若仅来自单调变换，无差异曲线与 MRS 完全一致**。  
  本例中 MRS 均为 -1，实证该原理——变换（平方）仅放大效用值，不改变边际替代逻辑。

#### (3) 非凸风险的警示（与上文 Willy Wheeler 案例联动）
- **图表凸性 vs 本题线性偏好**：  
  图表所绘凸曲线若代表严格凸偏好（如 Cobb-Douglas），则确保持效需求解；但 4.12 的线性偏好虽弱凸，**高无差异集仍凸**（因直线边界），故需求解存在。  
- **关键区分**：  
  此处 vs Willy Wheeler 案例（\( U = x_1^2 + x_2^2 \)，非凸）：  
  - 本题线性偏好：高无差异集凸（凸组合仍在集内），需求连续；  
  - Willy 案例：高无差异集非凸（如凸组合 \( (0.5,0.5) \) 脱离 \( U \geq 1 \)），破坏需求存在性。  
  图表凸性强化上文闭环：  
  > **凸性保需求解，但严格性（平滑 vs 有 kink）仅影响刻画方式，不破坏理论基础**。  
  4.12 的常数 MRS 虽无“动态替代”，但偏好凸性仍支撑需求理论——区别仅在于非严格凸（直线）下均衡可能不唯一。

---

*注：解析聚焦图片内容与上文理论的衔接，未复述已知凸偏好机制（如 Cobb-Douglas 的 MRS 计算），但凸显单调变换对偏好等价性的决定性作用，以及凸性条件在需求理论中的普适必要性。*

---
### Page/Slide 14



### 提取当前图片中的所有文字、公式  
#### 文字内容  
- **页眉**：46 UTILITY (Ch. 4)  
- **定义段落**：  
  > home runs, then \( A = S + D + T + H + W \) and \( B = S + W + 2D + 3T + 4H \). Let \( N \) be the number of times the batter bats. Then his index of runs created in the season is defined to be \( AB/N \) and will be called his \( RC \).  
- **(a)** In 1987, George Bell batted 649 times. He had 39 walks, 105 singles, 32 doubles, 4 triples, and 47 home runs. In 1987, Wade Boggs batted 656 times. He had 105 walks, 130 singles, 40 doubles, 6 triples, and 24 home runs. In 1987, Alan Trammell batted 657 times. He had 60 walks, 140 singles, 34 doubles, 3 triples, and 28 home runs. In 1987, Tony Gwynn batted 671 times. He had 82 walks, 162 singles, 36 doubles, 13 triples, and 7 home runs. We can calculate \( A \), the number of hits plus walks, \( B \) the number of total bases, and \( RC \), the runs created index for each of these players. For Bell, \( A = 227 \), \( B = 408 \), \( RC = 143 \). For Boggs, \( A = 305 \), \( B = 429 \), \( RC = 199 \). For Trammell, \( A = 265 \), \( B = 389 \), \( RC = 157 \). For Gwynn, \( A = 300 \), \( B = 383 \), \( RC = 171 \).  
- **(b)** If somebody has a preference ordering among these players, based only on the runs-created index, which player(s) would she prefer to Trammell?  
  > Boggs and Gwynn.  
- **(c)** The differences in the number of times at bat for these players are small, and we will ignore them for simplicity of calculation. On the graph below, plot the combinations of \( A \) and \( B \) achieved by each of the four players. Draw four "indifference curves," one through each of the four points you have plotted. These indifference curves should represent combinations of \( A \) and \( B \) that lead to the same number of runs-created.  

#### 公式与关键数值  
- **核心公式**：  
  \[
  A = S + D + T + H + W, \quad B = S + W + 2D + 3T + 4H, \quad RC = \frac{AB}{N}
  \]  
- **球员数据**：  
  | Player    | \( A \) | \( B \) | \( RC \) |  
  |-----------|---------|---------|----------|  
  | Bell      | 227     | 408     | 143      |  
  | Boggs     | 305     | 429     | 199      |  
  | Trammell  | 265     | 389     | 157      |  
  | Gwynn     | 300     | 383     | 171      |  

---

### 图表解析  
#### 图表描述  
- **坐标系**：  
  - 横轴：*Number of hits plus walks* (\( A \), range 0–360)  
  - 纵轴：*Number of total bases* (\( B \), range 0–480)  
- **数据点**：  
  - Bell: \((227, 408)\)  
  - Trammell: \((265, 389)\)  
  - Gwynn: \((300, 383)\)  
  - Boggs: \((305, 429)\)  
- **曲线特征**：  
  四条无差异曲线凸向原点（bowed inward），平滑连续且无 kink 点（对应问题 (c) 要求），每条曲线通过一个数据点。  

---

### 变化含义解析（立足上文知识点连续性）  
#### (1) 无差异曲线凸性的理论根源  
- **公式映射**：  
  由 \( RC = \frac{AB}{N} \) 且 \( N \) 被忽略（问题 (c) 假设），**效用函数等价于 \( u(A, B) = AB \)** —— 这是 **Cobb-Douglas 偏好**的典型形式（权重均为 1）。  
- **凸性成因**：  
  - 该效用函数满足 **严格凸性**，因 Hessian 矩阵负定；无差异曲线由 \( AB = \text{constant} \) 定义（双曲线），自然凸向原点。  
  - 此结果**严格承接上文 Bertha 的 Cobb-Douglas 偏好案例**：  
    > 无差异曲线凸性是 MRS 递减的几何表现，此处 \( \text{MRS} = -\frac{B}{A} \) 沿曲线递减（\( A \) 增时 \( B \) 减，\( |\text{MRS}| \) 下降），确保需求解唯一。  
  - **与上文矛盾点的区分**：  
    本题无完全替代偏好冲突（如上文 4.12 问题），因 \( u = AB \) 与 \( u = x_1 + x_2 \) 结构迥异：  
    - 后者 MRS 恒为 -1（直线），前者 MRS 动态变化（曲线）。  
    - 教材图表此处**精准匹配理论**，未出现上文所述“通用插图误用”问题。  

#### (2) 理论实践：偏好序与无差异曲线层级  
- **无差异曲线层级**：  
  曲线从内到外对应 \( RC \) 递增（Bell → Trammell → Gwynn → Boggs），因 \( AB \) 值：  
  \[
  \text{Bell: } 227 \times 408 = 92,616 \quad < \quad \text{Trammell: } 265 \times 389 = 103,085 \quad < \quad \text{Gwynn: } 300 \times 383 = 114,900 \quad < \quad \text{Boggs: } 305 \times 429 = 130,845
  \]  
  直接验证 **高无差异集凸性**：对任意两点凸组合，\( AB \) 值更高（因 \( u = AB \) 为拟凹函数），符合上文“凸偏好支撑需求理论”的核心结论。  
- **偏好序应用（问题 (b)）**：  
  - Trammell 的 \( RC = 157 \) 对应 \( AB \approx 103,085 \)。  
  - Boggs (\( RC = 199 \)) 和 Gwynn (\( RC = 171 \)) 位于更高无差异曲线，故 **严格偏好于 Trammell** —— 直接体现 **效用函数刻画偏好序** 的原理（上文知识点核心）。  

#### (3) 单调变换的隐性验证  
- **RC 与效用等价性**：  
  - 忽略 \( N \) 时，\( RC \propto AB \)，即 \( RC \) 是 \( u(A,B) = AB \) 的**单调变换**（正比例变换）。  
  - 这**实证上文关键结论**：  
    > 效用函数差异仅来自单调变换时，无差异曲线与 MRS 完全一致。  
  - 例如，若定义 \( v(A,B) = \log(AB) \)，则 \( v \) 与 \( u \) 生成相同无差异曲线，且 MRS 恒为 \( -B/A \)，印证变换不改变边际替代逻辑。  

---

### 理论闭环强化  
- 本题中 \( u = AB \) 严格满足 **凸偏好** 条件，故：  
  1. 无差异曲线凸性 → 消费者优化有唯一解（如预算约束切点）；  
  2. 与上文 Willy Wheeler 非凸案例（\( U = x_1^2 + x_2^2 \)) 形成对照：**此处高无差异集凸性保障需求存在性**。  
- **关键延伸**：  
  棒球数据将抽象效用理论具象化 —— \( A \) 和 \( B \) 作为“商品”，\( RC \) 作为效用指标，自然导出 MRS = \( -B/A \) 的替代率递减规律，**无缝延续上文“凸性是需求理论必要前提”的主线**。

---
### Page/Slide 15



### 提取图片中的文字与公式  
**文字内容**：  
- 顶部标识：`NAME _________ 47`  
- 问题编号：`4.14 (0) This problem concerns the runs-created index discussed in the preceding problem. Consider a batter who bats 100 times and always either makes an out, hits for a single, or hits a home run.`  
- 部分 (a)：`Let \( x \) be the number of singles and \( y \) be the number of home runs in 100 at-bats. Suppose that the utility function \( U(x,y) \) by which we evaluate alternative combinations of singles and home runs is the runs-created index. Then the formula for the utility function is \( U(x,y) = (x + y)(x + 4y)/100 \).`  
- 部分 (b)：`Let’s try to find out about the shape of an indifference curve between singles and home runs. Hitting 10 home runs and no singles would give him the same runs-created index as hitting 20 singles and no home runs. Mark the points (0,10) and (x,0), where \( U(x,0) = U(0,10) \).`  
- 部分 (c)：`Where \( x \) is the number of singles you solved for in the previous part, mark the point \( (x/2, 5) \) on your graph. Is \( U(x/2, 5) \) greater than or less than or equal to \( U(0,10) \)? Greater than. Is this consistent with the batter having convex preferences between singles and home runs? Yes.`  
- 图表标注：`Preference direction`（指向右上），坐标轴标签 `Home runs`（Y轴，0–20），`Singles`（X轴，0–20）  

**公式**：  
- 效用函数： \( U(x, y) = \dfrac{(x + y)(x + 4y)}{100} \)  
- 比较条件： \( U(x, 0) = U(0, 10) \)  

**图表关键点**：  
- 点标记： \((0,10)\)、\((10,5)\)、\((20,0)\)  
- 三条无差异曲线：  
  - 内侧曲线通过 \((0,10)\) 和 \((20,0)\)（\( U = 4 \)）  
  - 中间曲线通过 \((10,5)\)（\( U = 4.5 \)）  
  - 外侧曲线（图中未显式标记，但由偏好方向隐含）  

---

### 图表变化含义解析（衔接上文知识点）  
#### (1) 效用函数结构与凸性验证  
- **非标准Cobb-Douglas形式的凸性延伸**：  
  此效用函数 \( U(x,y) = \frac{(x+y)(x+4y)}{100} \) 非简单乘积形式（如上文 \( u = AB \)），但展开后 \( U = \frac{x^2 + 5xy + 4y^2}{100} \) 仍满足 **拟凹性**（关键上文结论）：  
  - 凸组合验证：点 \((10,5)\) 是 \((0,10)\) 与 \((20,0)\) 的凸组合（因 \( x = \frac{0+20}{2} \), \( y = \frac{10+0}{2} \)），且 \( U(10,5) = 4.5 > 4 = U(0,10) \)，**直接实证凸偏好**。  
  - 与上文逻辑一致：此现象延续了"高无差异集凸性是需求解唯一性的必要前提"（见上文"理论闭环强化"部分），但此处通过二次函数结构复现，表明凸性不依赖特定偏好形式。  

#### (2) MRS递减的几何表现  
- **MRS动态变化与曲线凸性**：  
  - 计算 MRS：  
    \[
    \text{MRS} = -\frac{\partial U/\partial x}{\partial U/\partial y} = -\frac{2x + 5y}{5x + 8y}
    \]  
  - 沿无差异曲线（如 \( U=4 \)）移动：  
    - 在 \((0,10)\)： \( |\text{MRS}| = \frac{5}{8} = 0.625 \)  
    - 在 \((20,0)\)： \( |\text{MRS}| = \frac{40}{100} = 0.4 \)  
    - **绝对值递减**，与曲线凸向原点完全匹配。  
  - **承袭上文核心机制**：如上文所述（"MRS 递减是凸性的几何表现"），此处替代率递减规律强化了"凸偏好支撑唯一需求解"的理论连续性——与上文 Bertha 的 Cobb-Douglas 案例互为印证，但揭示更一般化效用函数的普适性。  

#### (3) 消费者理论的实践映射  
- **偏好序层级化**：  
  - 图表中三条曲线从内到外对应效用递增（内侧 \( U=4 \) → 外侧 \( U>4.5 \)），**严格遵循上文无差异曲线层级逻辑**：  
    \[
    U(0,10) = U(20,0) = 4 < U(10,5) = 4.5
    \]  
  - 与上文 "RC 指标等价效用" 一致：此处 \( U \) 作为 runs-created index，是效用的单调变换（比例缩放），故无差异曲线形态不变（见上文"单调变换隐性验证"）。  
- **需求理论必要性重申**：  
  偏好方向箭头指向右上，表明效用随 \( x,y \) 增加而上升。结合凸性，确保消费者优化（如预算约束切点）存在唯一解——**呼应上文"非凸案例（\( U = x_1^2 + x_2^2 \)）的反例"，凸显凸性作为需求理论支柱的不可替代性**。  

> **关键延续**：本题以棒球实践具象化抽象凸性原理，无缝衔接上文主线——从 Cobb-Douglas 的 \( u=AB \) 到二次效用函数，凸性始终是 MRS 递减与需求唯一解的共同内核。

---
### Page/Slide 16



### 当前图片解析  

#### 1. 文字与公式提取  
- **文字内容**：  
  ```  
  48 UTILITY (Ch. 4)  
  ```  
- **公式**：无（图片仅含章节标题与页码）。  

---

#### 2. 与上文知识点的连续性说明  
- **章节定位**：  
  - 该图片为教材第 4 章“UTILITY”开篇页码（第 48 页），直接承接上文对**凸偏好**、**无差异曲线层级**及**MRS 递减规律**的分析。  
  - 上文已通过具体效用函数 $ U(x,y) = \frac{(x+y)(x+4y)}{100} $ 验证凸性及其对需求唯一性的支撑作用（例如点 $(10,5)$ 的效用 $ U=4.5 $ 严格高于边界点 $(0,10)$ 和 $(20,0)$ 的 $ U=4 $），本页作为理论展开的起始标识，隐含后续内容将延续“效用函数—无差异曲线—偏好性质”的逻辑主线。  

- **理论衔接点**：  
  - 上文核心结论已明确 **凸偏好是需求理论成立的必要条件**（非凸案例如 $ U = x_1^2 + x_2^2 $ 可导致多重解），本页的“UTILITY (Ch. 4)”标志着理论从“偏好描述”向“效用函数化”与“消费者优化”的推进，与上文的棒球实践案例形成方法论闭环——  
    > *从具体情境（棒球选择）提炼抽象原理（凸性），再回归一般效用函数框架（Chapter 4）*。  
  - 页码“48”暗示教材已系统构建消费者理论基石（如第 3 章偏好公理），本章将进一步通过效用函数严格化上文的**拟凹性论证**（如 MRS 递减与无差异曲线凸性）。  

---

#### 3. 无新增图表解析  
- 本图片无图表或公式，故无需补充几何含义。其核心作用为**章节导航**，为后续内容（如效用函数单调变换、边际替代率计算、预算约束优化）提供逻辑定位，与上文知识点构成“问题—验证—拓展”链条。
