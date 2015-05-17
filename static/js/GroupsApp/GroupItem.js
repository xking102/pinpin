var React = require("react");


module.exports = React.createClass({
	render:function(){
		var group = this.props.group;
		var detail_link = '#/group/'+group.id;
		return(
			<div className="col-md-3">
                <div className="thumbnail">
                    <img alt="230x200" src="/static/imgs/groups/230x200.gif" />
                     <div className="caption">
                        <h3>Product AAAAAAAA</h3>
                        <p>Cras justo odio, dapibus ac facapibus ac faapibus a
                        c faapibus ac faapibus ac faapibus ac failisis in, egestas eget quam.
                         Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultr
                         Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultr
                         icies vehicula ut id elit.</p>
                         <h4>剩余数量：15</h4>
                         <h4>到手单价：30</h4>
                        <p><a href={detail_link} className="btn btn-primary">View</a></p>
                        <p className="momenttime">5天前</p>
                    </div>
                </div>
			</div>
		)		
	}
})