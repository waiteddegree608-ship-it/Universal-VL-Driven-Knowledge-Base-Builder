# PDF_Quiz_4

### Page/Slide 1



# 题目解析

## 文字与公式提取

- **标题**：Quiz 4, Utility  
- **问题4.1**：  
  - 效用函数：$ U(x_A, x_B) = x_A x_B $  
  - 条件：无差异曲线通过点（10 apples, 30 bananas），求消费2 apples时的bananas数量  
  - 选项：(a) 25 bananas；(b) 50 bananas；(c) 152 bananas；(d) 158 bananas；(e) 150 bananas  
- **问题4.2**：  
  - 效用函数：$ U(A, B) = AB $  
  - 条件：消费点（20 apples, 100 bananas），苹果横轴、香蕉纵轴，求无差异曲线斜率  
  - 选项：(a) $-20$；(b) $-5$；(c) $-10$；(d) $-1/5$；(e) $-1/10$  
- **问题4.3**：  
  - 效用函数：$ U(x_1, x_2) = 4x_1^{1/2} + x_2 $  
  - 条件：初始消费（81 units of nuts, 14 units of berries），求增加40 units nuts时最多放弃的berries数量  
  - 选项：(a) 11；(b) 25；(c) 8  

---

## 题目解析

### 4.1 无差异曲线的效用等值性  
无差异曲线上的点具有相同效用值。已知效用函数 $ U = x_A x_B $，点 $ (10, 30) $ 的效用为：  
$$
U = 10 \times 30 = 300
$$  
当 $ x_A = 2 $ 时，保持效用不变需满足 $ 2 \cdot x_B = 300 $，解得 $ x_B = 150 $。  
**结论**：正确答案为 **(e)**。

---

### 4.2 边际替代率（MRS）的几何意义  
无差异曲线斜率由边际替代率 $ MRS = -\frac{MU_A}{MU_B} $ 决定，其中：  
- $ MU_A = \frac{\partial U}{\partial A} = B $（苹果的边际效用）  
- $ MU_B = \frac{\partial U}{\partial B} = A $（香蕉的边际效用）  

在消费点 $ (20, 100) $ 处：  
$$
MRS = -\frac{B}{A} = -\frac{100}{20} = -5
$$  
**结论**：正确答案为 **(b)**。

---

### 4.3 效用守恒下的替代量计算  
目标为保持效用不变时，新增40 units nuts（即 $ x_1 $ 从81增至121）所需的berries最小保留量：  
1. **初始效用**：  
   $$
   U = 4\sqrt{81} + 14 = 4 \times 9 + 14 = 50
   $$  
2. **新增坚果后的效用约束**：  
   $$
   4\sqrt{121} + x_2' = 50 \implies 4 \times 11 + x_2' = 50 \implies x_2' = 6
   $$  
3. **可放弃berries数量**：  
   $$
   14 - 6 = 8
   $$  
**结论**：最大放弃量为 **8**，正确答案为 **(c)**。

---
### Page/Slide 2



# 题目解析

## 文字与公式提取

- **标题**：448 UTILITY (Ch. 4)  
- **问题4.4**：  
  - 背景：Joe Bob 的堂兄 Jonas 消费商品1和2，Jonas 认为2单位商品1总是3单位商品2的完美替代品。  
  - 问题：以下哪个效用函数**唯一**不能代表 Jonas 的偏好？  
  - 选项：  
    (a) $ U(x_1, x_2) = 3x_1 + 2x_2 + 1,000 $  
    (b) $ U(x_1, x_2) = 9x_1^2 + 12x_1 x_2 + 4x_2^2 $  
    (c) $ U(x_1, x_2) = \min\{3x_1, 2x_2\} $  
    (d) $ U(x_1, x_2) = 30x_1 + 20x_2 - 10,000 $  
    (e) More than one of the above does NOT represent Jonas’s preferences.  
- **问题4.5**：  
  - 背景：Harry Mazzola 的效用函数 $ U(x_1, x_2) = \min\{x_1 + 2x_2, 2x_1 + x_2\} $，收入 $40，玉米片价格 $5/单位，薯条价格 $5/单位。  
  - 问题：Harry 将如何消费？  
  - 选项：  
    (a) definitely spend all of his income on corn chips.  
    (b) definitely spend all of his income on french fries.  
    (c) consume at least as much corn chips as french fries, but might consume both.  
    (d) consume at least as much french fries as corn chips, but might consume both.  
    (e) consume equal amounts of french fries and corn chips.  
