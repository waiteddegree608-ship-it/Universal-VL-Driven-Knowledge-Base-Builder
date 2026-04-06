# PDF_Quiz_13

### Page/Slide 1



### 1. 提取文字与公式  
**标题**：Quiz 13  
**主题**：Risky Assets  

#### 13.1  
**题干**：  
Suppose that Ms. Lynch in Problem 13.1 can make up her portfolio using a risk-free asset that offers a sure-fire rate of return of 15% and a risky asset with expected rate of return 30%, with standard deviation 5. If she chooses a portfolio with expected rate of return 18.75%, then the standard deviation of her return on this portfolio will be:  

**选项**：  
(a) 0.63%.  
(b) 4.25%.  
(c) 1.25%.  
(d) 2.50%.  
(e) None of the other options are correct.  

#### 13.2  
**题干**：  
Suppose that Fenner Smith of Problem 13.2 must divide his portfolio between two assets, one of which gives him an expected rate of return of 15 with zero standard deviation and one of which gives him an expected rate of return of 30 and has a standard deviation of 5. He can alter the expected rate of return and the variance of his portfolio by changing the proportions in which he holds the two assets. If we draw a “budget line” with expected return on the vertical axis and standard deviation on the horizontal axis, depicting the combinations that Smith can obtain, the slope of this budget line is:  

**选项**：  
(a) 3.  
(b) −3.  
(c) 1.50.  
(d) −1.50.  
(e) 4.50.  

---

### 2. 关键问题解析  
#### 13.1 的解题逻辑  
- **无风险资产**：收益率 $ r_f = 15\% $，标准差 $ \sigma_f = 0 $。  
- **风险资产**：预期收益率 $ E(r_m) = 30\% $，标准差 $ \sigma_m = 5 $。  
- **组合预期收益率**：$ E(r_p) = 18.75\% $。  

**推导**：  
设风险资产权重为 $ w $，则无风险资产权重为 $ 1-w $。  
根据组合收益公式：  
$$
E(r_p) = w \cdot E(r_m) + (1-w) \cdot r_f
$$  
代入数据：  
$$
18.75 = w \cdot 30 + (1-w) \cdot 15 \implies w = 0.25
$$  
组合标准差由风险资产权重决定：  
$$
\sigma_p = w \cdot \sigma_m = 0.25 \cdot 5 = 1.25
$$  
**结论**：选项 (c) 正确（1.25%）。  

---

#### 13.2 的预算线斜率  
- **无风险资产**：收益率 $ r_f = 15 $，标准差 $ \sigma_f = 0 $。  
- **风险资产**：预期收益率 $ E(r_m) = 30 $，标准差 $ \sigma_m = 5 $。  

**预算线定义**：  
当以标准差（横轴）和预期收益（纵轴）为坐标时，组合的可行集为一条直线，称为**资本配置线（Capital Allocation Line, CAL）**。其斜率为**夏普比率**（Sharpe Ratio）：  
$$
\text{Slope} = \frac{E(r_m) - r_f}{\sigma_m}
$$  
代入数据：  
$$
\text{Slope} = \frac{30 - 15}{5} = 3
$$  
**结论**：预算线斜率为 **3**，选项 (a) 正确。该斜率表示每承担 1 单位风险（标准差）所获得的超额收益。  

---

### 3. 知识连续性说明  
- **组合标准差**：在无风险资产与风险资产的组合中，标准差仅由风险资产权重线性决定（因无风险资产的标准差为 0 且与风险资产不相关）。  
- **预算线斜率**：反映风险-收益权衡的效率，斜率越大，单位风险带来的预期收益越高，体现资产配置的优化方向。  
- **隐含前提**：假设投资者可自由调整资产权重，且风险资产与无风险资产之间无相关性（题目默认）。

---
### Page/Slide 2



### 图片内容解析  

#### 1. 文字与公式提取  
当前图片中仅包含以下文字：  
```  
470 RISKY ASSETS (Ch. 13)  
```  
**无公式或图表**。  

---

#### 2. 知识连续性说明  
- **页码与章节定位**：  
  - 该页标注为教材第 `470` 页，对应第 **13 章 "RISKY ASSETS"**（风险资产）。  
  - 上文解析的 **13.1** 和 **13.2** 问题均源于此章节，具体涉及 **无风险资产与风险资产的组合优化** 及 **资本配置线（CAL）** 的几何意义。  

- **与上文关联**：  
  - 第 13 章核心内容为 **资产组合的风险-收益权衡**，上文问题（如预算线斜率、组合标准差计算）是本章理论的具体应用。  
  - 本章隐含前提（无风险资产与风险资产无相关性）直接支持了 **13.1 中组合标准差的线性推导** 和 **13.2 中预算线斜率的夏普比率定义**。  

---

#### 3. 补充说明  
- **理论框架作用**：  
  - 本章标题页（`470 RISKY ASSETS (Ch. 13)`）表明后续内容需结合 **均值-方差分析框架**，为问题 13.1/13.2 提供宏观逻辑基础。  
  - 无图表需解释，但结合上文可知：本章通过 **标准差-预期收益坐标系** 分析资产配置，与 13.2 中预算线的几何表述一致。
