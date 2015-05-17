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
                        <h1>Product Name</h1>
                    </div>
                </div>

                <div className="row">
                    <div className="col-md-7">
                        <div className="panel panel-default">
                             <div className="panel-heading">
                                <div className="panel-title">Product Images</div>
                            </div>
                            <div className="panel-body">
                                 <img alt="550x400" src="/static/imgs/groups/620x400.gif" />
                            </div>
                        </div>
                    </div>

                     <div className="col-md-5">
                        <div className="panel panel-default">
                             <div className="panel-heading">
                                <div className="panel-title">Product Name</div>
                            </div>
                            <div className="panel-body">
                                 <div className="col-md-12">
                                    <h4>description</h4>
                                    <p className="muted">
                                    Cras justo odio, dapibus ac facilisis in, egestas eget quam.Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
                                    </p>
                                 </div>
                                 <div className="col-md-12">
                                        <div className="row"><div className="col-md-5"><label>原到手价格：</label></div><div className="col-md-7"><s>￥200</s></div></div>
                                        <div className="row"><div className="col-md-5"><label>拼团价格：</label></div><div className="col-md-7"><strong>￥120</strong></div></div>
                                        <div className="row"><div className="col-md-5"><label>剩余拼团数量：</label></div><div className="col-md-7"><strong>35</strong></div></div>
                                 </div>
                                 <div className="col-md-12">
                                    <div className="col-md-3">
                                        <input className="form-control"  type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
                                 
                                    </div>

                                    <div className="col-md-6">
                                        <a href="#"className="btn btn-danger">购买</a>
                                 
                                    </div>

                                 </div>
                            </div>
                        </div>
                    </div>

                </div>



            <div className="col-md-4">
                <div className="panel panel-default">
                    <div className="panel-heading">
                    <div className="panel-title">FAQ</div>
                </div>
                    <div className="panel-body">
                       <li>1</li>
                       <li>2</li>
                       <li>3</li>
                       <li>4</li>
                       <li>5</li>
                       <li>6</li>
                    </div>
                    </div>
             </div>
                 


            </div>
		)		
	}
})