- **问题4.6**：  
  - 背景：Ethel 的效用函数 $ U(x, y) = \min\{2x + y, 3y\} $，$x$ 为横轴（水平轴），$y$ 为纵轴（垂直轴）。  
  - 问题：她的无差异曲线形状？  
  - 选项：  
    (a) consist of a vertical line segment and a horizontal line segment which meet in a kink along the line $ y = 2x $.  
    (b) consist of a vertical line segment and a horizontal line segment which meet in a kink along the line $ x = 2y $.  
    (c) consist of a horizontal line segment and a negatively sloped line segment which meet in a kink along the line $ x = y $.  
    (d) consist of a positively sloped line segment and a negatively sloped line segment which meet along the line $ x = y $.  
    (e) consist of a horizontal line segment and a positively sloped line segment which meet in a kink along the line $ x = 2y $.  

---

## 题目解析

### 4.4 完美替代品的效用函数验证  
Jonas 偏好要求商品1与商品2为完美替代品，替换比例为2:3（即2单位商品1等价于3单位商品2）。这隐含边际替代率（MRS）为常数，且 $ | \text{MRS} | = \frac{3}{2} $。  
- **效用函数特征**：完美替代品需为线性形式 $ U = \alpha x_1 + \beta x_2 $（或其单调变换），其中 $ \frac{\alpha}{\beta} = \frac{3}{2} $。  
  - 选项 (a) $ U = 3x_1 + 2x_2 + 1,000 $：$ \text{MRS} = -\frac{3}{2} $，符合替换比例。  
  - 选项 (b) $ U = 9x_1^2 + 12x_1 x_2 + 4x_2^2 = (3x_1 + 2x_2)^2 $：为单调变换（平方函数），偏好与线性形式一致，MRS 相同。  
  - 选项 (c) $ U = \min\{3x_1, 2x_2\} $：表示完美互补品，要求 $ 3x_1 = 2x_2 $（即固定比例 $ x_1:x_2 = 2:3 $），与替代关系矛盾。  
  - 选项 (d) $ U = 30x_1 + 20x_2 - 10,000 $：$ \text{MRS} = -\frac{30}{20} = -\frac{3}{2} $，与 (a) 比例相同（线性缩放）。  
- **关键区分**：(c) 的 min 函数导致 L 形无差异曲线（kink 处），而完美替代品需为直线无差异曲线。仅 (c) 不能代表 Jonas 的偏好。  
**结论**：正确答案为 **(c)**。  

### 4.5 完美互补品的最优预算分配  
Harry 的效用函数 $ U = \min\{x_1 + 2x_2, 2x_1 + x_2\} $ 表示商品间存在固定搭配关系，最优消费位于无差异曲线 kink 处，即：  
$$
x_1 + 2x_2 = 2x_1 + x_2 \implies x_2 = x_1
$$  
- **预算约束**：$ 5x_1 + 5x_2 = 40 \implies x_1 + x_2 = 8 $。  
- **代入 kink 条件**：$ x_1 = x_2 $ 时，$ 2x_1 = 8 \implies x_1 = x_2 = 4 $。  
- **效用验证**：$ U = \min\{4 + 8, 8 + 4\} = \min\{12, 12\} = 12 $，高于其他组合（如 $ (x_1, x_2) = (8,0) $ 时 $ U = 8 $）。  
- **选项含义**：收入和价格相等时，kink 线 $ x_1 = x_2 $ 与预算线交于 $ x_1 = x_2 = 4 $，故消费量严格相等。选项 (e) 直接描述此结果；(c) 和 (d) 的“at least as much”虽成立（因相等），但未捕获紧约束。  
**结论**：正确答案为 **(e)**。  

### 4.6 无差异曲线的形状分析  
Ethel 的效用函数 $ U = \min\{2x + y, 3y\} $ 的 kink 线由 $ 2x + y = 3y $ 确定：  
$$
2x + y = 3y \implies 2x = 2y \implies x = y
$$  
- **无差异曲线分段特征**：  
  - 当 $ x \geq y $ 时：$ U = 3y $（因 $ 3y \leq 2x + y $），故 $ y = \frac{U}{3} $ 为水平线段（$ y $ 恒定）。  
  - 当 $ x \leq y $ 时：$ U = 2x + y $（因 $ 2x + y \leq 3y $），故 $ y = U - 2x $ 为负斜率线段（斜率 $ -2 $）。  
- **kink 位置**：两线段在 $ x = y $ 处相交（如 $ U = 3 $ 时，交点 $ (1,1) $）。  
- **选项排除**：  
  - (a)、(b)、(e) 涉及垂直线或错误 kink 线，但曲线无垂直段。  
  - (d) 声称含正斜率段，但实际为负斜率与水平段。  
  - (c) 正确匹配：水平段（$ y = U/3 $）与负斜率段（$ y = U - 2x $）在 $ x = y $ 处 kink。  
**结论**：正确答案为 **(c)**。
