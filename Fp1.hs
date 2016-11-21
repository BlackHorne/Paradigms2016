head' (x:_) = x

tail' (_:xs) = xs
tail' _ = [] 

take' 0 _ = []
take' n (x:xs) = x : take' (n - 1) xs

drop' 0 x = x
drop' n (_:xs) = drop' (n - 1) xs
drop' _ _ = []

filter' f (x:xs) | f x = x : filter' f xs
                 | otherwise = filter' f xs
filter' _ _ = []

foldl' f z (x:xs) = foldl' f (f z x) xs
foldl' _ z _ = z

concat' (x:xs) y = x : concat' xs y
concat' _ y = y

quickSort' (x:xs) = concat' (concat' less equal) greater
          where
                less = quickSort' (filter' (<x) (x:xs))
                greater = quickSort' (filter' (>x) (x:xs))
                equal = filter' (==x) (x:xs)
quickSort' _ = []
