var React = require("react");


module.exports = React.createClass({
	render:function(){
		var group = this.props.group;
		var detail_link = '#/group/'+group.id;
        var mod = group.id%3;
        var stylecolor = "greenDark";
        if(mod == 0){
            stylecolor = "greenDark";
        }else if(mod == 1){
            stylecolor = "green";
        }else{
            stylecolor = "greenLight";
        };
        stylecolor = "circleStatsItemBox " + stylecolor;
		return(
			<div className="span2">
                <div className={stylecolor}>
                    <div className="header">{group.title}</div>
                    <div className="circleStat">
                        <a href={detail_link}>
                            <img alt="221x125" src="/static/imgs/groups/221x125.gif" />
                        </a>
                    </div>
                    <div className="footer">
                        <span className="count">
                            <span class="unit">到手价：￥</span>
                            <span className="number">{group.unit_price}</span>
                        </span>
                        <span className="sep"> | </span>
                        <span className="count">
                            <span class="unit">剩余数量：</span>
                            <span className="number">{group.total_qty}</span>
                        </span>
                    </div>
                </div>
			</div>
		)		
	}
})