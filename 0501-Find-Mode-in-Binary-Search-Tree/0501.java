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
    int count = 0, maxCount = 0;
    Integer prev = null;
    List<Integer> mode = new ArrayList<>();

    public int[] findMode(TreeNode root) {
        inorder(root, true);
        count = 0;
        prev = null;
        inorder(root, false);

        return mode.stream().mapToInt(i -> i).toArray();
    }

    public void inorder(TreeNode node, boolean isFirst) {
        if (node == null)
            return;
        inorder(node.left, isFirst);

        if (prev != null && prev == node.val) {
            count++;
        } else {
            count = 1;
        }

        if (isFirst) {
            if (count > maxCount) {
                maxCount = count;
            }
        } else {
            if (count == maxCount) {
                mode.add(node.val);
            }
        }

        prev = node.val;
        inorder(node.right, isFirst);
    }
}