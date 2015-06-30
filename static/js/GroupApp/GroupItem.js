var React = require("react");
var Steps = require('../Step/index');

var mui = require('material-ui');
var {Paper} = mui;

var AMUIReact = require('amazeui-react');
var {Grid, Col, ScrollSpy} = AMUIReact;


module.exports = React.createClass({
    contextTypes: {
      router: React.PropTypes.func.isRequired
    },
    getInitialState : function(){
        return{
            reqnum : 1,
            btn_buy_name: '购买',
            query_flag: false,
            desc:null
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
        this.setState({
            btn_buy_name:'稍等',
            query_flag: true
        });
        $.ajax({
          type:'post',
          url:'/api/v1/orders',
          contentType: "application/json",
          data:JSON.stringify({
            'gid':this.props.group.id,
            'req_qty':this.state.reqnum,
            'unit_price':this.props.group.unit_price,
            'total_price':this.props.group.unit_price*this.state.reqnum,
            'actual_price':this.props.group.unit_price*this.state.reqnum,
            'actual_transfer_fee':0
          }),
          success:function (resp) {
              if(resp.status=='succ'){
                this.setState({
                      btn_buy_name:'成功',
                      query_flag: false,
                });
                window.location.href='/u/order#/'+resp.oid+'/pay';
              }else{
                this.setState({
                      btn_buy_name:'卖光了',
                      query_flag: false,
                });
              }
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
            this.setState({
                      btn_buy_name:'失败',
                      query_flag: false
            });
          }.bind(this)
        });
      }
  },
  render:function(){
    var group = this.props.group;
    return(
      <div>
<ScrollSpy norepeat animation="slide-bottom" delay={1000}>
<Paper zDepth={3}>
<Grid className="doc-g" style={{marginLeft:'20px',paddingTop:'15px'}}>
{group.title}
</Grid>
<Grid className="doc-g">
  <Col sm={12} md={5} lg={5}>
   <img className="grayscale" src="/static/imgs/groups/700x500.png" />
  </Col>
  <Col sm={12} md={7} lg={7}>
    <p>到手价：{group.unit_price}</p>
    <p>原价：{group.list_price}</p>
    <p>剩余数：{group.total_qty}</p>
    <input style={{width:'45px',height:'30px'}} type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
    <br/>
    <a href="javascript:void(0)" onClick={this.handlerOrder} className="btn btn-danger">{this.state.btn_buy_name}</a>
  </Col>

</Grid>

<Grid className="doc-g" style={{marginTop:'10px'}}>
  <Col sm={12} md={12} lg={12}>
      {group.desc}


    
  </Col>
</Grid>
</Paper>
</ScrollSpy>
</div>

    )
  }


})
