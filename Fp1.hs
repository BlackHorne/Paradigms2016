head' (x:xs) = x

tail' (x:xs) = xs
tail' _ = [] 

take' 0 _ = []
take' n (x:xs) = x:(take' (n - 1) xs)

drop' 0 x = x
drop' n (x:xs) = drop' (n - 1) xs
drop' n _ = []

filter' f (x:xs) | f x = x : (filter' f xs)
                 | otherwise = filter' f xs
filter' f _ = []

foldl' f z (x:xs) = foldl' f (f z x) xs
foldl' f z _ = z

concat' (x:xs) y = x : (concat' xs y)
concat' _ y = y

quickSort' (x:xs) = concat' (concat'  (quickSort' (filter' (<x) (x:xs))) (filter' (==x) (x:xs))) (quickSort' (filter' (>x) (x:xs)))
quickSort' x = x

