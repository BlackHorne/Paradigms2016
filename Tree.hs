data BinaryTree = Nil | Node (Int, Int) BinaryTree BinaryTree deriving (Show, Eq)

data GetResult v = NotFound | Found v deriving Show

lookup k (Node (k', v) leftTree rightTree) 
                |k == k' = Found v
                |k > k' = lookup k rightTree
                |k < k' = lookup k leftTree
lookup _ _ = NotFound

insert k v (Node (k', v') leftTree rightTree)
                |k > k' = Node (k', v') leftTree (insert k v rightTree)
                |k < k' = Node (k', v') (insert k v leftTree) rightTree
                |k == k' = Node (k, v) leftTree rightTree
insert k v _ = Node (k, v) Nil Nil

delete k (Node (k', v) leftTree rightTree)
                |k > k' = Node (k', v) leftTree (delete k rightTree)
                |k < k' = Node (k', v) (delete k leftTree) rightTree
                |k == k' = mergeHeap
                        where mergeHeap 
                                |leftTree == Nil = rightTree 
                                |rightTree == Nil = leftTree
                                |otherwise = replaceMin (Node (k', v) leftTree rightTree)

findMinPair (Node (k, v) leftTree _) 
                |leftTree == Nil = (k, v)
                |otherwise = findMinPair leftTree

findMinKey (Node (k, _) leftTree _) 
                |leftTree == Nil = k
                |otherwise = findMinKey leftTree

replaceMin (Node (_, _) leftTree rightTree) = Node minPair leftTree (delete minKey rightTree)
                where 
                        minPair = findMinPair rightTree
                        minKey = findMinKey rightTree
