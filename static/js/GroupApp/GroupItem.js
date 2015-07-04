var React = require("react");
var Steps = require('../Step/index');

var mui = require('material-ui');
var {Paper} = mui;

var AMUIReact = require('amazeui-react');
var {Grid, Col, ScrollSpy} = AMUIReact;

var ImageList = require('./GroupImageList');
var PropertyList =require('./GroupPropertyList');

module.exports = React.createClass({
    getInitialState : function(){
        return{
            reqnum : 1,
            btn_buy_name: '购买',
            query_flag: false,
            desc:null,
            clickimage:'',
            clickcolor:'',
            clicksize:'',
            clickother:''
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
        var colorcheck = '';
        var sizecheck = '';
        var othercheck = '';
        if(this.props.group.color.length){
          if(this.state.clickcolor){
            var colorcheck = '颜色:'+this.state.clickcolor+' ';
          }else{
            var colorcheck = '颜色:'+this.props.group.color[0]+' ';
          }
        }
        if(this.props.group.size.length){
          if(this.state.clicksize){
            var sizecheck = '尺码:'+this.state.clicksize+' ';
          }else{
            var sizecheck = '尺码:'+this.props.group.size[0]+' ';
          }
        }
        if(this.props.group.other.length){
          if(this.state.clickother){
            var othercheck = '其他:'+this.state.clickother+' ';
          }else{
            var othercheck = '其他:'+this.props.group.other[0]+' ';
          }
        }
        var memo = colorcheck + sizecheck + othercheck;
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
            'actual_transfer_fee':0,
            'memo':memo
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
    var clickimage = this.state.clickimage.length?this.state.clickimage:group.image+'.big.png';
    return(
      <div>
<ScrollSpy norepeat animation="slide-bottom" delay={1000}>
<Paper zDepth={3}>
<Grid className="doc-g" style={{marginLeft:'20px',paddingTop:'15px'}}>
{group.title}
</Grid>
<Grid className="doc-g" style={{marginTop:'10px'}}>
  <Col sm={12} md={5} lg={5}>
   <img className="grayscale" src={clickimage} />
  </Col>

  
  <Col sm={12} md={7} lg={7}>
    <p>到手价：{group.unit_price}</p>
    <p>剩余数：{group.total_qty-group.req_qty-group.confirm_qty}</p>
    <Col sm={12} md={7} lg={7}>
    <PropertyList properties={group.color} label={'颜色'} onCheck={this._handleColorCheck} />
    </Col>

    <Col sm={12} md={7} lg={7}>
    <PropertyList properties={group.size} label={'尺码'} onCheck={this._handleSizeCheck} />
    </Col>

    <Col sm={12} md={7} lg={7}>
    <PropertyList properties={group.other} label={'其他'} onCheck={this._handleOtherCheck} />
    </Col>

    <Col style={{marginTop:'10px'}} sm={12} md={7} lg={7}>
    <input style={{width:'45px',height:'30px'}} type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
    <br/>
    <a href="javascript:void(0)" onClick={this.handlerOrder} className="btn btn-danger">{this.state.btn_buy_name}</a>
    </Col>
    
  </Col>

</Grid>

<Grid className="doc-g" style={{marginTop:'10px'}}>
  <Col sm={12} md={12} lg={12}>
  <ImageList imgs={group.images} ImageChange={this._handleImageChange} />
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
  },

  _handleImageChange:function(img){
    this.setState({
      clickimage:img
    })
   
  },

  _handleColorCheck:function(color){
    this.setState({
      clickcolor:color
    })
   
  },

  _handleSizeCheck:function(size){
    this.setState({
      clicksize:size
    })
   
  },

  _handleOtherCheck:function(other){
    this.setState({
      clickother:other
    })
   
  },

})
