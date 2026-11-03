const std = @import("std");

// https://leetcode.com/problems/group-anagrams/description/
// Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
// Output:[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
pub fn grouping_anagram(
    strs: []const []const u8,
    allocator: std.mem.Allocator,
) []const []const []const u8 {

    // 単純な方法
    // 配列先頭の単語の最初の文字列から順に、配列の要素と文字を全部比較する
    // 異なったものからハッシュテーブルかハッシュセットに入れる形
    // O(N * M)

    // 他の方法
    // Inputのlengthを調べる
    // 先頭の単語から順に最初の文字列から、他単語の文字と比較して同じである単語の数とlengthが同じか調べる。
    // 異なる場合は、その文字列をキーに単語をvalueとする

    // ヒントを得た方法
    // アルファベット26文字それぞれの出現回数を記録する
    //
    var map: std.AutoHashMap(u32, []const u8) = .init(allocator);
    defer map.deinit();

    // アルファベット26文字それぞれの出現回数を記録する
    // const count: i32 = .{0} * 26;
    for (strs) |c| {
        std.debug.print("cの値は{s}\n", .{c});
    }

    return &.{};
}

pub fn main() void {
    const input: []const []const u8 = &.{ "eat", "tea", "tan", "ate", "nat", "bat" };

    const result = grouping_anagram(input, std.heap.page_allocator);
    _ = result;
}
