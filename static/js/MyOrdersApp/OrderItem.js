var React = require("react");


module.exports = React.createClass({
	render:function(){
		var order = this.props.order;
		return(
			<div>
                <tr>
                    <td className="center">{order.id}</td>
                    <td className="center">{order.title}</td>
                    <td className="center">{order.price}</td>
                    <td className="center">
                        <a className="btn btn-success" href="#">
                            <i className="halflings-icon white zoom-in"></i>
                        </a>
                        <a className="btn btn-danger" href="#">
                            <i className="halflings-icon white trash"></i>
                        </a>
                    </td>
                </tr>
            </div>

		)		
	}
})