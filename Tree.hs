import Prelude hiding (lookup)

data BinaryTree k v = Nil | Node (k, v) (BinaryTree k v) (BinaryTree k v) deriving Show

lookup :: Ord k => k -> BinaryTree k v -> Maybe v
lookup k (Node (k', v) leftTree rightTree)
                |k == k' = Just v
                |k > k'  = lookup k rightTree
                |k < k'  = lookup k leftTree
lookup _ _ = Nothing

insert :: Ord k => k -> v -> BinaryTree k v -> BinaryTree k v
insert k v (Node (k', v') leftTree rightTree)
                |k > k'  = Node (k', v') leftTree (insert k v rightTree)
                |k < k'  = Node (k', v') (insert k v leftTree) rightTree
                |k == k' = Node (k, v) leftTree rightTree
insert k v _ = Node (k, v) Nil Nil

delete :: Ord k => k -> BinaryTree k v -> BinaryTree k v
delete k (Node (k', v) leftTree rightTree)
                |k > k' = Node (k', v) leftTree (delete k rightTree)
                |k < k' = Node (k', v) (delete k leftTree) rightTree
                |isEmpty leftTree  = rightTree 
                |isEmpty rightTree = leftTree
                |otherwise = (Node minPair leftTree (delete minKey rightTree))
                        where 
                                minPair = findMinPair rightTree
                                minKey  = findMinKey rightTree

isEmpty (Node (k, v) leftTree rightTree) = False
isEmpty Nil = True

findMinPair (Node (k, v) leftTree _) 
                |isEmpty leftTree = (k, v)
                |otherwise = findMinPair leftTree

findMinKey (Node (k, _) leftTree _) 
                |isEmpty leftTree = k
                |otherwise = findMinKey leftTree
