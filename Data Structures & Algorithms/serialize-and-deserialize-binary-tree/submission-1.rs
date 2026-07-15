// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::cell::RefCell;
use std::rc::Rc;

struct Codec {}

impl Codec {
    fn new() -> Self {
        Self {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, values: &mut Vec<String>) {
            match node {
                Some(node_rc) => {
                    let node_ref = node_rc.borrow();

                    values.push(node_ref.val.to_string());

                    dfs(&node_ref.left, values);
                    dfs(&node_ref.right, values);
                }
                None => {
                    values.push("N".to_string());
                }
            }
        }

        let mut values = Vec::new();
        dfs(&root, &mut values);

        values.join(",")

    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        fn build<'a, I>(values: &mut I) -> Option<Rc<RefCell<TreeNode>>>
        where
            I: Iterator<Item = &'a str>,
        {
            let value = values.next()?;

            if value == "N" {
                return None;
            }

            let val = value.parse::<i32>().ok()?;

            let left = build(values);
            let right = build(values);

            Some(Rc::new(RefCell::new(TreeNode {
                val,
                left,
                right,
            })))
        }

        let mut values = data.split(',');
        build(&mut values)
    }
}
