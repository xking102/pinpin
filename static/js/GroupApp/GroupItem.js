var React = require("react");


module.exports = React.createClass({
    getInitialState : function(){
        return{
            reqnum : 1,
            btn_buy_name: '购买',
            query_flag: false
        }    
    },
    handlerReqnum:function(e){
        var newval  = e.target.value;
        if(newval > 0){
            if(newval<=this.props.group.total_qty){
                this.setState({
                    reqnum : parseInt(newval)
                })
            }
        }
    },
    handlerOrder:function(e){
        if(this.state.query_flag){
            console.log('waiting');
        }else{
            var order ={
            gid:this.props.group.id,
            req_qty:this.state.reqnum,
            unit_price:this.props.group.unit_price,
            total_price:this.props.group.unit_price*this.state.reqnum,
            actual_price:this.props.group.unit_price*this.state.reqnum,
            actual_transfer_fee:0
        }
        this.setState({
            btn_buy_name:'稍等',
            query_flag: true
        });
        var data = {
            order:order
        };
        console.log(data);
        $.ajax({
            type:'post',
            url:'/api/v1/orders/',
            data:data
        }).done(function (resp) {
            console.log(resp.status);
            if(resp.status == 201){
                this.setState({
                    btn_buy_name:'成功',
                    query_flag: false,
                });
            }
            else{
                this.setState({
                    btn_buy_name:'失败',
                    query_flag: false

                });
            }
            
                
        }.bind(this));
        }
        
    },
	render:function(){
		var group = this.props.group;
        var styleObj={
            width: '45px',
        }
		return(
			<div>
  
              <div className="box span6">
                <div className="box-header" data-original-title>
                  <h2>
                  <i className="halflings-icon picture"></i>
                  <span className="break"></span>
                  {group.title}</h2>
                </div>
            
                <div className="box-content">
                  <img className="grayscale" src="/static/imgs/groups/2.png" alt="Sample Image 1"/>
                </div>
            
              </div>
            
            
              <div className="box span4">
                
                <div className="box-header" data-original-title>
                  <h2>
                  <i className="halflings-icon list-alt"></i>
                  <span className="break"></span>
                  购买信息</h2>
                </div>
            
                <div className="box-content">
                  <h3>到手价：{group.unit_price}</h3>
                  <h3>原价：{group.list_price}</h3>
                  <h3>剩余数：{group.total_qty}</h3>
                  <div className="row-fluid">
            
                    <div className="span2">
                      <input  style={styleObj} type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
                    </div>
            
                    <div className="span2">
                      <a href="#" onClick={this.handlerOrder} className="btn btn-danger">{this.state.btn_buy_name}</a>
                    </div>
                    
                  </div>
            
                </div>
                
              </div>


              <div className="box span10">
                <div className="box-header" data-original-title>
                  <h2>
                  <i className="halflings-icon book"></i>
                  <span className="break"></span>
                  详细描述</h2>
                </div>
            
                <div className="box-content">
                 {group.desc}
                </div>
            
              </div>

              
            </div>
		)		
	}
})