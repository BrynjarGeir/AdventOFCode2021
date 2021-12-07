{-# LANGUAGE TypeApplications #-}
module Day1 where
    readInput :: FilePath -> IO[Int]
    readInput file = (map (read @Int) . lines) <$> readFile file

    example :: IO[Int]
    example = readInput "example"

    countInc :: [Int] -> Int
    countInc = 
    