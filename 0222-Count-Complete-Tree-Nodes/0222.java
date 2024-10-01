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
    public int countNodes(TreeNode root) {
        if (root == null)
            return 0;

        int left = leftHeight(root);
        int right = rightHeight(root);

        if (left > right) {
            return 1 + countNodes(root.left) + countNodes(root.right);
        } else {
            return Math.pow(2, left) - 1;
        }

    }

    public int leftHeight(TreeNode node) {
        if (node == null)
            return 0;
        return 1 + leftHeight(node.left);
    }

    public int rightHeight(TreeNode node) {
        if (node == null)
            return 0;
        return 1 + rightHeight(node.right);
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