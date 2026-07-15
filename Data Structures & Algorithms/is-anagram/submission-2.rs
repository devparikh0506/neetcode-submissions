use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut counts : HashMap<char, i32> = HashMap::new();

        for c in s.chars(){
            *counts.entry(c).or_insert(0) += 1;
        }

        for c in t.chars(){
            if let Some(count) = counts.get_mut(&c) {
                if *count == 0 {
                    return false;
                }

                *count -= 1;
            } else {
                return false;
            }
        }

        for (c, count) in &counts{
            if *count != 0 {
                return false;
            }
        } 

        true
    }
}
