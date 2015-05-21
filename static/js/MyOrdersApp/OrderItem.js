var React = require("react");


module.exports = React.createClass({
	handleonClick:function(){
        console.log(this.props.order.id);
    },
    render:function(){
		return(
			<div>
                <div className="row-fluid">
                    <div className="span3 center">{this.props.order.id}</div>
                    <div className="span3 center">{this.props.order.gid}</div>
                    <div className="span3 center">{this.props.order.unit_price}</div>
                    <div className="span3 center">
                        <a className="btn btn-success" href={'#order/'+this.props.order.id}>
                            <i className="halflings-icon white zoom-in"></i>
                        </a>
                        <a className="btn btn-danger" onClick={this.handleonClick} href="#">
                            <i className="halflings-icon white trash"></i>
                        </a>
                    </div>
                </div>
            </div>

		)		
	}
})