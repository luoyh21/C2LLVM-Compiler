from antlr4 import *
from antlr.clongParser import clongParser
from antlr.clongVisitor import clongVisitor
from antlr.clongLexer import clongLexer
import os
import json

import antlr4

class TreeConverter:
    def __init__(self, parser):
        self.parser = parser

    def tree_to_dict(self, node):
        if isinstance(node, antlr4.tree.Tree.TerminalNode):
            return {
                "type": "EOF" if node.getSymbol().type<0 
                else self.parser.literalNames[node.getSymbol().type] if node.getSymbol().type < len(self.parser.literalNames) 
                else self.parser.symbolicNames[node.getSymbol().type], "text": node.getText()}
        else:
            if node.getChildCount() == 0:
                return {self.parser.ruleNames[node.getRuleIndex()]:node.getText()}
            children = [self.tree_to_dict(child) for child in node.children]
            return {self.parser.ruleNames[node.getRuleIndex()]: children}

def analyse(filename):
    """
    将输入的文件进行词法分析，得到token流
    Args:
        filename: 输入的文件名
    """
    lexer = clongLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser=clongParser(stream)
    tree = parser.prog()
    converter=TreeConverter(parser)
    write_tree_to_json(tree, filename, converter)
    
    
    
def write_tree_to_json(tree, filename, converter):
    tree_dict = converter.tree_to_dict(tree)
    tree_json = json.dumps(tree_dict, indent=4)
    dirname, basename = os.path.split(filename)
    base, _ = os.path.splitext(basename)
    new_filename = os.path.join(dirname, base + '.json')
    with open(new_filename, 'w') as f:
        f.write(tree_json)