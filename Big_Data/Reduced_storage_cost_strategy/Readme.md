# Implement an efficient data layout and retrieval strategy for a Hadoop Cluster

## Overview & background: 

A database may have some common data repeated across records. For example,
in the attached CSV file (that is exported from a database) some column values are
same among multiple rows. These common values are repetitively stored in the
database records, which increases the storage cost but reduces retrieval time for
analytical queries.

However, we need to create a layout of this kind of dataset on a Hadoop cluster at
a reduced storage cost. So, we need to understand the commonality of values
across records and create a data layout that avoids duplicate values. But at the 
same time, we need to allow retrieval of a complete data record from the storage,
given a record identifier.

## Input: CSV data with flat schema with multiple records and features.

## Description:

### 1. STORAGE:

Each Storage Node will store the data based on below condition. 

a. Mutually Exclusive feature data (column value) which is not common 
across records (rows): private node

b. Feature data common in two records: 2-way shared node

c. Feature data common in four records: 4-way shared node.

d. Feature data common in eight records: 8-way shared node.

Note: Private node, 2,4,8- way shared nodes are storage nodes which
stores feature values which are common in 2, 4, 8 records respectively.

### 2. METADATA 

Maintain record ID wise metadata about above storage deployments, which
will explain how the feature values are stored across the storage nodes. The 
meta-data can be stored on a specific node.

### 3. RETRIEVAL:
For provided record ID, retrieval of record will refer step 2 to fetch all the 
required features (column values) from respective storage nodes to form the 
original record.

**NOTE:** 

You can apply different techniques to understand the similarity of
feature values like normalization, standardization, vectorization etc
