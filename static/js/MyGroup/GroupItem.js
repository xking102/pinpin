var React = require("react");


module.exports = React.createClass({
    
    render:function(){
        var status = this.props.group.status;
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
        var statusDisplay='';
        if (status==10){
            statusDisplay="拼团中";
        }else if(status==15){
            statusDisplay="拼团成功";
        }else{
            statusDisplay="other";
        }
		return(
			<div>
                <div className="row-fluid">
                    <div className="span3 center">{this.props.group.title}</div>
                    <div className="span1 center">{this.props.group.total_qty}</div>
                    <div className="span1 center">{this.props.group.req_qty}</div>
                    <div className="span1 center">{this.props.group.confirm_qty}</div>
                    <div className="span1 center">{statusDisplay}</div>
                    <div className="span3 center">
                        <a className="btn btn-info" href={"group#/"+this.props.group.id}>
                            <i className="halflings-icon white zoom-in"></i>
                        </a>
                        <a className="btn btn-danger" style={styleObj} href={"#"}>
                            <i className="halflings-icon white ok"></i>
                        </a>
                    </div>
                </div>
            </div>

		)		
	}
})