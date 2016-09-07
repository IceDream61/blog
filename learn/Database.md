# Note of Database

## Questions

- 3NF 和 BCNF 的关系，老师讲的和网上说的不一样。
	- 老师讲的是：3NF 优于 BCNF，详见本文与老师的PPT
	- 网上说的是：BCNF 优于 3NF，详见[这篇](http://blog.csdn.net/scnujack/article/details/6539642)和[这篇](http://blog.sina.com.cn/s/blog_600da3330100dpfm.html)

## Progress

	写到了 Chapter3 的 3NF，应该开始写4NF。

## Chapter 3. Design Theory for Relational Databases

> A theory : “dependencies” will be talked first

### Functional Dependencies

- FD's Definition
	- Say "$X \rightarrow Y$ holds in R"
	- X, Y, Z represent sets of attributes
	- A, B, C represent single attributes	- just ABC represents {A,B,C}
- Trivial FD
	- $X \rightarrow Y$ where $X \supseteq Y$
- Combining and Splitting rule
	- $A \rightarrow BC$ equals to $A \rightarrow B$ and $A \rightarrow C$
- Superkey and Key (set)
	- K is a Superkey for relation R if K functionally determines all of R.
	- A Minimized Superkey is a Key
- Closure and Keys
	- Closure: denoted $Y^+$
	- if the closure of X is all attributes of a relation, then X is a key /superkey.

### Decompositions

- Goal of Relational Schema Design
	- To avoid **anomalies** and **redundancy**.
	- Anomaly Types:
		- **Update anomaly**: one occurrence of a fact is changed, but not all occurrences.
		- **Deletion anomaly**: valid fact is lost when a tuple is deleted.
		- **Insertion anomaly**: can't add a valid fact because of the lack of other information.
- How to arrive it if it has flaws?
	- Decompositions

### Normal Forms (BCNF, 3NF)

- A standard for a good Relational Scheme Design will eliminate problems

- Boyce-Codd Normal Form
	- Conditions: If $X \rightarrow Y$ is a nontrivial FD that holds in R, X is a superkey.
	- Example**s**:
		- $R(A,B,C)$ with $A \rightarrow B$, $A \rightarrow C$
	- How to decomposition into BCNF:
		- Check for BCNF for every FD like "$X \rightarrow Y$", it not, continue
		- Compute $X^+$
		- Replace R by relations with schemas:
			1. $R_1=X^+$
			2. $R_2=R-(X^+-X)$
		- Check for BCNF for each new Relations, back to the beginning

- Third Normal Form
	- Conditions: If X ->Y is a nontrivial FD that holds in R, X is a superkey, or Y is a prime.
	- Example**s**:
		- $R(A,B,C)$ with $AB \rightarrow C$ and $C \rightarrow B$.
	- An attribute is **prime** if it is a member of any key.

- Second Normal Form
	- Conditions: no nonkey attribute is dependent on only a portion of the primary key.

- First Normal Form
	- Conditions: every component of every tuple is an atomic value.

- Properties of a decomposition
	- Lossless Join 无损拆分: 信息无损
	- Dependency Preservation 依赖保护: 依旧可检查
	- **3NF: promise Lossless Join and Dependency Preservation**
	- **BCNF: only promise Lossless Join**

- Use **chase method** to find out whether the decomposition is lossy join.
	- Summary of the Chase Test method
		- If two rows agree in the left side of a **FD**, make their right sides agree too.
		- Always **replace** a subscripted symbol by the corresponding unsubscripted one, if possible.
		- If we ever get an unsubscripted row, we know any tuple in the project-join is in the original (**the join is lossless**).
		- Otherwise, the final tableau is a **counterexample**.

- 3NF Synthesis Algorithm
	- We can always construct a decomposition into 3NF relations with a lossless join and dependency preservation.
	- Need minimal basis for the FD’s:
		- Right sides are single attributes.		- No FD can be removed.
		- No attribute can be removed from a left side.
	- Algorithm: 还没看懂，暂略
	- Why It Works
		- for **Preserves dependencies**: each FD from a minimal basis is contained in a relation, thus preserved.
		- for **Lossless Join**: use the chase to show that the row for the relation that contains a key can be made all-unsubscripted variables.

- Origin PPTs:

![BCNF decomposition algorithm](Database12.png)

![3NF synthesis](Database13.png)

### Multivalued Dependencies (and 4NF)

### Reasoning About FD's + MVD's

## Chapter 2. The Relational Model of data

### Theorization

- Relation
	- Relation name
	- Attributes (column headers)
	- tuples (rows)
- Database
	- set of all relation schemas in the database
- Constraints on relations
	- Key Constrainsts: don't allow two tuples to have the same key

### Realization

- Set of tables $\leftarrow$ Database

``` sql
CREATE TABLE <name> (
	<list of elements>
);
DROP TABLE <name>;
```

- Table $\leftarrow$ Relation

``` sql
ALTER TABLE <name> ADD <new attribute>;
ALTER TABLE <name> DROP <attribute>;
```

- Element $\leftarrow$ Attribute

``` sql
CREATE TABLE <name> (
	<name>	<type>,
	<name>	<type> UNIQUE,
	<name>	<type> PRIMARY KEY,
	<name>	<type> NOT NULL,
	<name>	<type> DEFAULT value,
	
	PRIMARY KEY (<list of name>)
);
```

- Type of Element

| Type | Discribe |
| --- | --- |
| INT / INTEGER |  |
| REAL / FLOAT |  |
| CHAR(n) | fixed-length of n |
| VARCHAR(n) | variable-length up to n |
| BIT(n) | bit string of length n |
| BOOLEAN | true, false or **unknown** |
| DATE | `'yyyy-mm-dd'` |
| TIME | `'hh:mm:ss'` or `'hh:mm:ss.d'`*(percentage)* |

- Hint
	- Any value can be **NULL** except **PRIMARY KEY**.
	- There's only one **PRIMARY KEY** in one **TABLE**.

### Algebra

Operate | Format | Example on Set | Example on Bag
--- | --- | --- | ---
Selection | $R1:=\sigma_C(R2)$ | ![$JoeMenu:=\sigma_{bar="Joe's"}(Sells)$](Database1.png) | ![](Database8.png)
Projection | $R1:=\pi_L(R2)$ | ![$Prices:=\pi_{beer,price}(Sells)$](Database2.png) | ![](Database9.png)
Extended Projection | $R1:=\pi_L(R2)$ | ![$\pi_{A+B\rightarrow C,A,A(R)}$](Database3.png)
Product | $R3:=R1\times R2$ | ![Product on Set](Database4.png) | ![](Database10.png)
Theta-Join | $R3:=R1\Join_C R2$ | ![Theta-Join on Set](Database5.png) | ![](Database11.png)
Natural Join | $R3:=R1\Join R2$ | ![Natural Join on Set](Database6.png)
Renaming | $R1:=\rho_{R1(A_1,...,A_n)}(R2)$ | ![Renaming on Set](Database7.png)

### Bag and Set

- A bag (or multiset ) is like a set, but an element may appear more than once.

- Why Bags?
	- SQL, the most important query language for relational databases, is actually a bag language.
	- Some operations, like projection, are more efficient on bags than sets.


## Chapter 1. Introduction

- Database System
	- data, metadata
	- disk
	- DBMS
	- people (user, designer, manager)
- DBMS，Database Management System
	- such as: MySQL
- Data Model
	- such as: Relational Model, Semistructured-data Model
	- Motivation of Semistructured-data Model
		- Flexible representation of data
		- Sharing of **documents** among systems and databases
