use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        
        let uniques : HashSet<&i32> = nums.iter().collect();

        uniques.len() != nums.len()

    }
}
