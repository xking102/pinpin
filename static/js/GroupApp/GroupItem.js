var React = require("react");


module.exports = React.createClass({
    getInitialState : function(){
        return{
            reqnum : 1,
            amount : 30
        }    
    },
    handlerReqnum:function(e){
        var newval  = e.target.value;
        if(newval > 0){
            if(newval<=this.state.amount){
                this.setState({
                    reqnum : newval
                })
            }
        }
    },
	render:function(){
		var group = this.props.group;
		return(
			<div>
                <div className="row">
                    <div className="col-md-12">
                     <h1>{this.props.group.title}</h1>
                     <small>{this.props.group.id}</small>
                    </div>
                    <div className="col-md-6">
                        <div className="col-md-12">         
                            <img  src={group.img} className="img-responsive img-rounded" alt="Responsive image"/>
                        </div>
                    </div>

                    <div className="col-md-6">
                        <label>信息栏</label>
                        <h3>剩余数量：</h3>
                        <h3>到手单价：</h3>
                        <h3>国内快递运费：</h3>
                        <div className="col-xs-2">
                            <input className="form-control" type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
                        </div>
                        
                    </div>
                </div>
                
                <div className="row">
                    <div className="col-md-12">
                        <br/>
                        <br/>
                        <label>详细：</label>
                        <br/>
                        {group.desc}
                    </div>
                </div>


            </div>
		)		
	}
})