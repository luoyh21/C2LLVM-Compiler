// Generated from /Users/chao-xu21/Clong/translator/src/antlr/clong.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link clongParser}.
 */
public interface clongListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link clongParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(clongParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(clongParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#head}.
	 * @param ctx the parse tree
	 */
	void enterHead(clongParser.HeadContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#head}.
	 * @param ctx the parse tree
	 */
	void exitHead(clongParser.HeadContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#include}.
	 * @param ctx the parse tree
	 */
	void enterInclude(clongParser.IncludeContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#include}.
	 * @param ctx the parse tree
	 */
	void exitInclude(clongParser.IncludeContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(clongParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(clongParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(clongParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(clongParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(clongParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(clongParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(clongParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(clongParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#printf}.
	 * @param ctx the parse tree
	 */
	void enterPrintf(clongParser.PrintfContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#printf}.
	 * @param ctx the parse tree
	 */
	void exitPrintf(clongParser.PrintfContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#gets}.
	 * @param ctx the parse tree
	 */
	void enterGets(clongParser.GetsContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#gets}.
	 * @param ctx the parse tree
	 */
	void exitGets(clongParser.GetsContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#strlen}.
	 * @param ctx the parse tree
	 */
	void enterStrlen(clongParser.StrlenContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#strlen}.
	 * @param ctx the parse tree
	 */
	void exitStrlen(clongParser.StrlenContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#returnFunc}.
	 * @param ctx the parse tree
	 */
	void enterReturnFunc(clongParser.ReturnFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#returnFunc}.
	 * @param ctx the parse tree
	 */
	void exitReturnFunc(clongParser.ReturnFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(clongParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(clongParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#ifFunc}.
	 * @param ctx the parse tree
	 */
	void enterIfFunc(clongParser.IfFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#ifFunc}.
	 * @param ctx the parse tree
	 */
	void exitIfFunc(clongParser.IfFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#elseif}.
	 * @param ctx the parse tree
	 */
	void enterElseif(clongParser.ElseifContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#elseif}.
	 * @param ctx the parse tree
	 */
	void exitElseif(clongParser.ElseifContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#elseFunc}.
	 * @param ctx the parse tree
	 */
	void enterElseFunc(clongParser.ElseFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#elseFunc}.
	 * @param ctx the parse tree
	 */
	void exitElseFunc(clongParser.ElseFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#whileFunc}.
	 * @param ctx the parse tree
	 */
	void enterWhileFunc(clongParser.WhileFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#whileFunc}.
	 * @param ctx the parse tree
	 */
	void exitWhileFunc(clongParser.WhileFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#forFunc}.
	 * @param ctx the parse tree
	 */
	void enterForFunc(clongParser.ForFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#forFunc}.
	 * @param ctx the parse tree
	 */
	void exitForFunc(clongParser.ForFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#initFunc}.
	 * @param ctx the parse tree
	 */
	void enterInitFunc(clongParser.InitFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#initFunc}.
	 * @param ctx the parse tree
	 */
	void exitInitFunc(clongParser.InitFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#assignFunc}.
	 * @param ctx the parse tree
	 */
	void enterAssignFunc(clongParser.AssignFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#assignFunc}.
	 * @param ctx the parse tree
	 */
	void exitAssignFunc(clongParser.AssignFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#initParam}.
	 * @param ctx the parse tree
	 */
	void enterInitParam(clongParser.InitParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#initParam}.
	 * @param ctx the parse tree
	 */
	void exitInitParam(clongParser.InitParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#initArray}.
	 * @param ctx the parse tree
	 */
	void enterInitArray(clongParser.InitArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#initArray}.
	 * @param ctx the parse tree
	 */
	void exitInitArray(clongParser.InitArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(clongParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(clongParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(clongParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(clongParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#typeParam}.
	 * @param ctx the parse tree
	 */
	void enterTypeParam(clongParser.TypeParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#typeParam}.
	 * @param ctx the parse tree
	 */
	void exitTypeParam(clongParser.TypeParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(clongParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(clongParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#library}.
	 * @param ctx the parse tree
	 */
	void enterLibrary(clongParser.LibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#library}.
	 * @param ctx the parse tree
	 */
	void exitLibrary(clongParser.LibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#paramName}.
	 * @param ctx the parse tree
	 */
	void enterParamName(clongParser.ParamNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#paramName}.
	 * @param ctx the parse tree
	 */
	void exitParamName(clongParser.ParamNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#intm}.
	 * @param ctx the parse tree
	 */
	void enterIntm(clongParser.IntmContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#intm}.
	 * @param ctx the parse tree
	 */
	void exitIntm(clongParser.IntmContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#doublem}.
	 * @param ctx the parse tree
	 */
	void enterDoublem(clongParser.DoublemContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#doublem}.
	 * @param ctx the parse tree
	 */
	void exitDoublem(clongParser.DoublemContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#charm}.
	 * @param ctx the parse tree
	 */
	void enterCharm(clongParser.CharmContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#charm}.
	 * @param ctx the parse tree
	 */
	void exitCharm(clongParser.CharmContext ctx);
	/**
	 * Enter a parse tree produced by {@link clongParser#stringm}.
	 * @param ctx the parse tree
	 */
	void enterStringm(clongParser.StringmContext ctx);
	/**
	 * Exit a parse tree produced by {@link clongParser#stringm}.
	 * @param ctx the parse tree
	 */
	void exitStringm(clongParser.StringmContext ctx);
}