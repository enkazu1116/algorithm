const std = @import("std");

// https://leetcode.com/problems/group-anagrams/description/
// Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
// Output:[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
pub fn grouping_anagram(
    strs: []const []const u8,
    allocator: std.mem.Allocator,
) []const []const []const u8 {

    // ヒントを得た方法
    // アルファベット26文字それぞれの出現回数を記録する
    var map: std.AutoHashMap(u32, []const u8) = .init(allocator);
    defer map.deinit();

    // アルファベット26文字それぞれの出現回数を記録する
    var count: [26]u32 = .{0} ** 26;
    for (strs) |char| {
        for (char) |c| {
            count[c - 'a'] += 1;
        }
        std.debug.print("count: {any}\n", .{count});
    }

    return &.{};
}

pub fn main() void {
    const input: []const []const u8 = &.{ "eat", "tea", "tan", "ate", "nat", "bat" };

    const result = grouping_anagram(input, std.heap.page_allocator);
    _ = result;
}
