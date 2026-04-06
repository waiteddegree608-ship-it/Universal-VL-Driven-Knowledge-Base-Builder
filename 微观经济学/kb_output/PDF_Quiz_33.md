# PDF_Quiz_33

### Page/Slide 1



### 文字与公式提取

#### 文字内容  
- **Quiz 33**  
- **NAME__________**  
- **Law**  
- **33.1** Consider Madame Norrell, in Problem 33.1. She gets $5 \log x$ if she delivers $x$ buttons to her fence. She has to pay a fine $Fx$ if she is caught, and she has a 10 percent chance of getting caught. If she is caught, she cannot collect anything from her fence. How big should the fine be if we want to limit Madam Norrell to taking 5 buttons?  
  - $(a) \ 4.5$  
  - $(b) \ 5.5$  
  - $(c) \ 9$  
  - $(d) \ 11$  
  - $(e) \ 12$  
- **33.2** Consider Jim and Dick, described in Problem 33.2. Jim rides at speed $s$ and has money $m$; his utility function is $10s + m$. Dick walks at speed $w$ and has money $m$; his utility function is $10w + m$. The cost of an accident to Jim is $c_J(s,w) = s^2 + w^2$, and the cost of an accident to Dick is also $c_D(s,w) = s^2 + w^2$. If there is no liability, how fast will Dick and Jim move?  
  - $(a) \ s = 10$ and $w = 10$  
  - $(b) \ s = 5$ and $w = 5$  
  - $(c) \ s = 5$ and $w = 10$  
  - $(d) \ s = 10$ and $w = 5$  
  - $(e) \ s = 15$ and $w = 15$  

#### 公式列表  
- $5 \log x$  
- $F x$  
- $c_J(s,w) = s^2 + w^2$  
- $c_D(s,w) = s^2 + w^2$  
- $10s + m$  
- $10w + m$  

---

### 图表分析  
当前图片中**无图表**，仅含文字题目。  

---

### 题目解析  

#### 33.1：最优罚款设计  
**核心逻辑**：基于预期效用最大化原理设计威慑性罚款。  
- Madame Norrell 的预期效用为：  
  $$
  U = \underbrace{0.9 \cdot (5 \log x)}_{\text{未被抓时的收益}} + \underbrace{0.1 \cdot 0}_{\text{被抓时无收益}} - \underbrace{0.1 \cdot (F x)}_{\text{预期罚款成本}}
  $$  
  即 $U = 4.5 \log x - 0.1 F x$。  
- 一阶条件（最大化效用）：  
  $$
  \frac{dU}{dx} = \frac{4.5}{x} - 0.1 F = 0 \quad \Rightarrow \quad F = \frac{45}{x}
  $$  
- 目标限制 $x = 5$，代入得：  
  $$
  F = \frac{45}{5} = 9
  $$  
  **结论**：罚款需设为 $F = 9$ 才能抑制行为，对应选项 **(c)**。  

#### 33.2：无责任规则下的行为选择  
**核心逻辑**：在无责任规则下，个体仅内化自身事故成本，忽略对他人影响，导致纳什均衡解。  
- **Jim 的效用最大化**（给定 $w$）：  
  $$
  \max_s \, [10s - c_J(s,w)] = \max_s \, (10s - s^2 - w^2)
  $$  
  一阶条件：$10 - 2s = 0 \ \Rightarrow \ s = 5$。  
- **Dick 的效用最大化**（给定 $s$）：  
  $$
  \max_w \, [10w - c_D(s,w)] = \max_w \, (10w - s^2 - w^2)
  $$  
  一阶条件：$10 - 2w = 0 \ \Rightarrow \ w = 5$。  
- **均衡结果**：双方独立决策时，均选择速度 $5$，即 $(s, w) = (5, 5)$。  
  **结论**：无责任规则导致过低速度（效率损失），对应选项 **(b)**。

---
### Page/Slide 2



### 文字提取  
- `520 LAW (Ch. 33)`  

### 解析  
该文字为教科书页码及章节标识：  
- **`520`** 表示内容出处为教材第520页；  
- **`LAW (Ch. 33)`** 指明主题为法律经济学（LAW），对应第33章。  

结合上文知识点总结，此标识直接关联问题 **33.1**（最优罚款设计）和 **33.2**（无责任规则下的行为选择）。上文已基于该章节内容解析了预期效用最大化原理在威慑性罚款中的应用（$F=9$ 抑制按钮盗窃行为），以及无责任规则导致纳什均衡失效（$s=w=5$ 的低效率结果）。此处页码引用仅作为理论情境的定位锚点，无新增分析单元，但强化了法律经济学中“事故成本内化”与“威慑机制”理论框架的连续性。
