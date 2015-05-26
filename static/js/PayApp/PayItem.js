var React = require('react');



module.exports = React.createClass({
	getInitialState:function(){
		return {
			btn_name: '确认付款',
			query_flag: false,
			result:false,
			message:'',
      isPay:false
		}
	},
	handlerPay: function(){
		if(this.state.query_flag){
            console.log('waiting');
        }else{
          this.setState({
              btn_name:'正在付款',
              query_flag: true
          });
          $.ajax({
              type:'put',
              url:'/order_pay/'+this.props.order.id,
              contentType: "application/json",
          }).success(function (resp) {
              this.setState({
                      btn_name:'付款成功',
                      query_flag: true,
                      result:true,
                      isPay:true,
                      message:'{"text":"支付成功","layout":"bottomLeft","type":"information"}'
                  });
          }.bind(this))
          .error(function (resp){
            this.setState({
                      btn_name:'付款失败',
                      query_flag: false,
                      message:'{"text":"支付失败","layout":"bottomLeft","type":"information"}'
  
                  });
          }.bind(this));
          }
	},
	render:function(){
        var styleObj={
            display: 'block',
         };
        var PayContent = this.state.isPay||this.props.order.status==25 ? 
       <div>
 <div className="row-fluid">
            已支付 {this.props.order.total_price}
          </div>
 <a   href="/" className="btn btn-danger">去看看别的</a>   
       </div> :
         <div>
 <div className="row-fluid">
            共需要支付 {this.props.order.total_price}
          </div>

            
          <div className="row-fluid">
            <a href="#"  onClick={this.handlerPay} className="btn btn-danger">{this.state.btn_name}</a>   
          </div>
       </div> ;
		return (
			<div>
				<div className="box-header" data-original-title>
					<h2>
						<i className="halflings-icon user"></i>
						<span className="break"></span>
						支付
						</h2>	
				</div>

				<div className="box-content">
					{PayContent}
						

				</div>
			</div>

		)
	}
})
