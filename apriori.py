'''
    Developed by: James Ald Teves
    BS Computer Science

    Instructor: Dr. Chuchi S. Montenegro
    Description: A simulation on how the Apriori algorithm works  
'''
#Transactions Datasets
data = [['M', 'O', 'N', 'K', 'E', 'Y'],
        ['D', 'O', 'N', 'K', 'E', 'Y'],
        ['M', 'A', 'K', 'E'],
        ['M', 'U', 'C', 'K', 'Y'],
        ['C', 'O', 'O', 'K', 'I', 'E']]

# Define the minimum support = 60% and confidence = 75%
min_support = 0.6
min_confidence = 0.75

#Step 1: Generate candidate item sets of length 1
def generate_candidates_1(data):
    candidates = set()
    for transaction in data:
        for item in transaction:
            candidates.add(frozenset([item]))
    return candidates

#Step 2: Prune candidates that do not meet the minimum support
def prune_candidates(candidates, data, min_support):
    item_counts = {}
    num_transactions = len(data)
    frequent_candidates = set()

    for candidate in candidates:
        for transaction in data:
            if candidate.issubset(transaction):
                item_counts[candidate] = item_counts.get(candidate, 0) + 1

    for candidate, count in item_counts.items():
        support = count / num_transactions
        if support >= min_support:
            frequent_candidates.add(candidate)

    return frequent_candidates

#Step 3: Generate candidate item sets of length k
def generate_candidates_k(prev_candidates, k):
    candidates = set()
    for candidate1 in prev_candidates:
        for candidate2 in prev_candidates:
            union_candidate = candidate1.union(candidate2)
            if len(union_candidate) == k:
                candidates.add(union_candidate)
    return candidates

#Step 4: Find frequent item sets
def apriori(data, min_support):
    frequent_item_sets = []
    k = 1
    candidates = generate_candidates_1(data)

    while candidates:
        candidates = prune_candidates(candidates, data, min_support)
        frequent_item_sets.extend(list(candidates))
        k += 1
        candidates = generate_candidates_k(candidates, k)

    return frequent_item_sets

#Step 5: Mine association rules
def mine_association_rules(data, min_support, min_confidence):
    frequent_item_sets = apriori(data, min_support)
    association_rules = []

    for item_set in frequent_item_sets:
        if len(item_set) > 1:
            for item in item_set:
                antecedent = frozenset([item])
                consequent = item_set - antecedent
                support_antecedent = calculate_support(antecedent, data)
                confidence = calculate_confidence(antecedent, item_set, data)

                if confidence >= min_confidence:
                    association_rules.append((antecedent, consequent, support_antecedent, confidence))

    return association_rules

#Helper function to calculate support
def calculate_support(item_set, data):
    count = 0
    for transaction in data:
        if item_set.issubset(transaction):
            count += 1
    return count / len(data)

#Helper function to calculate confidence
def calculate_confidence(antecedent, item_set, data):
    return calculate_support(item_set, data) / calculate_support(antecedent, data)

#Main Method Function
if __name__ == '__main__':
    frequent_item_sets = apriori(data, min_support)
    print("Frequent Item Sets:")
    for item_set in frequent_item_sets:
        print(item_set)

    association_rules = mine_association_rules(data, min_support, min_confidence)
    print("\nAssociation Rules:")
    for rule in association_rules:
        antecedent, consequent, support, confidence = rule
        print(f"Rule: {antecedent} => {consequent}, Support: {support}, Confidence: {confidence}")