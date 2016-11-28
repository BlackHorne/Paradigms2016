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
delete _ (Node (_, _) Nil rightTree) = rightTree
delete _ (Node (_, _) leftTree Nil)  = leftTree 
delete _ (Node (k, v) leftTree rightTree) = delParent (Node (k, v) leftTree rightTree)

delParent (Node (_, _) leftTree rightTree) = Node minPair leftTree (delete minKey rightTree)
        where minPair = findMinPair rightTree
              minKey  = fst minPair

findMinPair (Node (k, v) Nil _) = (k, v)
findMinPair (Node (_, _) leftTree _) = findMinPair leftTree

