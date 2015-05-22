var React = require("react");


module.exports = React.createClass({
    
    render:function(){
        var status = this.props.order.status;
        var styleObj={
            display: 'block',
         };
        if(status==25){
            styleObj={
                display: 'none',
            };
        }else{
            styleObj={
                
            };
        }
		return(
			<div>
                <div className="row-fluid">
                    <div className="span3 center">{this.props.order.id}</div>
                    <div className="span3 center">{this.props.order.gid}</div>
                    <div className="span3 center">{this.props.order.unit_price}</div>
                    <div className="span3 center">
                        <a className="btn btn-info" href={"order#/"+this.props.order.id}>
                            <i className="halflings-icon white zoom-in"></i>
                        </a>
                        <a className="btn btn-danger" style={styleObj} href={"order#/"+this.props.order.id+"/pay"}>
                            <i className="halflings-icon white ok"></i>
                        </a>
                    </div>
                </div>
            </div>

		)		
	}
})