/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ans = new ArrayList<>();
        treePath(root, "", ans);
        return ans;
    }

    public void treePath(TreeNode node, String path, List<String> ans) {
        if (node == null)
            return;

        path += node.val;

        if (node.left == null && node.right == null) {
            ans.add(path);
            return;
        }

        if (node.left != null) {
            treePath(node.left, path + "->", ans);
        }

        if (node.right != null) {
            treePath(node.right, path + "->", ans);
        }
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}